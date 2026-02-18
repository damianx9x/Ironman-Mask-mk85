# IRON MAN MASK - OPERATIONS MASTER (FINAL)

## 1. Cel dokumentu

Ten dokument jest jedna, kompletna instrukcja dla projektu maski.
Ma zamknac temat "co, gdzie i jak dziala", zeby przy kolejnych zmianach nie tlumaczyc wszystkiego od zera.

Glowne priorytety systemu:

1. Ruch maski (otwieranie/zamykanie) ma najwyzszy priorytet.
2. Ochrona serw przed przeciaganiem i przegrzewaniem.
3. Stabilna praca na realnym sprzecie (laser, LED, oczy, audio, przycisk, czujnik szczeki).
4. Wygodna diagnostyka i strojenie przez USB.

Domyslna filozofia startu:

- start zamkniety (`START_OPEN=False`)
- szczeka-sense domyslnie OFF (`JAW_SENSE_ENABLED=False`)
- przycisk domyslnie przez `digitalio` (`BUTTON_USE_KEYPAD_EVENTS=False`)

---

## 2. Co jest "final build"

Final build to zawartosc folderu `final/`:

- firmware CircuitPython:
  - `code.py`
  - `config.py`
  - `comms.py`
  - `logic_core.py`
  - `servos.py`
  - `laser.py`
  - `leds.py`
  - `eyes.py`
  - `audio_sys.py`
  - `ubieranie.py`
- konfigurator USB:
  - `configurator_usb.html`
  - `assets/jarvis_hud.svg`
  - `CONFIGURATOR_README.md`
- narzedzia hosta:
  - `tool_final_build.py`
- dokumentacja:
  - `OPERATIONS_MASTER.md` (ten plik)

---

## 3. Tooling hosta (NOWE)

Plik: `tool_final_build.py`

To jedno narzedzie obsluguje trzy rzeczy:

1. `preflight` - sprawdza czy pliki sa kompletne i czy Python ma poprawna skladnie.
2. `serve-ui` - odpala lokalny HTTP server dla `configurator_usb.html`.
3. `build` - tworzy ZIP finalnej paczki w `final/build/`.

### 3.1 Szybkie komendy

Z folderu `final/`:

```bash
python3 tool_final_build.py preflight
python3 tool_final_build.py serve-ui --port 8000
python3 tool_final_build.py build --preflight
```

### 3.2 Wynik komendy build

Po `build` dostajesz:

- `final/build/maska_final_build_<timestamp>.zip`
- `final/build/manifest_<timestamp>.json`
- `final/build/latest_manifest.json`

Uwaga:
Paczka nie zawiera katalogu `/sounds` z dysku `CIRCUITPY`. Dzwieki wrzucasz recznie na plytke.

---

## 4. Architektura runtime (jak to dziala)

Plik glowny: `code.py`

Petla `while True` wykonuje stale:

1. Odczyt komend USB (`comms.check_usb_commands`).
2. Odczyt stanu szczeki (`ubieranie.JawMonitor` na `PIN_JAW_SENSE = D10`).
3. Sterowanie serwami (harmonogram ruchu + easing + ograniczenie predkosci).
4. Obsluge przycisku (single click / multi click / triple click demo).
5. Obsluge lasera (auto-open przy obiekcie, auto-close po timeout).
6. Aktualizacje LED.
7. Ustawianie jasnosci oczu.
8. Diag runtime po serialu (opcjonalnie).

### 4.1 Priorytety logiki

Najwazniejsze warunki, od najwazniejszych:

1. `jaw_detached`:
   - maska otwierana (lub utrzymywana otwarta),
   - demo zatrzymane,
   - auto laser resetowane.
2. `tuning_mode`:
   - ruch serw podporzadkowany aktualnym wartosciom config,
   - brak automatycznego release po close (dla strojenia).
3. `demo_sequence_active`:
   - blokuje normalny toggle przyciskiem i auto laser,
   - steruje oczami i LED na potrzeby sekwencji.
4. Normalny tryb pracy:
   - przycisk, laser, auto-close, LED/eyes.

---

## 5. Pinout (aktualny)

Z `config.py`:

- `PIN_POWER = EXTERNAL_POWER`
- `PIN_BUTTON = EXTERNAL_BUTTON`
- `PIN_JAW_SENSE = D10`  (wykrywanie szczeki)
- `PIN_SERVO_LEFT = D11`
- `PIN_SERVO_RIGHT = D12`
- `PIN_EYES = D5`
- `PIN_LED_DOME = TX`
- `PIN_LED_JAW = RX`
- `PIN_LASER_SDA = SDA`
- `PIN_LASER_SCL = SCL`

