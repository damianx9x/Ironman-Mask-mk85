import pwmio
from adafruit_motor import servo
import config

# Inicjalizacja PWM dla serw
# Używamy częstotliwości 50Hz (standard dla serw modelarskich)
pwm_s1 = pwmio.PWMOut(config.PIN_SERVO_LEFT, duty_cycle=2 ** 15, frequency=50)
pwm_s2 = pwmio.PWMOut(config.PIN_SERVO_RIGHT, duty_cycle=2 ** 15, frequency=50)

# Tworzenie obiektów serw
s1 = servo.Servo(pwm_s1)
s2 = servo.Servo(pwm_s2)

def set_raw(servo_obj, angle):
    """
    Bezpieczne ustawianie kąta serwa.
    Ignoruje błędy, jeśli serwo chwilowo nie odpowiada.
    """
    try:
        servo_obj.angle = angle
    except Exception:
        pass # Ignorujemy błędy, żeby nie zawiesić systemu