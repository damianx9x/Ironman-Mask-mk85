# 💻 DOKUMENTACJA OPROGRAMOWANIA (SOFTWARE)

## 1. LOGIKA SYSTEMU (STATE MACHINE)

### A. Tryb Zakładania (Jaw Detached)
*   Aktywowany, gdy pin **D10** jest w stanie wysokim (szczęka odpięta).
*   Maska automatycznie się otwiera.
*   Oczy gasną, wnętrze kopuły świeci na biało (latarka).
*   Sterowanie głosem i laserem jest zablokowane.

### B. Start Systemu
*   Maska ustawia się w pozycji OTWARTEJ.
*   Odtwarza dźwięk powitalny.
*   HUD świeci na niebiesko (pulsowanie).

### C. Otwarcie Manualne (Przycisk)
*   Wciśnięcie przycisku zmienia stan na przeciwny.
*   Aktywuje flagę `manual_open = True` -> Maska **nie zamknie się sama**.

### D. Otwarcie Automatyczne (Laser)
*   Wymaga zbliżenia ręki (< 20 cm) przez 3 sekundy.
*   Po zabraniu ręki uruchamia licznik 5 sekund do auto-zamknięcia.
*   Priorytet: Laser nadpisuje tryb manualny (włącza auto-zamykanie).

---

## 2. SYGNALIZACJA WIZUALNA (HUD)

| Kolor | Znaczenie |
| :--- | :--- |
| **ZIELONY** | Diagnostyka – czujnik widzi rękę (trzymaj dalej). |
| **CZERWONY** | Ostrzeżenie – serwa są w ruchu (nie wkładaj palców). |
| **NIEBIESKI** | Standby – maska otwarta, system gotowy. |
| **ZGASZONY** | Maska zamknięta (ciemność w środku). |

---

## 3. ZABEZPIECZENIA (SAFETY)

1.  **Priorytet Ruchu:** Podczas pracy serw czujnik laserowy jest ignorowany, aby procesor generował stabilny sygnał PWM.
2.  **Filtr Szumów (Debounce):** Laser musi potwierdzić odczyt 3 razy z rzędu.
3.  **Hot-Plug Protection:** Odpięcie szczęki (lasera) nie zawiesza programu (bloki `try...except` na I2C).