import board
import digitalio

# Klasa odpowiedzialna za sprawdzanie, czy szczęka jest podpięta
class JawMonitor:
    def __init__(self, pin_id=board.D10):
        """
        Konfiguracja pinu detekcji.
        Używamy trybu Pull-Up (stan wysoki, gdy nic nie jest podłączone).
        """
        self.pin = digitalio.DigitalInOut(pin_id)
        self.pin.direction = digitalio.Direction.INPUT
        self.pin.pull = digitalio.Pull.UP

    @property
    def is_detached(self):
        """
        Sprawdza stan:
        True (Prawda) = Szczęka ODPIĘTA (Obwód otwarty)
        False (Fałsz) = Szczęka WPIĘTA (Obwód zamknięty do masy)
        """
        return self.pin.value