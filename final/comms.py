import supervisor
import sys
import json
import config


tuning_mode = False
demo_triggered = False


def consume_demo_trigger():
    global demo_triggered
    val = demo_triggered
    demo_triggered = False
    return val


def check_usb_commands(servos_module, audio_module, eyes_module):
    global tuning_mode, demo_triggered

    if not supervisor.runtime.serial_bytes_available:
        return False

    try:
        line = sys.stdin.readline()
        if not line:
            return False

        data = json.loads(line.strip())
        cmd = data.get("cmd")

        if cmd == "connect":
            tuning_mode = True
            print(">>> TRYB STROJENIA AKTYWNY")
            audio_module.play(config.SND_STARTUP)
            print(json.dumps({"type": "ack", "cmd": "connect", "tuning_mode": tuning_mode}))
            return True

        if cmd == "set_config":
            key = data.get("key")
            val = data.get("value")

            key_aliases = {"SERVO_SPEED_DELAY": "SERVO_UPDATE_DELAY"}
            key = key_aliases.get(key, key)

            if hasattr(config, key):
                current_val = getattr(config, key)
                if isinstance(current_val, int) and not isinstance(current_val, bool):
                    setattr(config, key, int(val))
                elif isinstance(current_val, float):
                    setattr(config, key, float(val))
                elif isinstance(current_val, bool):
                    if isinstance(val, str):
                        setattr(config, key, val.strip().lower() in ("1", "true", "yes", "on"))
                    else:
                        setattr(config, key, bool(val))
                else:
                    setattr(config, key, str(val))

            if hasattr(config, key):
                print(
                    json.dumps(
                        {
                            "type": "ack",
                            "cmd": "set_config",
                            "key": key,
                            "value": getattr(config, key),
                        }
                    )
                )
            return True

        if cmd == "get_config":
            keys = data.get("keys")
            if not isinstance(keys, list) or not keys:
                keys = []
                for name in dir(config):
                    if name.isupper():
                        keys.append(name)
            out = {}
            for key in keys:
                if hasattr(config, key):
                    val = getattr(config, key)
                    try:
                        json.dumps(val)
                        out[key] = val
                    except Exception:
                        out[key] = str(val)
            print(json.dumps({"type": "config", "data": out}))
            return True

        if cmd == "play_sound":
            filename = data.get("file")
            audio_module.play(filename)
            print(json.dumps({"type": "ack", "cmd": "play_sound", "file": filename}))
            return True

        if cmd == "trigger_demo":
            demo_triggered = True
            print(json.dumps({"type": "ack", "cmd": "trigger_demo", "queued": True}))
            return True

        if cmd == "set_tuning_mode":
            tuning_mode = bool(data.get("value"))
            print(json.dumps({"type": "ack", "cmd": "set_tuning_mode", "tuning_mode": tuning_mode}))
            return True

    except Exception as e:
        print(f"Blad USB: {e}")

    return False