Uwagi:

- Dla CircuitPython 10 na Feather RP2040 Prop-Maker aliasy `GPIO23/GPIO19` nie sa dostepne.
- Dlatego uzywamy aliasow zgodnych z board map: `EXTERNAL_POWER` i `EXTERNAL_BUTTON`.
- Domyslnie `JAW_SENSE_ENABLED=False` (zeby niestabilny sygnal D10 nie blokowal pracy). Wlacz po potwierdzeniu poprawnego wiringu.

---

## 6. Serwa - bezpieczenstwo i precyzja

### 6.1 Co chroni serwa

1. Predkosc ograniczona:
   - `SERVO_MAX_SPEED_DPS`
   - `SERVO_OPEN_SPEED_MULT`
   - `SERVO_CLOSE_SPEED_MULT`
2. Ruch po czasie + easing:
   - `logic_core.calc_motion_duration`
   - `logic_core.ease_in_out`
   - `logic_core.ease_out_cubic` (dla szybszego startu otwierania)
3. Ograniczenie nadmiernego otwarcia:
   - `OPEN_REDUCTION_DEG` (obecnie 2 stopnie)
4. Odpuszczenie serw po zamknieciu:
   - `SERVO_RELEASE_AFTER_CLOSE = True`
   - `SERVO_RELEASE_DELAY`
   - `SERVO_SETTLE_TIME`

### 6.2 Dlaczego to jest krytyczne

Bez tych ograniczen serwo:

- bierze skokowo duzy prad,
- grzeje sie przy docisku na koncu zakresu,
- szybciej zuzywa przekladnie,
- moze wprowadzac drgania i niestabilnosc napiecia.

### 6.3 Asymetryczne serwa (odwrocony montaz)

W konfiguratorze obowiazuje parowanie:

- `S1_OPEN <-> S2_CLOSE`
- `S1_CLOSE <-> S2_OPEN`

Zaleznosc:

`wartosc_drugiego = SERVO_PAIR_SUM - wartosc_pierwszego`

Przyklad 1 (klasyczne lustrzane):

- `SERVO_PAIR_SUM = 180`
- jesli `S1_OPEN = 160`, to `S2_CLOSE = 20`

Przyklad 2 (mechanika 0/90):

- `SERVO_PAIR_SUM = 90`
- jesli jedno ma `0`, drugie ma `90`

W konfiguratorze prawy suwak jest lustrzanie odwrocony wizualnie, zeby oba suwaki "szly razem", mimo logiki HIGH<->LOW.

---

## 7. Laser (VL53L0X) - auto-open i auto-close

### 7.1 Reguly

1. Pomiar co okolo 50 ms.
1.5. Jesli init czujnika nie powiedzie sie na starcie, firmware ponawia inicjalizacje automatycznie podczas pracy.
2. Sygnał filtrowany EWMA (`LASER_FILTER_ALPHA`).
3. Obiekt uznany za poprawny gdy:
   - `distance >= LASER_MIN_VALID_MM`
   - `distance <= LASER_DIST_LIMIT`
4. Potrzebna jest stabilizacja:
   - `LASER_DEBOUNCE` kolejnych trafien
   - `LASER_HOLD_TIME` czasu obecnosci
5. Po braku obiektu:
   - jesli otwarcie bylo automatyczne (`manual_open=False`), maska zamyka sie po `AUTO_CLOSE_DELAY`.

### 7.2 Wymaganie 25 cm

Aktualnie:

- `LASER_DIST_LIMIT = 250` mm (25 cm)

---

## 8. Przycisk i cooldown

Przycisk obslugiwany przez:

- `keypad.Keys(...)` (gdy dziala),
- fallback `digitalio` (gdy keypad niedostepny).

### 8.1 Logika klikniec

1. Single click:
   - po opoznieniu `SINGLE_CLICK_DECISION_DELAY`
   - toggle open/close
2. Multi-click:
   - okno `MULTI_CLICK_WINDOW`
3. Triple click:
   - liczba klikniec `TRIPLE_CLICK_COUNT` (aktualnie 3)
   - uruchamia demo sequence

### 8.2 Cooldown 2s

Po otwarciu ustawiany jest lock:

- `button_locked_until = now + BUTTON_COOLDOWN`
- aktualnie `BUTTON_COOLDOWN = 2.0`

W tym czasie normalny toggle przyciskiem nie dziala.
Triple click (demo) jest obslugiwany osobno.

---

## 9. Demo mode (dluga sekwencja)

