import random
import time
import math
import digitalio

try:
    import keypad
except Exception:
    keypad = None

import config


CONFIG_DEFAULTS = {
    "PIN_POWER": None,
    "PIN_BUTTON": None,
    "PIN_JAW_SENSE": None,
    "PIN_SERVO_LEFT": None,
    "PIN_SERVO_RIGHT": None,
    "PIN_EYES": None,
    "PIN_LED_DOME": None,
    "PIN_LED_JAW": None,
    "PIN_LASER_SDA": None,
    "PIN_LASER_SCL": None,
    "S1_OPEN": 160,
    "S1_CLOSE": 20,
    "S2_OPEN": 20,
    "S2_CLOSE": 160,
    "OPEN_REDUCTION_DEG": 2,
    "SERVO_MAX_SPEED_DPS": 78.0,
    "SERVO_OPEN_SPEED_MULT": 1.35,
    "SERVO_CLOSE_SPEED_MULT": 1.0,
    "SERVO_OPEN_FAST_EASE": True,
    "SERVO_UPDATE_DELAY": 0.012,
    "SERVO_SETTLE_TIME": 0.12,
    "SERVO_RELEASE_AFTER_CLOSE": True,
    "SERVO_RELEASE_DELAY": 0.20,
    "SERVO_MIN_ANGLE": 0,
    "SERVO_MAX_ANGLE": 180,
    "SERVO_MIN_PULSE": 750,
    "SERVO_MAX_PULSE": 2250,
    "LASER_DIST_LIMIT": 250,
    "LASER_MIN_VALID_MM": 40,
    "LASER_DEBOUNCE": 3,
    "LASER_HOLD_TIME": 0.35,
    "LASER_FILTER_ALPHA": 0.4,
    "LASER_TIMING_BUDGET_US": 50000,
    "ANIMATION_MODE": 1,
    "AUTO_CLOSE_DELAY": 5.0,
    "EYE_MAX_BRIGHT": 1.0,
    "LED_UPDATE_DELAY": 0.03,
    "NUM_LEDS_DOME": 15,
    "NUM_LEDS_JAW": 8,
    "BUTTON_DEBOUNCE": 0.06,
    "BUTTON_COOLDOWN": 2.0,
    "MULTI_CLICK_WINDOW": 0.55,
    "SINGLE_CLICK_DECISION_DELAY": 0.30,
    "TRIPLE_CLICK_COUNT": 3,
    "DEMO_FX_DURATION": 4.0,
    "BUTTON_USE_KEYPAD_EVENTS": False,
    "START_OPEN": False,
    "JAW_SENSE_ENABLED": False,
    "JAW_DETACH_ACTIVE_LEVEL": False,
    "JAW_DETACH_DEBOUNCE": 0.60,
    "RUNTIME_DIAG_ENABLED": True,
    "RUNTIME_DIAG_INTERVAL": 2.0,
    "SHOW_OFF_ENABLED": False,
    "SHOW_OFF_INTERVAL": 10.0,
    "SND_STARTUP": "startup.wav",
    "SND_OPEN": "open.wav",
    "SND_CLOSE": "close.wav",
    "DEMO_SEQUENCE_ENABLED": True,
    "DEMO_STAGE_IGNITION": 1.8,
    "DEMO_STAGE_OPEN_HOLD": 2.8,
    "DEMO_STAGE_CLOSE_HOLD": 2.2,
    "DEMO_STAGE_ARC": 2.4,
    "DEMO_STAGE_FINAL_HOLD": 2.6,
    "DEMO_EYE_PULSE_MIN": 0.08,
}

for _k, _v in CONFIG_DEFAULTS.items():
    if not hasattr(config, _k):
        setattr(config, _k, _v)
        print("CONFIG DEFAULT:", _k, "=", _v)

print("\n>>> URUCHAMIANIE SYSTEMU MARK 85...")
try:
    power = digitalio.DigitalInOut(config.PIN_POWER)
    power.direction = digitalio.Direction.OUTPUT
    power.value = True
except Exception as e:
    power = None
    print("BLAD POWER PIN:", e)
time.sleep(0.6)

