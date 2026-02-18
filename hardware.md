# 🛠️ DOKUMENTACJA SPRZĘTOWA (HARDWARE)

## 1. OPIS FIZYCZNY I KONSTRUKCJA

**Model:** Hełm Iron Man MK5 przeskalowany do 110%.
**Technologia:** Druk 3D (FDM) + Galwanizacja miedzią.
**Waga przyłbicy:** ok. 200g.

### Mechanika Ruchu
*   **Serwa:** 2x MG90s (Metal Gear) w skroniach.
*   **Wspomaganie:** Zalecana przeciwwaga (sprężyna) wewnątrz zawiasu.

### System Połączeń (Hybrydowy)
*   **Mocowanie:** 16 par magnesów neodymowych 8x1mm.
*   **Elektryka:** Szybkozłączki Pogo-Pin.
    *   **Lewa strona (5-pin):** Zasilanie i Dane (Laser, LED).
    *   **Prawa strona (3-pin):** Audio i Bezpieczeństwo (Sense).

---

## 2. SCHEMAT POŁĄCZEŃ (PINOUT MASTER)

| Komponent | Pin na Płytce | Typ Sygnału | Opis |
| :--- | :--- | :--- | :--- |
| **Zasilanie** | USB / BAT | Power In | Zasilanie z Huba (+5V) |
| **Masa** | GND | GND | Wspólna masa |
| **Power Enable** | GPIO 23 | Digital Out | Włącza zasilanie 5V dla LED/Serw |
| **Serwo Lewe** | D11 | PWM | Sygnał serwa |
| **Serwo Prawe** | D12 | PWM | Sygnał serwa |
| **Oczy (LED)** | D5 | PWM Output | Plus diody (+ Rezystor 100Ω) |
| **Kopuła (LED)** | TX (GPIO 0) | NeoPixel Data | Pasek wewnątrz kasku |
| **Szczęka (LED)** | RX (GPIO 1) | NeoPixel Data | Pasek w szczęce (HUD) |
| **Przycisk** | Btn (GPIO 19) | Digital In | Druga noga do GND |
| **Laser SDA** | SDA (GPIO 2) | I2C Data | Do złącza 5-pin (Lewe) |
| **Laser SCL** | SCL (GPIO 3) | I2C Clock | Do złącza 5-pin (Lewe) |
| **Mikrofon SCK** | SCK | I2S Clock | Pin SCK na INMP441 |
| **Mikrofon WS** | MI (MISO) | I2S Word Select | Pin WS na INMP441 |
| **Mikrofon SD** | MO (MOSI) | I2S Data | Pin SD na INMP441 |
| **Detekcja Szczęki** | D10 | Digital In | Do pinu "Sense" (Pogo-Pin) |

---

## 3. SYSTEM ZASILANIA

*   **Źródło:** Powerbank 5V / 2.4A.
*   **Kondensatory:**
    *   1000µF 16V w Hubie (Kopuła) – chroni MCU przed resetem.
    *   470µF w Szczęce – stabilizuje laser i LEDy.