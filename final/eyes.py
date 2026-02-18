import pwmio
import config

eye_pwm = pwmio.PWMOut(config.PIN_EYES, frequency=5000, duty_cycle=0)


def set_brightness(val):
    if val < 0:
        val = 0
    if val > 1:
        val = 1
    eye_pwm.duty_cycle = int(val * 65535)