import audio_sys
import comms
import eyes
import laser
import leds
import logic_core
import servos
import ubieranie


def get_targets_from_config():
    open_s1 = logic_core.clamp_angle(
        logic_core.trimmed_open_angle(config.S1_OPEN, config.S1_CLOSE, config.OPEN_REDUCTION_DEG),
        config.SERVO_MIN_ANGLE,
        config.SERVO_MAX_ANGLE,
    )
    open_s2 = logic_core.clamp_angle(
        logic_core.trimmed_open_angle(config.S2_OPEN, config.S2_CLOSE, config.OPEN_REDUCTION_DEG),
        config.SERVO_MIN_ANGLE,
        config.SERVO_MAX_ANGLE,
    )
    close_s1 = logic_core.clamp_angle(config.S1_CLOSE, config.SERVO_MIN_ANGLE, config.SERVO_MAX_ANGLE)
    close_s2 = logic_core.clamp_angle(config.S2_CLOSE, config.SERVO_MIN_ANGLE, config.SERVO_MAX_ANGLE)
    return (open_s1, open_s2), (close_s1, close_s2)

btn = None
btn_prev_state = True
button_keys = None
if config.BUTTON_USE_KEYPAD_EVENTS and keypad:
    try:
        button_keys = keypad.Keys((config.PIN_BUTTON,), value_when_pressed=False, pull=True)
        print(">>> BUTTON: keypad event queue")
    except Exception:
        button_keys = None

if not button_keys:
    try:
        btn = digitalio.DigitalInOut(config.PIN_BUTTON)
        btn.direction = digitalio.Direction.INPUT
        btn.pull = digitalio.Pull.UP
        btn_prev_state = btn.value
        print(">>> BUTTON: fallback digitalio")
    except Exception as e:
        btn = None
        btn_prev_state = True
        print("BLAD BUTTON fallback:", e)

class _DummyJawMonitor:
    @property
    def raw_detached(self):
        return False

    @property
    def is_detached(self):
        return False


try:
    jaw_mon = ubieranie.JawMonitor(
        pin_id=config.PIN_JAW_SENSE,
        enabled=config.JAW_SENSE_ENABLED,
        active_level=config.JAW_DETACH_ACTIVE_LEVEL,
        debounce_s=config.JAW_DETACH_DEBOUNCE,
    )
except Exception as e:
    print("BLAD JAW MONITOR:", e)
    jaw_mon = _DummyJawMonitor()

(open_target_s1, open_target_s2), (close_target_s1, close_target_s2) = get_targets_from_config()

if config.START_OPEN:
    current_s1 = float(open_target_s1)
    current_s2 = float(open_target_s2)
    initial_open = True
else:
    current_s1 = float(close_target_s1)
    current_s2 = float(close_target_s2)
    initial_open = False

servos.set_pair(current_s1, current_s2)

state = {
    "current_s1": current_s1,
    "current_s2": current_s2,
    "is_open": initial_open,
    "manual_open": initial_open,
    "motion_active": False,
    "motion_start": 0.0,
    "motion_duration": 0.0,
    "motion_from_s1": current_s1,
    "motion_from_s2": current_s2,
    "motion_to_s1": current_s1,
    "motion_to_s2": current_s2,
    "motion_is_opening": initial_open,
    "last_servo_update": 0.0,
    "servo_release_at": 0.0,
    "last_presence_time": time.monotonic(),
    "button_locked_until": 0.0,
    "demo_fx_until": 0.0,
    "last_showoff_time": 0.0,
    "demo_sequence_active": False,
    "demo_stage": 0,
    "demo_stage_started": 0.0,
    "demo_motion_queued": False,
    "demo_eye_override": None,
}

laser_detection_stack = 0
laser_hold_start = 0.0
last_laser_time = 0.0
current_dist = 9999
filtered_dist = None

last_button_edge = 0.0
click_count = 0
last_click_time = 0.0
pending_single_click_at = 0.0

last_led_time = 0.0
last_diag_time = 0.0


audio_sys.play(config.SND_STARTUP)