Wlaczony przez:

- 3 szybkie klikniecia,
- USB command: `{"cmd":"trigger_demo"}`.

Etapy (konfigurowalne):

1. Ignition (`DEMO_STAGE_IGNITION`)
2. Open motion
3. Open hold (`DEMO_STAGE_OPEN_HOLD`)
4. Close motion
5. Close hold (`DEMO_STAGE_CLOSE_HOLD`)
6. Re-open motion
7. Arc burst (`DEMO_STAGE_ARC`)
8. Final close
9. Final hold + fade (`DEMO_STAGE_FINAL_HOLD`)

Oczy:

- puls i nadpisanie jasnosci przez `demo_eye_override`,
- dolny prog pulsu: `DEMO_EYE_PULSE_MIN`.

LED:

- w trakcie demo wymuszane sa konkretne `ANIMATION_MODE`,
- dodatkowy efekt przez `demo_fx_until`.

---

## 10. Audio

Audio jest gotowe do testu przez I2S:

- startup: `SND_STARTUP` i `audio_sys.play("startup.wav")`.

Wazne:

- Dzwieki otwierania/zamykania nie sa obecnie odpalane z logiki ruchu.
- To bylo intencjonalne (priorytet niezawodnosci ruchu).

---

## 11. LED i oczy

### 11.1 Oczy

- `eyes.set_brightness(0..1)` na `PIN_EYES`.
- Gdy maska zamknieta i nieruchoma: `EYE_MAX_BRIGHT`.
- Gdy otwarta lub w ruchu: oczy wygaszane, chyba ze demo nadpisuje.

### 11.2 LED

`leds.update(...)` obsluguje:

1. jaw detached: puls bialy
2. demo active: efekt rainbow + burst
3. moving: skaner ruchu
4. hand present: kolor zalezny od dystansu
5. idle: tryby `ANIMATION_MODE` 1..10

---

## 12. USB protocol (konfigurator i automaty)

### 12.1 Obslugiwane komendy JSON (stdin serial)

1. `{"cmd":"connect"}`
2. `{"cmd":"set_config","key":"...","value":...}`
3. `{"cmd":"get_config","keys":["KEY1","KEY2"]}`
4. `{"cmd":"play_sound","file":"startup.wav"}`
5. `{"cmd":"trigger_demo"}`
6. `{"cmd":"set_tuning_mode","value":true|false}`

### 12.2 Odpowiedzi

System zwraca `ack` i/lub `config` jako JSON:

- `{"type":"ack", ...}`
- `{"type":"config","data":{...}}`

### 12.3 Tuning mode

`connect` automatycznie wlacza `tuning_mode=True`.

Skutki:

- dynamiczna zmiana config dziala od razu w RAM,
- serwa sa utrzymywane aktywnie (bez release po close),
- demo zatrzymuje sie jesli tuning mode zostanie wlaczony.

---

## 13. Parametry config.py - pelna referencja

### 13.1 SERVO

- `S1_OPEN`, `S1_CLOSE`, `S2_OPEN`, `S2_CLOSE`
- `OPEN_REDUCTION_DEG`
- `SERVO_MAX_SPEED_DPS`
- `SERVO_OPEN_SPEED_MULT`
- `SERVO_CLOSE_SPEED_MULT`
- `SERVO_OPEN_FAST_EASE`
- `SERVO_UPDATE_DELAY`
- `SERVO_SETTLE_TIME`
- `SERVO_RELEASE_AFTER_CLOSE`
- `SERVO_RELEASE_DELAY`
- `SERVO_MIN_ANGLE`, `SERVO_MAX_ANGLE`
- `SERVO_MIN_PULSE`, `SERVO_MAX_PULSE`
- `SERVO_PAIR_SUM` (uzywane przez konfigurator)

### 13.2 LASER

- `LASER_DIST_LIMIT`
- `LASER_MIN_VALID_MM`
- `LASER_DEBOUNCE`
- `LASER_HOLD_TIME`
- `LASER_FILTER_ALPHA`
- `LASER_TIMING_BUDGET_US`

### 13.3 GLOBAL / LED / EYES

- `ANIMATION_MODE`
- `AUTO_CLOSE_DELAY`
- `EYE_MAX_BRIGHT`
- `LED_UPDATE_DELAY`
- `NUM_LEDS_DOME`
- `NUM_LEDS_JAW`

### 13.4 BUTTON / CLICK

