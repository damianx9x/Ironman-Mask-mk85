import config
import time

try:
    import busio
except Exception as e:
    busio = None
    print("BLAD LASERA: brak busio:", e)

try:
    import adafruit_vl53l0x
except Exception as e:
    adafruit_vl53l0x = None
    print("BLAD LASERA: brak adafruit_vl53l0x:", e)


i2c = None
sensor = None
_last_init_try = 0.0
_last_init_error = None
_last_read_error = None
_INIT_RETRY_S = 1.0


def _init_sensor(force=False):
    global i2c, sensor, _last_init_try, _last_init_error

    if sensor is not None:
        return True
    if (not busio) or (not adafruit_vl53l0x):
        return False

    now = time.monotonic()
    if (not force) and (now - _last_init_try) < _INIT_RETRY_S:
        return False
    _last_init_try = now

    try:
        if i2c is None:
            i2c = busio.I2C(config.PIN_LASER_SCL, config.PIN_LASER_SDA)
        sensor = adafruit_vl53l0x.VL53L0X(i2c)
        sensor.measurement_timing_budget = config.LASER_TIMING_BUDGET_US
        if _last_init_error is not None:
            print("LASER: VL53L0X recovered")
        _last_init_error = None
        return True
    except Exception as e:
        msg = str(e)
        if msg != _last_init_error:
            print("BLAD LASERA: init VL53L0X nieudany:", e)
            _last_init_error = msg
        sensor = None
        return False


_init_sensor(force=True)


def get_distance():
    global sensor, _last_read_error
    if sensor is None and (not _init_sensor(force=False)):
        return 9999

    try:
        d = sensor.range
        _last_read_error = None
        return d
    except Exception as e:
        msg = str(e)
        if msg != _last_read_error:
            print("BLAD LASERA: odczyt range nieudany:", e)
            _last_read_error = msg
        sensor = None
        return 9999
