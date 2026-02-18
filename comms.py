import supervisor
import sys
import json
import config

# ==============================================================================
# MODUŁ KOMUNIKACJI USB (J.A.R.V.I.S. LINK)
# ==============================================================================

# Flaga: Czy jesteśmy w trybie strojenia?
# Jeśli True, maska ignoruje czujniki i słucha tylko suwaków z komputera.
tuning_mode = False

def check_usb_commands(servos_module, audio_module, eyes_module):
    """
    Sprawdza, czy przyszły dane z dashboardu HTML.
    Zwraca: True jeśli przyszła komenda, False jeśli cisza.
    """
    global tuning_mode

    # Sprawdzamy, czy w buforze USB są jakieś dane
    if supervisor.runtime.serial_bytes_available:
        try:
            # Czytamy linię tekstu (JSON)
            line = sys.stdin.readline()
            if not line: return False
            
            # Parsujemy JSON
            data = json.loads(line.strip())
            
            if "cmd" in data:
                cmd = data["cmd"]

                # 1. Komenda: Połączono z Dashboardem
                if cmd == "connect":
                    tuning_mode = True
                    print(">>> TRYB STROJENIA AKTYWNY (Czujniki wstrzymane)")
                    audio_module.play(config.SND_STARTUP)
                    return True

                # 2. Komenda: Zmiana ustawień (Suwaki)
                if cmd == "set_config":
                    key = data.get("key")
                    val = data.get("value")
                    
                    # Aktualizujemy zmienną w configu (tylko w pamięci RAM!)
                    if hasattr(config, key):
                        # Konwersja typów (int/float)
                        current_val = getattr(config, key)
                        if isinstance(current_val, int) and not isinstance(current_val, bool):
                            setattr(config, key, int(val))
                        elif isinstance(current_val, float):
                            setattr(config, key, float(val))
                        else:
                            setattr(config, key, str(val)) # Dla napisów (pliki dźwiękowe) i bool
                    
                    # Wymuszamy tryb strojenia przy każdej zmianie
                    tuning_mode = True 
                    return True

                # 3. Komenda: Testuj Dźwięk
                if cmd == "play_sound":
                    filename = data.get("file")
                    audio_module.play(filename)
                    return True

        except Exception as e:
            print(f"Błąd USB: {e}")
            
    return False