def schedule_motion(target_s1, target_s2, result_is_open, now):
    target_s1 = float(logic_core.clamp_angle(target_s1, config.SERVO_MIN_ANGLE, config.SERVO_MAX_ANGLE))
    target_s2 = float(logic_core.clamp_angle(target_s2, config.SERVO_MIN_ANGLE, config.SERVO_MAX_ANGLE))

    if (
        state["motion_active"]
        and abs(state["motion_to_s1"] - target_s1) < 0.2
        and abs(state["motion_to_s2"] - target_s2) < 0.2
    ):
        state["is_open"] = result_is_open
        return

    if (
        (not state["motion_active"])
        and abs(state["current_s1"] - target_s1) < 0.2
        and abs(state["current_s2"] - target_s2) < 0.2
    ):
        state["is_open"] = result_is_open
        return

    if servos.is_released():
        servos.engage_at_last_position()

    state["motion_active"] = True
    state["motion_start"] = now
    state["motion_from_s1"] = state["current_s1"]
    state["motion_from_s2"] = state["current_s2"]
    state["motion_to_s1"] = target_s1
    state["motion_to_s2"] = target_s2
    state["motion_is_opening"] = bool(result_is_open)
    if result_is_open:
        speed_dps = float(config.SERVO_MAX_SPEED_DPS) * float(config.SERVO_OPEN_SPEED_MULT)
    else:
        speed_dps = float(config.SERVO_MAX_SPEED_DPS) * float(config.SERVO_CLOSE_SPEED_MULT)
    state["motion_duration"] = logic_core.calc_motion_duration(
        state["motion_from_s1"],
        state["motion_from_s2"],
        target_s1,
        target_s2,
        speed_dps,
        config.SERVO_UPDATE_DELAY,
    )
    state["is_open"] = result_is_open
    if result_is_open:
        state["button_locked_until"] = max(state["button_locked_until"], now + config.BUTTON_COOLDOWN)
    state["servo_release_at"] = 0.0


def set_demo_stage(stage, now):
    state["demo_stage"] = stage
    state["demo_stage_started"] = now
    state["demo_motion_queued"] = False


def start_demo_sequence(now):
    state["demo_sequence_active"] = True
    state["manual_open"] = False
    state["demo_eye_override"] = config.DEMO_EYE_PULSE_MIN
    set_demo_stage(0, now)
    print(">>> DEMO: START")


def stop_demo_sequence(reason):
    state["demo_sequence_active"] = False
    state["demo_stage"] = 0
    state["demo_motion_queued"] = False
    state["demo_eye_override"] = None
    print(f">>> DEMO: STOP ({reason})")


