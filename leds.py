import neopixel
import config
import math
import random

# Inicjalizacja pasków LED
strip_dome = neopixel.NeoPixel(config.PIN_LED_DOME, config.NUM_LEDS_DOME, brightness=0.5, auto_write=False)
strip_jaw  = neopixel.NeoPixel(config.PIN_LED_JAW, config.NUM_LEDS_JAW, brightness=0.5, auto_write=False)

def wheel(pos):
    # Pomocnicza funkcja do kolorów tęczy (0-255)
    if pos < 0 or pos > 255: return (0, 0, 0)
    if pos < 85: return (255 - pos * 3, pos * 3, 0)
    if pos < 170: pos -= 85; return (0, 255 - pos * 3, pos * 3)
    pos -= 170; return (pos * 3, 0, 255 - pos * 3)

def update(now, is_moving, is_open, jaw_detached, dist, anim_mode):
    """
    Główna funkcja sterująca kolorami.
    """
    # --- PRIORYTETY SYSTEMOWE (OSTRZEŻENIA) ---
    if jaw_detached:
        strip_jaw.fill((0, 0, 0)) # Wyłączone jak odpięte
        strip_dome.fill((200, 200, 200)) # Latarka
        strip_dome.show(); strip_jaw.show()
        return
    elif is_moving:
        strip_jaw.fill((255, 0, 0)) # Czerwony - Ostrzeżenie (Ruch)
        strip_dome.fill((255, 0, 0))
        strip_dome.show(); strip_jaw.show()
        return
    elif dist < config.LASER_DIST_LIMIT:
        strip_jaw.fill((0, 255, 0)) # Zielony - Widzę rękę!
        strip_dome.show(); strip_jaw.show()
        return

    # --- ANIMACJE UŻYTKOWNIKA (Gdy maska stoi) ---
    # Wybieramy efekt na podstawie config.ANIMATION_MODE
    
    # 1. SOLID (Stały Turkus - Klasyk)
    if anim_mode == 1:
        strip_dome.fill((0, 100, 255))
        strip_jaw.fill((0, 0, 50) if is_open else (0,0,0))

    # 2. BREATHING (Oddychanie - Domyślny)
    elif anim_mode == 2:
        pulse = (math.sin(now * 3) + 1) / 2 * 150
        strip_dome.fill((0, int(pulse*0.5), int(pulse)))
        strip_jaw.fill((0, 0, int(pulse*0.2)) if is_open else (0,0,0))

    # 3. LARSON SCANNER (Cylon / KITT)
    elif anim_mode == 3:
        strip_dome.fill((0,0,0))
        pos = int((math.sin(now * 5) + 1) / 2 * (config.NUM_LEDS_DOME - 1))
        strip_dome[pos] = (255, 0, 0)
        if pos > 0: strip_dome[pos-1] = (50, 0, 0)
        if pos < config.NUM_LEDS_DOME-1: strip_dome[pos+1] = (50, 0, 0)

    # 4. RAINBOW CYCLE (Tęcza)
    elif anim_mode == 4:
        for i in range(config.NUM_LEDS_DOME):
            idx = int((i * 256 / config.NUM_LEDS_DOME) + now * 50) & 255
            strip_dome[i] = wheel(idx)

    # 5. STROBE (Ostrzegawczy)
    elif anim_mode == 5:
        if int(now * 10) % 2 == 0:
            strip_dome.fill((255, 255, 255))
        else:
            strip_dome.fill((0, 0, 0))

    # 6. SPARKLE (Iskrzenie)
    elif anim_mode == 6:
        strip_dome.fill((0, 0, 20))
        if random.random() < 0.1:
            strip_dome[random.randint(0, config.NUM_LEDS_DOME-1)] = (255, 255, 255)

    # 7. TRAFFIC LIGHT (Sygnalizacja)
    elif anim_mode == 7:
        phase = int(now) % 3
        col = (255,0,0) if phase == 0 else ((255,100,0) if phase == 1 else (0,255,0))
        strip_dome.fill(col)

    # 8. POLICE (Policja)
    elif anim_mode == 8:
        if int(now * 4) % 2 == 0:
            strip_dome.fill((255, 0, 0))
        else:
            strip_dome.fill((0, 0, 255))

    # 9. MATRIX (Zielony deszcz)
    elif anim_mode == 9:
        strip_dome.fill((0,0,0))
        for i in range(config.NUM_LEDS_DOME):
            if random.random() < 0.2:
                strip_dome[i] = (0, 255, 0)

    # 10. HEARTBEAT (Bicie serca)
    elif anim_mode == 10:
        x = now * 3
        # Funkcja symulująca bicie serca
        bright = max(0, math.sin(x) * math.sin(x*3) * 255)
        strip_dome.fill((int(bright), 0, 0))

    # HUD w szczęce (jeśli nie ma specyficznej animacji, gaśnie przy zamknięciu)
    if anim_mode not in [1, 2] and not is_open:
        strip_jaw.fill((0,0,0))
        
    strip_dome.show()
    strip_jaw.show()