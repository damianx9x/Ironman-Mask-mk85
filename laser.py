import board
import busio
import adafruit_vl53l0x
import config

# Inicjalizacja I2C dla lasera
i2c = busio.I2C(config.PIN_LASER_SCL, config.PIN_LASER_SDA)

sensor = None

try:
    sensor = adafruit_vl53l0x.VL53L0X(i2c)
    # Zwiększenie budżetu czasowego dla lepszej precyzji (opcjonalne)
    sensor.measurement_timing_budget = 200000 
except Exception:
    print("BŁĄD LASERA: Nie wykryto czujnika VL53L0X!")

def get_distance():
    """
    Zwraca odległość w milimetrach.
    Jeśli błąd, zwraca 9999 (poza zasięgiem).
    """
    if not sensor:
        return 9999
    try:
        return sensor.range
    except Exception:
        return 9999