- `BUTTON_DEBOUNCE`
- `BUTTON_COOLDOWN`
- `MULTI_CLICK_WINDOW`
- `SINGLE_CLICK_DECISION_DELAY`
- `TRIPLE_CLICK_COUNT`
- `BUTTON_USE_KEYPAD_EVENTS`

### 13.5 DEMO / DIAG

- `DEMO_FX_DURATION`
- `DEMO_SEQUENCE_ENABLED`
- `DEMO_STAGE_IGNITION`
- `DEMO_STAGE_OPEN_HOLD`
- `DEMO_STAGE_CLOSE_HOLD`
- `DEMO_STAGE_ARC`
- `DEMO_STAGE_FINAL_HOLD`
- `DEMO_EYE_PULSE_MIN`
- `RUNTIME_DIAG_ENABLED`
- `RUNTIME_DIAG_INTERVAL`

### 13.6 AUDIO / SHOWOFF

- `SND_STARTUP`
- `SND_OPEN`
- `SND_CLOSE`
- `SHOW_OFF_ENABLED`
- `SHOW_OFF_INTERVAL`

---

## 14. Konfigurator USB - jak uzywac poprawnie

Plik: `configurator_usb.html`

### 14.1 Procedura strojenia

1. `python3 tool_final_build.py serve-ui --port 8000`
2. Otworz `http://127.0.0.1:8000/configurator_usb.html`
3. Kliknij `Polacz USB`
4. Kliknij `Pobierz z plytki`
5. Strojenie:
   - najpierw servo i bezpieczenstwo,
   - potem laser,
   - potem LED/eyes/demo.
6. Po strojeniu przepisz finalne wartosci do `config.py`.

### 14.2 Znaczenie opcji "Paruj asymetrycznie HIGH<->LOW"

Gdy ON:

- `S2_OPEN` i `S2_CLOSE` sa wyliczane automatycznie,
- edytujesz glownie `S1_OPEN` i `S1_CLOSE`,
- prawa strona ma odwracany suwak wizualnie.

Gdy OFF:

- kazde serwo regulujesz osobno.

### 14.3 Pop-upy

Kazdy parametr ma przycisk `?`.
Opis podaje:

- co realnie zmienia,
- jaki jest efekt uboczny,
- czy parametr jest bezpieczenstwa/ruchu/wizualu.

---

## 15. Procedura kalibracji serw (zalecana)

Tryb bezpieczny:

1. Ustaw preset safe (`Preset Safe Servo`) albo recznie:
   - nizsza predkosc,
   - wiekszy settle/release.
2. Wlacz parowanie asymetryczne.
3. Ustaw `SERVO_PAIR_SUM` zgodnie z mechanika:
   - klasycznie 180,
   - dla 0/90 ustaw 90.
4. Strojenie CLOSE:
   - tak, zeby maska domykala bez docisku.
5. Strojenie OPEN:
   - tak, zeby nie dobija byla na skraju.
6. Zwieksz `OPEN_REDUCTION_DEG` jesli koncowka nadal jest agresywna.
7. Potwierdz:
   - ruch powtarzalny,
   - brak przegrzewania serw po kilku cyklach.

---

## 16. Test plan na realnym sprzecie (obowiazkowy)

### 16.1 Test A - boot i inicjalizacja

1. Restart plytki.
2. Oczekiwane:
   - brak exception na serialu,
   - startup audio (jesli I2S i plik sa dostepne),
   - serwa w stanie otwartym startowym.

### 16.2 Test B - przycisk

1. Single click:
   - open -> close -> open.
2. Sprawdz cooldown:
   - po otwarciu przez 2s brak ponownego toggle.
3. Triple click:
   - start demo sequence.

### 16.3 Test C - laser 25 cm

1. Ustaw obiekt ~25 cm.
2. Oczekiwane:
   - po debounce + hold maska sie otwiera.
3. Odsun obiekt.
4. Oczekiwane:
   - po `AUTO_CLOSE_DELAY` maska sie zamyka.

### 16.4 Test D - safety serw

1. 20-30 cykli open/close.
2. Oczekiwane:
   - brak zaciec,
   - brak agresywnego "strzalu" na starcie ruchu,
   - po close serwa puszczane (`release_all`) przy aktywnej opcji.

### 16.5 Test E - demo

1. Trigger demo z przycisku i z USB.
2. Oczekiwane:
   - pelna sekwencja etapow,
   - oczy i LED zsynchronizowane,
   - brak kolizji z laserem i normalnym toggle podczas demo.

---

## 17. Najczestsze problemy i rozwiazania

### Problem: serwa drgaja lub mocno sie grzeja

Dzialania:

