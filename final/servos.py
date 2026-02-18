import config

try:
    import pwmio
except Exception as e:
    pwmio = None
    print("BLAD SERWO: brak pwmio:", e)

try:
    from adafruit_motor import servo as adafruit_servo
except Exception as e:
    try:
        import servo as adafruit_servo
        print("SERWO: fallback na servo.py")
    except Exception:
        adafruit_servo = None
        print("BLAD SERWO: brak adafruit_motor/servo:", e)


def _clamp_angle(angle):
    val = int(round(float(angle)))
    if val < config.SERVO_MIN_ANGLE:
        return config.SERVO_MIN_ANGLE
    if val > config.SERVO_MAX_ANGLE:
        return config.SERVO_MAX_ANGLE
    return val


_hardware_ready = False

pwm_s1 = None
pwm_s2 = None
s1 = None
s2 = None

if pwmio and adafruit_servo:
    try:
        pwm_s1 = pwmio.PWMOut(config.PIN_SERVO_LEFT, duty_cycle=0, frequency=50)
        pwm_s2 = pwmio.PWMOut(config.PIN_SERVO_RIGHT, duty_cycle=0, frequency=50)
        s1 = adafruit_servo.Servo(
            pwm_s1,
            min_pulse=config.SERVO_MIN_PULSE,
            max_pulse=config.SERVO_MAX_PULSE,
        )
        s2 = adafruit_servo.Servo(
            pwm_s2,
            min_pulse=config.SERVO_MIN_PULSE,
            max_pulse=config.SERVO_MAX_PULSE,
        )
        _hardware_ready = True
    except Exception as e:
        print("BLAD SERWO: init nieudany:", e)
        _hardware_ready = False

_released = False
_last_left = _clamp_angle(config.S1_OPEN)
_last_right = _clamp_angle(config.S2_OPEN)


def set_raw(servo_obj, angle):
    global _released, _last_left, _last_right
    safe_angle = _clamp_angle(angle)
    if servo_obj is s1:
        _last_left = safe_angle
    elif servo_obj is s2:
        _last_right = safe_angle

    if (not _hardware_ready) or (servo_obj is None):
        return

    try:
        servo_obj.angle = safe_angle
        _released = False
    except Exception:
        pass


def set_pair(left_angle, right_angle):
    set_raw(s1, left_angle)
    set_raw(s2, right_angle)


def release_all():
    global _released
    if not _hardware_ready:
        _released = True
        return

    try:
        s1.angle = None
        s2.angle = None
        _released = True
        return
    except Exception:
        pass

    try:
        pwm_s1.duty_cycle = 0
        pwm_s2.duty_cycle = 0
        _released = True
    except Exception:
        pass


def engage_at_last_position():
    set_pair(_last_left, _last_right)


def is_released():
    return _released
