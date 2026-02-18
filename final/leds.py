import math
import random
import config

try:
    import neopixel
except Exception as e:
    neopixel = None
    print("BLAD LED: brak neopixel:", e)


class _NullStrip:
    def __init__(self, length):
        try:
            self._n = max(1, int(length))
        except Exception:
            self._n = 1

    def __len__(self):
        return self._n

    def __setitem__(self, idx, value):
        return

    def fill(self, color):
        return

    def show(self):
        return


if neopixel:
    try:
        strip_dome = neopixel.NeoPixel(
            config.PIN_LED_DOME,
            config.NUM_LEDS_DOME,
            brightness=0.45,
            auto_write=False,
        )
        strip_jaw = neopixel.NeoPixel(
            config.PIN_LED_JAW,
            config.NUM_LEDS_JAW,
            brightness=0.45,
            auto_write=False,
        )
    except Exception as e:
        print("BLAD LED: init paskow nieudany:", e)
        strip_dome = _NullStrip(config.NUM_LEDS_DOME)
        strip_jaw = _NullStrip(config.NUM_LEDS_JAW)
else:
    strip_dome = _NullStrip(config.NUM_LEDS_DOME)
    strip_jaw = _NullStrip(config.NUM_LEDS_JAW)


def wheel(pos):
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)


def _set_scanner(strip, now, speed, head, tail):
    strip.fill((0, 0, 0))
    pos = int((math.sin(now * speed) + 1.0) * 0.5 * (len(strip) - 1))
    strip[pos] = head
    if pos > 0:
        strip[pos - 1] = tail
    if pos < len(strip) - 1:
        strip[pos + 1] = tail


def _jaw_idle_fill(is_open):
    if is_open:
        strip_jaw.fill((0, 12, 34))
    else:
        strip_jaw.fill((0, 0, 0))


def update(now, is_moving, is_open, jaw_detached, dist, anim_mode, demo_active=False):
    if jaw_detached:
        pulse = int((math.sin(now * 2.5) + 1.0) * 0.5 * 180) + 30
        strip_dome.fill((pulse, pulse, pulse))
        strip_jaw.fill((0, 0, 0))
        strip_dome.show()
        strip_jaw.show()
        return

    if demo_active:
        for i in range(config.NUM_LEDS_DOME):
            idx = int((i * 256 / config.NUM_LEDS_DOME) + now * 90) & 255
            strip_dome[i] = wheel(idx)
        for i in range(config.NUM_LEDS_JAW):
            idx = int((255 - i * 256 / config.NUM_LEDS_JAW) + now * 120) & 255
            strip_jaw[i] = wheel(idx)
        if int(now * 8) % 2 == 0:
            strip_dome[random.randint(0, config.NUM_LEDS_DOME - 1)] = (255, 255, 255)
        strip_dome.show()
        strip_jaw.show()
        return

    if is_moving:
        _set_scanner(strip_dome, now, 8.0, (255, 70, 0), (90, 20, 0))
        strip_jaw.fill((70, 10, 0))
        strip_dome.show()
        strip_jaw.show()
        return

    hand_present = config.LASER_MIN_VALID_MM <= dist <= config.LASER_DIST_LIMIT
    if hand_present:
        span = max(1, config.LASER_DIST_LIMIT - config.LASER_MIN_VALID_MM)
        proximity = 1.0 - ((dist - config.LASER_MIN_VALID_MM) / span)
        g = int(120 + 135 * proximity)
        b = int(40 + 120 * proximity)
        strip_dome.fill((0, g, b))
        strip_jaw.fill((0, int(g * 0.65), int(b * 0.8)) if is_open else (0, 0, 0))
        strip_dome.show()
        strip_jaw.show()
        return

    if anim_mode == 1:
        strip_dome.fill((0, 85, 255))
        _jaw_idle_fill(is_open)
    elif anim_mode == 2:
        pulse = int((math.sin(now * 3.2) + 1.0) * 0.5 * 170) + 12
        strip_dome.fill((0, int(pulse * 0.45), pulse))
        strip_jaw.fill((0, int(pulse * 0.18), int(pulse * 0.32)) if is_open else (0, 0, 0))
    elif anim_mode == 3:
        _set_scanner(strip_dome, now, 5.0, (255, 0, 0), (55, 0, 0))
        strip_jaw.fill((30, 0, 0) if is_open else (0, 0, 0))
    elif anim_mode == 4:
        for i in range(config.NUM_LEDS_DOME):
            idx = int((i * 256 / config.NUM_LEDS_DOME) + now * 50) & 255
            strip_dome[i] = wheel(idx)
        if is_open:
            for i in range(config.NUM_LEDS_JAW):
                idx = int((i * 256 / config.NUM_LEDS_JAW) + now * 80) & 255
                strip_jaw[i] = wheel(idx)
        else:
            strip_jaw.fill((0, 0, 0))
    elif anim_mode == 5:
        if int(now * 10) % 2 == 0:
            strip_dome.fill((255, 255, 255))
            strip_jaw.fill((80, 80, 80) if is_open else (0, 0, 0))
        else:
            strip_dome.fill((0, 0, 0))
            strip_jaw.fill((0, 0, 0))
    elif anim_mode == 6:
        strip_dome.fill((0, 0, 20))
        if random.random() < 0.1:
            strip_dome[random.randint(0, config.NUM_LEDS_DOME - 1)] = (255, 255, 255)
        _jaw_idle_fill(is_open)
    elif anim_mode == 7:
        phase = int(now) % 3
        col = (255, 0, 0) if phase == 0 else ((255, 100, 0) if phase == 1 else (0, 255, 0))
        strip_dome.fill(col)
        strip_jaw.fill((col[0] // 6, col[1] // 6, col[2] // 6) if is_open else (0, 0, 0))
    elif anim_mode == 8:
        if int(now * 4) % 2 == 0:
            strip_dome.fill((255, 0, 0))
            strip_jaw.fill((60, 0, 0) if is_open else (0, 0, 0))
        else:
            strip_dome.fill((0, 0, 255))
            strip_jaw.fill((0, 0, 60) if is_open else (0, 0, 0))
    elif anim_mode == 9:
        strip_dome.fill((0, 0, 0))
        for i in range(config.NUM_LEDS_DOME):
            if random.random() < 0.2:
                strip_dome[i] = (0, 255, 0)
        strip_jaw.fill((0, 20, 0) if is_open else (0, 0, 0))
    elif anim_mode == 10:
        x = now * 3
        bright = max(0, math.sin(x) * math.sin(x * 3) * 255)
        strip_dome.fill((int(bright), 0, 0))
        strip_jaw.fill((int(bright * 0.2), 0, 0) if is_open else (0, 0, 0))
    else:
        strip_dome.fill((0, 90, 200))
        _jaw_idle_fill(is_open)

    strip_dome.show()
    strip_jaw.show()