1. Zmniejsz `SERVO_MAX_SPEED_DPS`.
2. Zwieksz `SERVO_UPDATE_DELAY`.
3. Zwieksz `OPEN_REDUCTION_DEG`.
4. Sprawdz czy `SERVO_RELEASE_AFTER_CLOSE=True`.
5. Skoryguj pozycje CLOSE, zeby nie dociskac mechaniki.

### Problem: maska podnosi sie za wolno (jakby serwo nie mialo sily)

Dzialania:

1. Zwieksz `SERVO_MAX_SPEED_DPS`.
2. Zwieksz `SERVO_OPEN_SPEED_MULT`.
3. Ustaw `SERVO_OPEN_FAST_EASE=True` (mocniejszy start ruchu).
4. Zmniejsz `SERVO_UPDATE_DELAY` (gestsze kroki sterowania).
5. Upewnij sie, ze zasilanie serw jest stabilne (osobna linia + kondensator, wspolna masa).

### Problem: maska nie reaguje na laser

Dzialania:

1. Sprawdz czujnik i I2C.
2. Sprawdz `LASER_DIST_LIMIT` i `LASER_MIN_VALID_MM`.
3. Zmniejsz `LASER_DEBOUNCE` i/lub `LASER_HOLD_TIME` testowo.
4. Sprawdz logi runtime (`dist=... hand=...`).

### Problem: demo nie startuje

Dzialania:

1. Sprawdz `DEMO_SEQUENCE_ENABLED=True`.
2. Sprawdz czy nie jest aktywny `jaw_detached`.
3. Sprawdz czy nie jest aktywny `tuning_mode`.
4. Uzyj `trigger_demo` z konfiguratora i sprawdz ack.

### Problem: konfigurator nie laczy sie z USB

Dzialania:

1. Uzyj Chrome/Edge (Web Serial).
2. Kliknij `Polacz USB` i wybierz poprawny port.
3. Zamknij inne aplikacje, ktore trzymaja port.
4. Sprawdz kabel USB data (nie tylko ladowanie).

---

## 18. Procedura deploy na CIRCUITPY

1. Wykonaj backup aktualnych plikow z plytki.
2. Skopiuj pliki runtime z `final/` na dysk `CIRCUITPY`.
3. Dodaj biblioteki adafruit w `/lib` (zgodnie z importami).
4. Upewnij sie, ze `startup.wav` jest w `/sounds`.
5. Restart plytki.
6. Przejdz test plan z sekcji 16.

---

## 19. Procedura "zmieniam cos i nie chce regresji"

Przed zmianami:

1. `python3 tool_final_build.py preflight`
2. Snapshot `config.py` (kopiuj do backupu).

Po zmianach:

1. `python3 tool_final_build.py preflight`
2. Test A/B/C/D/E z sekcji 16.
3. `python3 tool_final_build.py build --preflight`
4. Zarchiwizuj ZIP + manifest.

---

## 20. Zasady dalszego rozwoju

1. Nie psuc priorytetu ruchu maski.
2. Kazda nowa funkcja ma byc "non-blocking" i ma miec jasna zaleznosc od stanu.
3. Zmiany ruchu serw zawsze testowac na realnym hardware.
4. Audio i efekty nigdy nie moga blokowac loopa sterowania.
5. Kazdy nowy parametr:
   - dodac do `config.py`,
   - dodac do konfiguratora,
   - dodac opis popup,
   - dopisac do tego dokumentu.

---

## 21. FAQ (krotko)

### Czy moge zostawic stale aktywne trzymanie serwa?

Mozesz, ale niezalecane. Wiekszy pobor i grzanie.

### Czy moge zmienic cooldown?

Tak, `BUTTON_COOLDOWN`, ale przy zbyt malym czasie rośnie ryzyko przypadkowych toggle.

### Czy dzwieki open/close sa aktywne?

Nie, obecnie nie sa wywolywane w logice ruchu.

### Czy ustawienia z konfiguratora zapisuja sie na stale?

Nie. To RAM runtime. Trwale zmiany wpisujesz do `config.py`.

---

## 22. Szybka checklista "przed oddaniem projektu"

1. `preflight` przechodzi bez bledow.
2. Laser otwiera przy ~25 cm i zamyka po timeout.
3. Cooldown 2 s dziala.
4. Triple click uruchamia dlugie demo.
5. Serwa po close sa odpuszczane (jesli opcja wlaczona).
6. Brak dzwieku open/close podczas ruchu.
7. Konfigurator laczy sie po USB i wysyla config.
8. Finalny ZIP wygenerowany i zarchiwizowany.
