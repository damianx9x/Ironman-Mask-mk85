import board
import digitalio
import time


class JawMonitor:
    def __init__(self, pin_id=board.D10, enabled=True, active_level=True, debounce_s=0.12):
        self.enabled = bool(enabled)
        self.active_level = bool(active_level)
        self.debounce_s = max(0.0, float(debounce_s))
        self.pin = None
        self._stable = False
        self._candidate = False
        self._changed_at = time.monotonic()

        if not self.enabled:
            return

        self.pin = digitalio.DigitalInOut(pin_id)
        self.pin.direction = digitalio.Direction.INPUT
        self.pin.pull = digitalio.Pull.UP

        initial = self._read_detached_raw()
        self._stable = initial
        self._candidate = initial

    def _read_detached_raw(self):
        if (not self.enabled) or (self.pin is None):
            return False
        try:
            pin_val = bool(self.pin.value)
            return pin_val if self.active_level else (not pin_val)
        except Exception:
            return False

    @property
    def raw_detached(self):
        return self._read_detached_raw()

    @property
    def is_detached(self):
        if not self.enabled:
            return False

        now = time.monotonic()
        raw = self._read_detached_raw()

        if raw != self._candidate:
            self._candidate = raw
            self._changed_at = now
        elif self._stable != self._candidate and (now - self._changed_at) >= self.debounce_s:
            self._stable = self._candidate

        return self._stable
