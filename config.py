import board

# ==============================================================================
# PLIK KONFIGURACYJNY - IRON MAN MARK LXXXV (MARK 85)
# Tutaj zmieniasz ustawienia. Nie musisz dotykać innych plików!
# ==============================================================================

# --- 1. PODŁĄCZENIA (PINY NA PŁYTCE) ---
# Jeśli zmienisz kabelki, zmień to tutaj.

PIN_POWER       = board.GPIO23  # "Włącznik główny" dla prądu (Serwa, LED, Audio)
PIN_BUTTON      = board.GPIO19  # Przycisk manualny (Terminal 'Btn')
PIN_JAW_SENSE   = board.D10     # Kabel sprawdzający czy szczęka jest wpięta

# Serwa (Silniki)
PIN_SERVO_LEFT  = board.D11     # Lewe serwo
PIN_SERVO_RIGHT = board.D12     # Prawe serwo

# Oświetlenie
PIN_EYES        = board.D5      # Oczy (zwykłe LEDy)
PIN_LED_DOME    = board.TX      # Pasek LED wewnątrz kasku (GPIO 0)
PIN_LED_JAW     = board.RX      # Pasek LED w szczęce (GPIO 1)

# Laser (Czujnik odległości)
PIN_LASER_SDA   = board.SDA     # Dane lasera (GPIO 2)
PIN_LASER_SCL   = board.SCL     # Zegar lasera (GPIO 3)

# Audio (Głośnik jest na stałe podpięty do I2S Amp)
# Mikrofon (INMP441)
PIN_MIC_SCK     = board.SCK     # Zegar mikrofonu (GPIO 14)
PIN_MIC_WS      = board.MISO    # Word Select (GPIO 8) - UWAGA: Mapowanie niestandardowe
PIN_MIC_SD      = board.MOSI    # Dane mikrofonu (GPIO 15)

# --- 2. USTAWIENIA RUCHU (SERWA) ---
# Kąty serw (0-180 stopni). Musisz to dobrać eksperymentalnie, żeby nic nie połamać!
S1_OPEN  = 160  # Pozycja otwarta (Lewe)
S1_CLOSE = 20   # Pozycja zamknięta (Lewe)

S2_OPEN  = 20   # Pozycja otwarta (Prawe - zazwyczaj odwrotnie niż lewe)
S2_CLOSE = 160  # Pozycja zamknięta (Prawe)

# Szybkość ruchu
SERVO_SPEED_DELAY = 0.01  # Czas (w sekundach) między kroczkami. Więcej = Wolniej.
SERVO_STEP        = 2.0   # O ile stopni przesuwa się serwo w jednym kroku. Mniej = Płynniej.

# --- 3. USTAWIENIA LASERA (STEROWANIE RĘKĄ) ---
LASER_DIST_LIMIT = 200  # Maksymalna odległość wykrywania ręki (w milimetrach). Max 2000mm (2m).
LASER_DEBOUNCE   = 3    # Ile razy pod rząd musi zobaczyć rękę, żeby zareagować (ochrona przed błędami).
LASER_HOLD_TIME  = 3.0  # Ile sekund trzeba trzymać rękę, żeby otworzyć maskę.

# --- 4. INNE USTAWIENIA ---
ANIMATION_MODE   = 1    # Wybrana animacja LED (1-10)
AUTO_CLOSE_DELAY = 5.0  # Po ilu sekundach maska sama się zamknie (jeśli otwarta laserem).
EYE_MAX_BRIGHT   = 1.0  # Jasność oczu (0.0 to wyłączone, 1.0 to max).
LED_UPDATE_DELAY = 0.03 # Szybkość odświeżania animacji LED (im mniej, tym płynniej, ale obciąża procesor).

# Liczba diod w paskach
NUM_LEDS_DOME = 15
NUM_LEDS_JAW  = 8

# --- 5. DŹWIĘKI (NAZWY PLIKÓW) ---
# Pliki muszą być w folderze /sounds na płytce
SND_STARTUP = "startup.wav"
SND_OPEN    = "open.wav"
SND_CLOSE   = "close.wav" # Dźwięk zamykania (opcjonalny)

# --- 6. TRYB SHOW OFF (DEMO NA PÓŁKĘ) ---
SHOW_OFF_ENABLED = False # Czy tryb demo jest włączony?
SHOW_OFF_INTERVAL = 10.0 # Co ile sekund maska ma coś zrobić w trybie demo