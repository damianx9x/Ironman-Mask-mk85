import time
import digitalio
import board
import supervisor
import sys
import json
import random

# --- IMPORT MODUŁÓW PROJEKTU ---
# Każdy plik odpowiada za inną część hełmu
import config
import servos
import eyes
import leds
import audio_sys
import laser
import voice
import ubieranie
import comms # Nowy moduł komunikacji

# ==============================================================================
# IRON MAN MARK LXXXV - GŁÓWNY SYSTEM (BRAIN)
# Wersja: V0.8.5 (Endgame Edition)
# ==============================================================================

# ==============================================================================
# SEKCJA 1: PRZYGOTOWANIE SPRZĘTU (SETUP)
# ==============================================================================
print("\n>>> URUCHAMIANIE SYSTEMU MARK 85...")

# 1. Włączamy główne zasilanie dla dodatków (Serwa, LEDy, Audio)
# Bez tego pinu (GPIO 23) nic poza procesorem nie zadziała!
power = digitalio.DigitalInOut(config.PIN_POWER)
power.direction = digitalio.Direction.OUTPUT
power.value = True
time.sleep(1.0) # Czekamy sekundę, aż kondensatory się naładują

# 2. Konfiguracja przycisku manualnego
btn = digitalio.DigitalInOut(config.PIN_BUTTON)
btn.direction = digitalio.Direction.INPUT
btn.pull = digitalio.Pull.UP

# 3. Inicjalizacja modułów (Głos, Szczęka)
voice_mod = voice.VoiceChanger(audio_sys.audio_out) if audio_sys.audio_out else None
jaw_mon = ubieranie.JawMonitor(config.PIN_JAW_SENSE)

# ==============================================================================
# SEKCJA 2: ZMIENNE STANU (PAMIĘĆ ROBOCZA)
# ==============================================================================
# Czy maska jest otwarta?
is_open = True

# Cele dla serw (dokąd mają jechać)
target_s1, target_s2 = config.S1_OPEN, config.S2_OPEN
# Aktualna pozycja serw (gdzie są teraz)
current_s1, current_s2 = float(config.S1_OPEN), float(config.S2_OPEN)

# Flagi logiczne
manual_open = True  # Czy otwarto przyciskiem? (Wtedy nie zamyka się sama)
laser_detection_stack = 0 # Licznik potwierdzeń lasera (anty-szum)

# Liczniki czasu (do opóźnień bez zatrzymywania procesora)
last_servo_time = 0
last_laser_time = 0
last_presence_time = time.monotonic()
last_led_time = 0
laser_hold_start = 0
current_dist = 9999
last_btn_time = 0
BUTTON_COOLDOWN = 1.5 # Blokada przycisku na 1.5s po użyciu
last_showoff_time = 0 # Czas ostatniej akcji w trybie demo

# ==============================================================================
# SEKCJA 3: START SYSTEMU
# ==============================================================================
# Ustawiamy serwa na start
servos.set_raw(servos.s1, config.S1_OPEN)
time.sleep(0.2)
servos.set_raw(servos.s2, config.S2_OPEN)

# Efekty startowe
eyes.set_brightness(0.0)
audio_sys.play(config.SND_STARTUP)

# Zapamiętujemy stan przycisku
btn_prev_state = btn.value