def update_demo_sequence(now, jaw_detached, tuning_mode, open_target_s1, open_target_s2, close_target_s1, close_target_s2):
    if not state["demo_sequence_active"]:
        return

    if jaw_detached:
        stop_demo_sequence("jaw_detached")
        return
    if tuning_mode:
        stop_demo_sequence("tuning_mode")
        return

    stage = state["demo_stage"]
    elapsed = now - state["demo_stage_started"]

    # Stage 0: ignition pulse (oczy + agresywniejsze LED)
    if stage == 0:
        pulse = (math.sin(now * 7.5) + 1.0) * 0.5
        state["demo_eye_override"] = config.DEMO_EYE_PULSE_MIN + (
            (config.EYE_MAX_BRIGHT - config.DEMO_EYE_PULSE_MIN) * pulse
        )
        config.ANIMATION_MODE = 3
        state["demo_fx_until"] = now + 0.3
        if elapsed >= config.DEMO_STAGE_IGNITION:
            set_demo_stage(1, now)
        return

    # Stage 1: otworz
    if stage == 1:
        state["demo_eye_override"] = config.EYE_MAX_BRIGHT * 0.95
        config.ANIMATION_MODE = 2
        if not state["demo_motion_queued"]:
            schedule_motion(open_target_s1, open_target_s2, True, now)
            state["demo_motion_queued"] = True
        if state["demo_motion_queued"] and (not state["motion_active"]) and state["is_open"]:
            set_demo_stage(2, now)
        return

    # Stage 2: hold open + show
    if stage == 2:
        state["demo_eye_override"] = config.EYE_MAX_BRIGHT * 0.85
        config.ANIMATION_MODE = 4
        state["demo_fx_until"] = now + 0.2
        if elapsed >= config.DEMO_STAGE_OPEN_HOLD:
            set_demo_stage(3, now)
        return

    # Stage 3: zamknij
    if stage == 3:
        state["demo_eye_override"] = config.EYE_MAX_BRIGHT
        config.ANIMATION_MODE = 8
        if not state["demo_motion_queued"]:
            schedule_motion(close_target_s1, close_target_s2, False, now)
            state["demo_motion_queued"] = True
        if state["demo_motion_queued"] and (not state["motion_active"]) and (not state["is_open"]):
            set_demo_stage(4, now)
        return

    # Stage 4: hold close
    if stage == 4:
        pulse = (math.sin(now * 5.2) + 1.0) * 0.5
        state["demo_eye_override"] = 0.35 + (0.65 * pulse * config.EYE_MAX_BRIGHT)
        config.ANIMATION_MODE = 10
        if elapsed >= config.DEMO_STAGE_CLOSE_HOLD:
            set_demo_stage(5, now)
        return

    # Stage 5: otworz ponownie
    if stage == 5:
        state["demo_eye_override"] = config.EYE_MAX_BRIGHT
        config.ANIMATION_MODE = 6
        if not state["demo_motion_queued"]:
            schedule_motion(open_target_s1, open_target_s2, True, now)
            state["demo_motion_queued"] = True
        if state["demo_motion_queued"] and (not state["motion_active"]) and state["is_open"]:
            set_demo_stage(6, now)
        return

    # Stage 6: arc-reactor burst
    if stage == 6:
        pulse = (math.sin(now * 11.0) + 1.0) * 0.5
        state["demo_eye_override"] = 0.25 + (0.75 * pulse * config.EYE_MAX_BRIGHT)
        config.ANIMATION_MODE = 4
        state["demo_fx_until"] = now + 0.3
        if elapsed >= config.DEMO_STAGE_ARC:
            set_demo_stage(7, now)
        return

    # Stage 7: final close
    if stage == 7:
        state["demo_eye_override"] = config.EYE_MAX_BRIGHT
        config.ANIMATION_MODE = 3
        if not state["demo_motion_queued"]:
            schedule_motion(close_target_s1, close_target_s2, False, now)
            state["demo_motion_queued"] = True
        if state["demo_motion_queued"] and (not state["motion_active"]) and (not state["is_open"]):
            set_demo_stage(8, now)
        return

    # Stage 8: final hold close + fade out
    if stage == 8:
        fade = max(0.0, 1.0 - (elapsed / max(0.1, config.DEMO_STAGE_FINAL_HOLD)))
        state["demo_eye_override"] = config.EYE_MAX_BRIGHT * fade
        config.ANIMATION_MODE = 2
        if elapsed >= config.DEMO_STAGE_FINAL_HOLD:
            state["demo_eye_override"] = None
            state["manual_open"] = False
            stop_demo_sequence("completed")
        return


