import pwmio
import config

# Inicjalizacja PWM dla oczu (LED)
# Częstotliwość 5000Hz zapewnia brak migotania w kamerze
eye_pwm = pwmio.PWMOut(config.PIN_EYES, frequency=5000, duty_cycle=0)

def set_brightness(val):
    """
    Ustawia jasność oczu.
    val: od 0.0 (wyłączone) do 1.0 (max)
    """
    if val < 0: val = 0
    if val > 1: val = 1
    # Przeliczenie 0.0-1.0 na zakres 0-65535 (16-bit)
    eye_pwm.duty_cycle = int(val * 65535)