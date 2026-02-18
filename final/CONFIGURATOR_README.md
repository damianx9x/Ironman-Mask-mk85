# Konfigurator USB (Web Serial)

Plik: `configurator_usb.html`

Pelna dokumentacja projektu:

- `OPERATIONS_MASTER.md`

Narzędzie hosta:

- `tool_final_build.py` (`preflight`, `serve-ui`, `build`)

## Jak uruchomić

1. Wejdź do folderu `final`.
2. Uruchom lokalny serwer:
   `python3 tool_final_build.py serve-ui --port 8000`
3. Otwórz w Chrome/Edge:
   `http://localhost:8000/configurator_usb.html`
4. Podłącz płytkę USB i kliknij `Połącz USB`.
5. Kliknij `Pobierz z płytki`, zmieniaj parametry i `Wyślij wszystko`.

## Co działa

- live zmiana wartości `config` przez USB (`set_config`)
- odczyt aktualnych wartości z płytki (`get_config`)
- wymuszenie `tuning_mode` ON/OFF
- test dźwięku startup
- uruchamianie długiego demo-sequence (`trigger_demo`)
- popupy z opisem wpływu każdego parametru
- parowanie serw (domyślnie ON): `S1_OPEN <-> S2_CLOSE` i `S1_CLOSE <-> S2_OPEN` wg `SERVO_PAIR_SUM`
- po ponownym włączeniu parowania wartości prawego serwa synchronizują się od razu
- panel HUD JARVIS pod sekcją logów (`assets/jarvis_hud.svg`)
- w trybie parowania suwak prawego serwa jest lustrzanie odwrócony wizualnie, żeby oba suwaki "szły razem" przy asymetrii HIGH<->LOW

## Uwaga

Zmiany wysyłane przez USB są w RAM (działają do restartu).  
Jeśli chcesz je na stałe, przepisz finalne wartości do `config.py`.

Aktualne domyslne ustawienia bezpieczne:

- `START_OPEN = False`
- `JAW_SENSE_ENABLED = False`
- `BUTTON_USE_KEYPAD_EVENTS = False`
- profil serw: szybsze podnoszenie (`SERVO_OPEN_SPEED_MULT`, `SERVO_OPEN_FAST_EASE`) przy zachowaniu release po zamknieciu