while True:
    now = time.monotonic()

    (open_target_s1, open_target_s2), (close_target_s1, close_target_s2) = get_targets_from_config()

    comms.check_usb_commands(servos, audio_sys, eyes)

    jaw_detached = jaw_mon.is_detached
    if jaw_detached:
        if state["demo_sequence_active"]:
            stop_demo_sequence("jaw_detached")
        # jaw detach has priority for safety, but should not latch manual_open permanently
        state["manual_open"] = False
        laser_detection_stack = 0
        laser_hold_start = 0.0
        state["last_presence_time"] = now
        if (
            (not state["is_open"])
            or (
                state["motion_active"]
                and (
                    abs(state["motion_to_s1"] - open_target_s1) > 0.2
                    or abs(state["motion_to_s2"] - open_target_s2) > 0.2
                )
            )
        ):
            schedule_motion(open_target_s1, open_target_s2, True, now)

    if (
        config.DEMO_SEQUENCE_ENABLED
        and comms.consume_demo_trigger()
        and (not state["demo_sequence_active"])
        and (not jaw_detached)
        and (not comms.tuning_mode)
    ):
        start_demo_sequence(now)

    if comms.tuning_mode and not jaw_detached:
        if servos.is_released():
            servos.engage_at_last_position()
        desired_s1, desired_s2 = (
            (open_target_s1, open_target_s2) if state["is_open"] else (close_target_s1, close_target_s2)
        )
        if (
            abs(state["motion_to_s1"] - desired_s1) > 0.2
            or abs(state["motion_to_s2"] - desired_s2) > 0.2
            or (
                (not state["motion_active"])
                and (
                    abs(state["current_s1"] - desired_s1) > 0.2
                    or abs(state["current_s2"] - desired_s2) > 0.2
                )
            )
        ):
            schedule_motion(desired_s1, desired_s2, state["is_open"], now)

    if state["motion_active"] and (now - state["last_servo_update"] >= config.SERVO_UPDATE_DELAY):
        elapsed = now - state["motion_start"]
        progress = elapsed / state["motion_duration"] if state["motion_duration"] > 0 else 1.0

        if progress >= 1.0:
            state["current_s1"] = state["motion_to_s1"]
            state["current_s2"] = state["motion_to_s2"]
            servos.set_pair(state["current_s1"], state["current_s2"])
            state["motion_active"] = False
            state["last_servo_update"] = now
            if (not state["is_open"]) and config.SERVO_RELEASE_AFTER_CLOSE and (not comms.tuning_mode):
                state["servo_release_at"] = now + max(config.SERVO_SETTLE_TIME, config.SERVO_RELEASE_DELAY)
            else:
                state["servo_release_at"] = 0.0
        else:
            if state["motion_is_opening"] and config.SERVO_OPEN_FAST_EASE:
                eased = logic_core.ease_out_cubic(progress)
            else:
                eased = logic_core.ease_in_out(progress)
            state["current_s1"] = state["motion_from_s1"] + ((state["motion_to_s1"] - state["motion_from_s1"]) * eased)
            state["current_s2"] = state["motion_from_s2"] + ((state["motion_to_s2"] - state["motion_from_s2"]) * eased)
            servos.set_pair(state["current_s1"], state["current_s2"])
            state["last_servo_update"] = now

    if (
        (not state["motion_active"])
        and (not state["is_open"])
        and state["servo_release_at"] > 0.0
        and now >= state["servo_release_at"]
        and (not comms.tuning_mode)
        and (not servos.is_released())
    ):
        servos.release_all()
        state["servo_release_at"] = 0.0

    update_demo_sequence(
        now,
        jaw_detached,
        comms.tuning_mode,
        open_target_s1,
        open_target_s2,
        close_target_s1,
        close_target_s2,
    )

    press_event = False
    if button_keys:
        evt = button_keys.events.get()
        while evt:
            if evt.pressed:
                press_event = True
            evt = button_keys.events.get()
    else:
        if btn:
            btn_state = btn.value
            if (not btn_state) and btn_prev_state and (now - last_button_edge >= config.BUTTON_DEBOUNCE):
                press_event = True
            btn_prev_state = btn_state

    if press_event:
        if state["demo_sequence_active"]:
            click_count = 0
            pending_single_click_at = 0.0
        else:
            last_button_edge = now
            if (now - last_click_time) <= config.MULTI_CLICK_WINDOW:
                click_count += 1
            else:
                click_count = 1
            last_click_time = now
            pending_single_click_at = now + config.SINGLE_CLICK_DECISION_DELAY

            if click_count >= config.TRIPLE_CLICK_COUNT:
                if config.DEMO_SEQUENCE_ENABLED and (not jaw_detached) and (not comms.tuning_mode):
                    start_demo_sequence(now)
                else:
                    state["demo_fx_until"] = now + config.DEMO_FX_DURATION
                    config.ANIMATION_MODE = random.randint(1, 10)
                click_count = 0
                pending_single_click_at = 0.0

    if pending_single_click_at > 0.0 and now >= pending_single_click_at:
        if (
            click_count == 1
            and (not jaw_detached)
            and (not comms.tuning_mode)
            and (not state["motion_active"])
            and (not state["demo_sequence_active"])
        ):
            if now >= state["button_locked_until"]:
                if state["is_open"]:
                    state["manual_open"] = False
                    schedule_motion(close_target_s1, close_target_s2, False, now)
                else:
                    state["manual_open"] = True
                    schedule_motion(open_target_s1, open_target_s2, True, now)
        click_count = 0
        pending_single_click_at = 0.0

    if (
        config.SHOW_OFF_ENABLED
        and (not jaw_detached)
        and (not comms.tuning_mode)
        and (not state["motion_active"])
        and (not state["demo_sequence_active"])
        and (now - state["last_showoff_time"]) > config.SHOW_OFF_INTERVAL
    ):
        action = random.randint(0, 2)
        if action == 0:
            if state["is_open"]:
                state["manual_open"] = False
                schedule_motion(close_target_s1, close_target_s2, False, now)
            else:
                state["manual_open"] = True
                schedule_motion(open_target_s1, open_target_s2, True, now)
        elif action == 1:
            config.ANIMATION_MODE = random.randint(1, 10)
        else:
            state["demo_fx_until"] = now + config.DEMO_FX_DURATION
        state["last_showoff_time"] = now

    if (
        (not jaw_detached)
        and (not comms.tuning_mode)
        and (not state["motion_active"])
        and (not state["demo_sequence_active"])
        and (now - last_laser_time) >= 0.05
    ):
        d = laser.get_distance()
        if d < 8000:
            filtered_dist = logic_core.ewma_filter(filtered_dist, d, config.LASER_FILTER_ALPHA)
            current_dist = int(filtered_dist)
        else:
            current_dist = d

        hand_present = logic_core.is_hand_present(d, config.LASER_MIN_VALID_MM, config.LASER_DIST_LIMIT)

        if hand_present:
            laser_detection_stack += 1
            state["last_presence_time"] = now
        else:
            laser_detection_stack = 0

        if laser_detection_stack >= config.LASER_DEBOUNCE:
            if not state["is_open"]:
                if laser_hold_start == 0.0:
                    laser_hold_start = now
                elif (now - laser_hold_start) >= config.LASER_HOLD_TIME:
                    state["manual_open"] = False
                    schedule_motion(open_target_s1, open_target_s2, True, now)
                    laser_hold_start = 0.0
            else:
                laser_hold_start = 0.0
        else:
            laser_hold_start = 0.0
            if state["is_open"] and (not state["manual_open"]):
                if (now - state["last_presence_time"]) >= config.AUTO_CLOSE_DELAY:
                    schedule_motion(close_target_s1, close_target_s2, False, now)

        last_laser_time = now

    if (now - last_led_time) >= config.LED_UPDATE_DELAY:
        leds.update(
            now,
            state["motion_active"],
            state["is_open"],
            jaw_detached,
            current_dist,
            config.ANIMATION_MODE,
            demo_active=(now < state["demo_fx_until"]),
        )
        last_led_time = now

    if state["demo_eye_override"] is not None:
        val = state["demo_eye_override"]
        if val < 0.0:
            val = 0.0
        if val > config.EYE_MAX_BRIGHT:
            val = config.EYE_MAX_BRIGHT
        eyes.set_brightness(val)
    elif (not state["is_open"]) and (not state["motion_active"]) and (not jaw_detached):
        eyes.set_brightness(config.EYE_MAX_BRIGHT)
    else:
        eyes.set_brightness(0.0)

    if config.RUNTIME_DIAG_ENABLED and (now - last_diag_time) >= config.RUNTIME_DIAG_INTERVAL:
        hand = logic_core.is_hand_present(current_dist, config.LASER_MIN_VALID_MM, config.LASER_DIST_LIMIT)
        jaw_raw = False
        try:
            jaw_raw = jaw_mon.raw_detached
        except Exception:
            jaw_raw = False
        print(
            "[RUNTIME] "
            f"open={state['is_open']} moving={state['motion_active']} released={servos.is_released()} "
            f"jaw_detached={jaw_detached} jaw_raw={jaw_raw} dist={current_dist} hand={hand} "
            f"manual_open={state['manual_open']} tuning={comms.tuning_mode} "
            f"demo={state['demo_sequence_active']} stage={state['demo_stage']}"
        )
        last_diag_time = now

    time.sleep(0.001)