# ==============================================================================
# SEKCJA 4: PĘTLA GŁÓWNA (TO DZIEJE SIĘ W KÓŁKO)
# ==============================================================================
while True:
    now = time.monotonic()

    # --- KROK 0: SPRAWDŹ KOMENDY Z KOMPUTERA ---
    # Przekazujemy moduły, żeby comms.py mógł nimi sterować
    comms.check_usb_commands(servos, audio_sys, eyes)

    # Jeśli jesteśmy w trybie strojenia (Dashboard podłączony),
    # aktualizujemy cele serw na bieżąco z configu i POMIJAMY resztę logiki (laser itp.)
    if comms.tuning_mode:
        if is_open: target_s1, target_s2 = config.S1_OPEN, config.S2_OPEN
        else:       target_s1, target_s2 = config.S1_CLOSE, config.S2_CLOSE
        # Tutaj kod leci dalej tylko do sekcji RUCH SERW i LED, pomijając logikę czujników

    # --- KROK 0.5: TRYB SHOW OFF (DEMO) ---
    # Jeśli włączony w configu i szczęka jest wpięta
    if config.SHOW_OFF_ENABLED and not jaw_detached and not comms.tuning_mode:
        if (now - last_showoff_time) > config.SHOW_OFF_INTERVAL:
            # Losujemy akcję
            action = random.randint(0, 3)
            
            if action == 0: # Otwórz/Zamknij
                if is_open:
                    target_s1, target_s2 = config.S1_CLOSE, config.S2_CLOSE
                    audio_sys.play(config.SND_CLOSE) # Używamy konfigurowalnego dźwięku
                    is_open = False
                else:
                    target_s1, target_s2 = config.S1_OPEN, config.S2_OPEN
                    audio_sys.play(config.SND_OPEN)
                    is_open = True
            elif action == 1: # Zmień animację losowo
                config.ANIMATION_MODE = random.randint(1, 10)
            elif action == 2: # Mrugnij oczami (tylko jak zamknięta)
                if not is_open:
                    eyes.set_brightness(0.0); time.sleep(0.1); eyes.set_brightness(config.EYE_MAX_BRIGHT)
            
            last_showoff_time = now

    # --- KROK 1: CZY SZCZĘKA JEST NA MIEJSCU? ---
    jaw_detached = jaw_mon.is_detached
    # jaw_detached = False # ODKOMENTUJ TYLKO DO TESTÓW BEZ SZCZĘKI

    if jaw_detached:
        # >>> TRYB ZAKŁADANIA (WEAR MODE) <<<
        # Jeśli szczęka odpięta -> Otwórz wszystko, wyłącz bajery.
        target_s1, target_s2 = config.S1_OPEN, config.S2_OPEN
        is_open = True
        manual_open = True

        if voice_mod: voice_mod.deactivate()

        # Reset czujników
        laser_detection_stack = 0
        laser_hold_start = 0

    # --- KROK 2: RUCH SERW (PŁYNNY) ---
    # Sprawdzamy, czy serwa są tam gdzie powinny być. Jeśli nie, przesuwamy o kawałek.
    diff1 = abs(current_s1 - target_s1)
    diff2 = abs(current_s2 - target_s2)
    is_moving = (diff1 > 0.5) or (diff2 > 0.5)

    if is_moving and (now - last_servo_time > config.SERVO_SPEED_DELAY):
        # Logika płynnego ruchu (Smooth Sweep)
        if diff1 > 0.5:
            step = config.SERVO_STEP if target_s1 > current_s1 else -config.SERVO_STEP
            current_s1 += step if abs(current_s1 - target_s1) >= config.SERVO_STEP else (target_s1 - current_s1)
        if diff2 > 0.5:
            step = config.SERVO_STEP if target_s2 > current_s2 else -config.SERVO_STEP
            current_s2 += step if abs(current_s2 - target_s2) >= config.SERVO_STEP else (target_s2 - current_s2)
        servos.set_raw(servos.s1, int(current_s1))
        servos.set_raw(servos.s2, int(current_s2))
        last_servo_time = now

    # --- KROK 3: OBSŁUGA PRZYCISKU ---
    # Tylko gdy szczęka jest wpięta i NIE stroimy maski
    if not jaw_detached and not comms.tuning_mode:
        btn_current_state = btn.value
        if not btn_current_state and btn_prev_state: # Wykryto wciśnięcie
            if (now - last_btn_time) > BUTTON_COOLDOWN:
                if is_open:
                    # Zamykanie
                    target_s1, target_s2 = config.S1_CLOSE, config.S2_CLOSE
                    audio_sys.play(config.SND_CLOSE if hasattr(config, 'SND_CLOSE') else config.SND_OPEN)
                    is_open = False
                    manual_open = False
                else:
                    # Otwieranie
                    target_s1, target_s2 = config.S1_OPEN, config.S2_OPEN
                    audio_sys.play(config.SND_OPEN)
                    is_open = True
                    manual_open = True
                last_btn_time = now
        btn_prev_state = btn_current_state

    # --- KROK 4: OBSŁUGA LASERA (GESTRY RĘKĄ) ---
    # Wyłączamy laser w trybie strojenia, żeby nie przeszkadzał
    if not jaw_detached and not is_moving and not comms.tuning_mode and (now - last_laser_time > 0.05):
        d = laser.get_distance()
        current_dist = d

        # Czy ręka jest w zasięgu? (3cm - 13cm)
        if 30 < d < config.LASER_DIST_LIMIT:
            laser_detection_stack += 1
        else:
            laser_detection_stack = 0

        # Jeśli sygnał jest stabilny (ręka jest pewna)
        if laser_detection_stack >= config.LASER_DEBOUNCE:
            last_presence_time = now
            if manual_open: manual_open = False

            if not is_open:
                # Odliczanie czasu trzymania ręki (HOLD)
                if laser_hold_start == 0: laser_hold_start = now

                # Otwarcie po czasie HOLD
                if (now - laser_hold_start > config.LASER_HOLD_TIME):
                    target_s1, target_s2 = config.S1_OPEN, config.S2_OPEN
                    audio_sys.play(config.SND_OPEN)
                    is_open = True
                    laser_hold_start = 0
        else:
            # Ręka zabrana
            laser_hold_start = 0
            if is_open and not manual_open:
                # Auto-zamykanie po czasie
                if (now - last_presence_time) > config.AUTO_CLOSE_DELAY:
                    target_s1, target_s2 = config.S1_CLOSE, config.S2_CLOSE
                    audio_sys.play(config.SND_CLOSE if hasattr(config, 'SND_CLOSE') else config.SND_OPEN)
                    is_open = False
        last_laser_time = now

    # --- KROK 5: MODULATOR GŁOSU ---
    # Działa tylko gdy serwa stoją (żeby nie było zakłóceń)
    if voice_mod and not jaw_detached:
        if is_moving:
            voice_mod.deactivate()
        else:
            voice_mod.activate()
            voice_mod.update()

    # --- KROK 6: EFEKTY ŚWIETLNE (LED) ---
    if now - last_led_time > config.LED_UPDATE_DELAY:
        leds.update(now, is_moving, is_open, jaw_detached, current_dist, config.ANIMATION_MODE)
        last_led_time = now

    # Sterowanie jasnością oczu
    if not is_open and not is_moving and not jaw_detached:
        eyes.set_brightness(config.EYE_MAX_BRIGHT)
    else:
        eyes.set_brightness(0.0)