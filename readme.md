# 🦾 Iron Man MK85 Interactive Mask / Maska Iron Man MK85

> **Advanced Wearable Project with Motorized Jaw, AI Voice Control & IoT**  
> **Zaawansowany Projekt Wearable'a z Motoryzowaną Szczęką, Kontrolą Głosem AI & IoT**

![Status](https://img.shields.io/badge/Status-Active-green) ![Language](https://img.shields.io/badge/Language-Python%20%7C%20CircuitPython-blue) ![Hardware](https://img.shields.io/badge/Hardware-Adafruit%20RP2040-orange)

---

## 📋 **English / Overview**

**Iron Man MK85 Mask** is a fully interactive, wearable helmet project featuring:

✨ **Motorized Jaw Movement** - 2x MG90s servos with smooth animations  
💡 **RGB LED Systems** - Eyes, Dome HUD (NeoPixel), Arc Reactor glow  
🔊 **Advanced Audio** - JARVIS voice pack, I2S microphone, real-time synthesis  
🎯 **Gesture Recognition** - Laser proximity sensor + jaw detection  
🌐 **IoT Connectivity** - WiFi dashboard, MQTT, real-time telemetry  
⚙️ **State Machine AI** - Intelligent automation & decision making  
🔧 **Hybrid Connector** - Magnetic + Pogo-Pin system for hot-swap jaw  

**Core Innovation**: Fully automated state management with voice/gesture recognition, powered by Adafruit RP2040 Prop-Maker Feather.

### 🎭 **Key Features**

#### **Mechanical Systems**
- **Motorized Jaw**: 2x MG90s Metal Gear servos in temples (smooth 0-85° range)
- **Magnetic Connector**: 16x 8x1mm neodymium magnets for structural integrity
- **Pogo-Pin System**: 5-pin (power+laser) + 3-pin (audio+sense) hot-swap
- **3D Printed**: FDM TPU + copper electroplating (110% scaled MK5 helmet)

#### **LED & Light Systems**
- **Eye LEDs**: Direct PWM control for intensity effects + color transitions
- **Dome HUD**: WS2812B NeoPixel strip (addressable RGB) - state indicator
- **Arc Reactor**: NeoPixel strip in jaw - visual feedback + status display
- **Color-Coded States**: Blue (idle), Yellow (armed), Red (alert), Green (active)

#### **Audio & Voice**
- **MEMS Microphone** (INMP441): I2S digital interface for voice detection
- **Class D Amplifier**: 0.5W speaker for voice synthesis & effects
- **JARVIS Voice Pack**: Pre-programmed AI responses
- **Real-Time Processing**: Command recognition + feedback

#### **Sensors & Automation**
- **Laser Distance Sensor** (VL53L0X): Hand proximity detection (< 20cm threshold)
- **Jaw Detection** (GPIO): Magnetic detachment sensor via Pogo-Pin
- **3-Second Auto-Open**: Gesture recognition for contactless activation
- **5-Second Auto-Close**: Smart energy management

#### **Smart Power Management**
- **5V/2.4A PowerBank**: Stable external power source
- **Smart Enable Pin**: GPIO 23 controls outlet for servos/LEDs
- **Capacitor Bank**: 1000µF (dome) + 470µF (jaw) for stability
- **5-6 Hour Runtime**: Efficient power distribution

---

## 🛠️ **Dokumentacja Polski**

**Maska Iron Man MK85** to w pełni interaktywny projekt wearable'a z:

✨ **Motoryzowana Szczęka** - 2x serwomechanizymy MG90s z płynną animacją  
💡 **Systemy LED RGB** - Oczy, HUD Kopuły (NeoPixel), blask Reaktora Łuku  
🔊 **Zaawansowane Audio** - Pakiet głosu JARVIS, mikrofon I2S, synteza w czasie rzeczywistym  
🎯 **Rekonogscencja Gestów** - Czujnik laserowy + detekcja szczęki  
🌐 **Łączność IoT** - Pulpit WiFi, MQTT, telemetria w czasie rzeczywistym  
⚙️ **AI Maszyna Stanów** - Inteligentna automatyzacja & podejmowanie decyzji  
🔧 **Hybrydowy Złącze** - System magnetyczny + Pogo-Pin do gorącego wymiany szczęki  

**Kluczowa Innowacja**: W pełni zautomatyzowane zarządzanie stanami z rozpoznawaniem głosu/gestów, zasilane procesorem Adafruit RP2040 Prop-Maker Feather.

### 🎭 **Główne Funkcje**

#### **Systemy Mechaniczne**
- **Motoryzowana Szczęka**: 2x serwomechanizymy MG90s Metal Gear w skroniach (gładki zakres 0-85°)
- **Złącze Magnetyczne**: 16x magnesy neodymowe 8x1mm dla integralności strukturalnej
- **System Pogo-Pin**: 5-pin (zasilanie+laser) + 3-pin (audio+czujnik) gorąca wymiana
- **Druk 3D**: FDM TPU + galwanizacja miedziowa (hełm MK5 w skali 110%)

#### **Systemy Oświetlenia LED**
- **Oczy LED**: Bezpośrednia kontrola PWM dla efektów intensywności + przejścia kolorów
- **HUD Kopuły**: Pasek WS2812B NeoPixel (adresowane RGB) - wskaźnik stanu
- **Reaktor Łuku**: Pasek NeoPixel w szczęce - sprzężenie zwrotne wizualne + wyświetlanie stanu
- **Kodowanie Kolorami Stanów**: Niebieski (bezczynny), Żółty (uzbrojony), Czerwony (alert), Zielony (aktywny)

#### **Audio & Głos**
- **Mikrofon MEMS** (INMP441): Interfejs cyfrowy I2S do detekcji głosu
- **Wzmacniacz Klasy D**: Głośnik 0.5W do syntezy głosu & efektów
- **Pakiet Głosu JARVIS**: Wstępnie zaprogramowane odpowiedzi AI
- **Przetwarzanie w Czasie Rzeczywistym**: Rozpoznawanie komend + sprzężenie zwrotne

#### **Czujniki & Automatyzacja**
- **Czujnik Laserowy** (VL53L0X): Detekcja bliskości ręki (próg < 20cm)
- **Detekcja Szczęki** (GPIO): Czujnik magnetycznego odłączenia poprzez Pogo-Pin
- **3-Sekundowe Auto-Otwarcie**: Rekonогscencja gestów dla aktywacji bez kontaktu
- **5-Sekundowe Auto-Zamknięcie**: Inteligentne zarządzanie energią

#### **Inteligentne Zarządzanie Energią**
- **PowerBank 5V/2.4A**: Stabilne źródło zasilania zewnętrznego
- **Pin Inteligentnego Włączania**: GPIO 23 kontroluje gniazdo dla serw/LED
- **Bank Kondensatorów**: 1000µF (kopuła) + 470µF (szczęka) dla stabilności
- **Żywotność 5-6 Godzin**: Efektywna dystrybucja energii

---

## 🔧 **Hardware Specifications / Specyfikacja Sprzętu**

### **Core Controller / Procesor**
| Component | Specifications | Purpose |
|-----------|---|---|
| **Adafruit RP2040 Prop-Maker Feather** | ARM Cortex-M0+, 133 MHz, 8 MB Flash, 264K RAM | Main control unit - state machine, sensor polling, audio synthesis |
| **Power Management** | USB-C + Optional LiPoly | 5V/2.4A external PowerBank for servos/LEDs |

### **Actuators / Aktuatory**
| Component | Count | Specs | Connection | Function |
|-----------|-------|-------|-----------|----------|
| **MG90s Metal Gear Servo** | 2x | 4.8-6V, 55 oz*in torque, 0-180° | GPIO 20/21 (PWM) | Jaw opening/closing in temples |
| **Magnetic Connector** | 16x | 8x1mm Neodymium N42 | Adhesive-mounted | Structural integrity + alignment |

### **Sensor Systems / Systemy Czujników**
| Sensor | Model | Protocol | GPIO/Pin | Detects |
|--------|-------|----------|----------|---------|
| **Laser Distance** | VL53L0X | I2C (0x29) | SDA/SCL | Hand proximity (<20cm) |
| **Jaw Detector** | Magnetic Reed | GPIO 13 | D13 | Jaw attachment/detachment |
| **Accelerometer** | LIS3DH (onboard) | I2C/I2S | Built-in | Motion, tap, tilt detection |

### **Audio & Voice / Audio & Głos**
| Component | Specs | Interface | Function |
|----------|-------|-----------|----------|
| **MEMS Microphone** | INMP441 (I2S) | I2S (GPIO 15/14/13) | Real-time voice command detection |
| **Class D Amplifier** | MAX98357A, 0.5W | I2S Digital | JARVIS voice synthesis + effects |
| **Speaker** | 4Ω, 0.5W | Screw Terminal | Audio output (voice, alerts, effects) |

### **Visual Systems (Lighting) / Systemy Wizualne**
| System | Type | Count | Protocol | GPIO | Function |
|--------|------|-------|----------|------|----------|
| **Eye LEDs** | Direct RGB PWM | 2 sets | GPIO 2/3/4 | Eye glow control |
| **Dome HUD** | WS2812B NeoPixel | 1 strip | GPIO 5 | Status indicator (color-coded states) |
| **Arc Reactor** | WS2812B NeoPixel | 1 strip | GPIO 6 | Visual feedback + glow effects |

### **Power Distribution / Dystrybucja Energii**
| Rail | Voltage | Capacity | Uses | Protection |
|------|---------|----------|------|-----------|
| **Main 5V** | 5V/2.4A | PowerBank | Servos, Amplifier, Sensors | GPIO 23 Enable Pin |
| **Logic 3.3V** | 3.3V (onboard) | USB/LiPoly | RP2040, Sensors, LEDs | Built-in regulator |
| **Capacitor Bank** | 5V | 1470µF total | Servo surge protection | (dome 1000µF + jaw 470µF) |

### **Connectivity / Łączność**
| Interface | Protocol | Purpose |
|-----------|----------|---------|
| **WiFi** | 802.11n (RP2040 capable) | Dashboard control + MQTT telemetry |
| **Pogo-Pin Hybrid** | 5-pin + 3-pin | Hot-swap jaw (Power+Laser / Audio+Sense) |
| **USB-C** | Serial + Power | Programming + USB charging backup |

---

## 🧠 **Software Architecture / Architektura Oprogramowania**

### **State Machine / Maszyna Stanów**

```
┌─────────────┐
│   POWERED   │
└──────┬──────┘
       │
       ▼
┌──────────────┐     Jaw Closed → False
│   IDLE/OFF   │◄─────────────────────────┐
│┌────────────┐│                          │
││ Blue HUD   ││                          │
│└────────────┘│                          │
└──────┬───────┘                          │
       │ Voice: "GOOD MORNING"            │
       │ OR Gesture: Hand <20cm           │
       │                                  │
       ▼                                  │
┌──────────────┐                          │
│   ARMED      │ (Yellow HUD)             │
│┌────────────┐│─────────────────────────┤
││ Loading...  ││ 3s timeout              │
│└────────────┘│→ Auto-Open               │
└──────┬───────┘                          │
       │ Gesture: Hand closes/jaw opens   │
       │                                  │
       ▼                                  │
┌──────────────┐                          │
│   ACTIVE     │                          │
│┌────────────┐│ (Green HUD)              │
││ Processing │││─ Voice Command Mode     │
│└────────────┘││─ Servo Control Enable   │
└──────┬───────┘│─ Arc Reactor glowing    │
       │        └──────────────────┐      │
       │ 5s No Motion              │      │
       │ OR "STAND DOWN"           │      │
       ▼                           │      │
    AUTO-CLOSE ─────────────────────┘
```

### **Python Modules / Moduły Python**

#### **1. `code.py` - Main State Machine / Główna Maszyna Stanów**
```python
# Entry point for mask operation
# Core logic:
#  - Initializes all subsystems (audio, LEDs, servos, sensors)
#  - Manages state transitions
#  - Handles user input (voice, gesture, manual controls)
#  - Implements safety checks (jaw open limits, servo bounds)
#  - Manages power states (active/sleep modes)
#
# Key Functions:
#  - update_state(): Poll sensors, trigger transitions
#  - handle_voice_command(): Process JARVIS recognition
#  - gesture_detect(): Monitor laser + jaw sensor
#  - auto_idle(): 5-second timeout to idle state
```

#### **2. `leds.py` - NeoPixel & LED Control / Kontrola LED**
```python
# RGB LED management system
#
# Control Systems:
#  - Dome HUD: WS2812B strip for state indicator
#  - Arc Reactor: WS2812B in jaw for visual feedback
#  - Eye LEDs: Direct PWM for intensity control
#
# Color Mapping:
#  - Blue (#0000FF): IDLE state, system healthy
#  - Yellow (#FFFF00): ARMED state, loading animation
#  - Green (#00FF00): ACTIVE state, ready
#  - Red (#FF0000): ERROR/ALERT state
#  - Cyan (#00FFFF): Voice recognition active
#  - Magenta (#FF00FF): Servo movement feedback
#
# Key Functions:
#  - set_hud_color(color): Update dome indicators
#  - pulse_effect(rate): Breathing/pulse animation
#  - arc_reactor_glow(): Continuous glow effect
#  - eye_intensity(val): 0-255 PWM brightness
```

#### **3. `servos.py` - Jaw Movement Control / Kontrola Ruchu Szczęki**
```python
# Servo automation for jaw mechanism
#
# Servos:
#  - GPIO 20: Right temple servo (0-85°)
#  - GPIO 21: Left temple servo (0-85°)
#
# Movement Profiles:
#  - OPEN: Swift 0→85° animation (200ms), smooth easing
#  - CLOSE: Controlled 85→0° decay (150ms), soft landing
#  - CLENCH: Rapid 0→50→0° pulse (jaw stress test)
#  - TAUNT: 50% open with servo jitter (menacing effect)
#
# Safety Features:
#  - Servo bounds checking (0-85° hard limits)
#  - Current sensing for servo strain detection
#  - Auto-stops if jaw magnetic detach detected
#
# Key Functions:
#  - open_jaw(speed): Animate to open position
#  - close_jaw(speed): Animate to closed position
#  - jaw_position(): Read current servo angle
#  - emergency_close(): Hard stop for safety
```

#### **4. `audio_sys.py` - Audio Processing / Przetwarzanie Audio**
```python
# I2S audio pipeline management
#
# Components:
#  - INMP441 Microphone (GPIO 14/15/13): Voice input
#  - MAX98357A Amplifier: Speaker output (0.5W)
#
# Functions:
#  - microphone_listen(): Real-time audio capture
#  - playback_sound(filename): Play WAV from storage
#  - amplitude_meter(): Monitor input levels
#  - audio_effects(): Echo, reverb, equalization
#
# JARVIS Voice Pack:
#  - "Good Morning"    (welcome)
#  - "Emergency Alert" (alarm state)
#  - "Systems Online"  (startup check)
#  - "Shutting Down"   (power-off sequence)
#
# Key Functions:
#  - play_effect(effect_type): Sound effect playback
#  - voice_synthesis(text): Real-time TTS generation
#  - listen_and_detect(): Command recognition loop
```

#### **5. `voice.py` - Voice Recognition / Rozpoznawanie Głosu**
```python
# JARVIS AI voice command system
#
# Commands Recognized:
#  - "WAKE UP" / "ONLINE": Activate mask
#  - "JARVIS" / "HELLO": Idle greeting response
#  - "STAND DOWN" / "SLEEP": Enter idle state
#  - "OPEN VISOR" / "OPEN": Manual jaw control
#  - "CLOSE VISOR" / "CLOSE": Manual jaw control
#  - "MAXIMUM POWER": Performance mode
#  - "SELF-TEST": Diagnostic sequence
#
# Processing:
#  - Audio stream → Frequency analysis (FFT)
#  - Keyword spotting (pattern matching)
#  - Confidence threshold (70% minimum)
#  - Response generation with tone variation
#
# Key Functions:
#  - detect_keyword(audio_data): Pattern match voice
#  - process_command(keyword): Execute voice action
#  - generate_response(command): Voice feedback synthesis
#  - confidence_level(): Returns 0-100 match percentage
```

#### **6. `laser.py` - Gesture Recognition / Rekonogscencja Gestów**
```python
# VL53L0X Time-of-Flight laser distance sensor
#
# Purpose:
#  - Detect hand proximity near mask face
#  - Trigger contactless "3-gesture activation"
#  - Enable safe interactive feedback
#
# Thresholds:
#  - Near (<10cm): High-confidence gesture detected
#  - Close (10-20cm): Potential gesture (yellow alert)
#  - Far (>20cm): No detection (idle state)
#
# Gesture Logic:
#  - Single Hand Wave: Cycle through HUD colors
#  - Sustained Proximity (3s): Auto-open jaw
#  - Rapid Hand Swipe: Toggle LED effects
#  - Hand Block: Emergency safety stop
#
# Key Functions:
#  - read_distance(): Get range in mm (100-1200mm)
#  - detect_gesture(threshold): Velocity/pattern analysis
#  - proximity_alarm(): Trigger alert if too close
#  - calibrate_sensor(): Initial zero-level setup
```

#### **7. `comms.py` - WiFi & MQTT Communication / Komunikacja WiFi**
```python
# IoT connectivity for remote monitoring/control
#
# WiFi:
#  - SSID: [Configured in config.py]
#  - Protocol: 802.11n @2.4GHz
#  - Connection: Auto-reconnect with backoff
#
# MQTT Topics:
#  - Published (telemetry):
#    - mask/state: Current state (IDLE/ARMED/ACTIVE)
#    - mask/jaw_angle: Servo position (0-85°)
#    - mask/hud_color: Current LED indicator
#    - mask/temperature: Internal temp (if available)
#    - mask/battery: Power bank voltage %
#
#  - Subscribed (commands):
#    - mask/command/jaw: "OPEN" / "CLOSE" / "<angle>"
#    - mask/command/hud: "BLUE" / "GREEN" / "RED" / "ALERT"
#    - mask/command/voice: Voice command relay
#    - mask/command/reset: Force state reset
#
# Messaging:
#  - QoS=1 (at-least-once delivery)
#  - Keep-alive: 60 seconds
#  - Reconnect: 5s exponential backoff (max 60s)
#
# Key Functions:
#  - connect_mqtt(): Establish broker connection
#  - publish_telemetry(): Send sensor data
#  - subscribe_commands(): Listen for remote control
#  - disconnected_handler(): Graceful offline mode
```

#### **8. `config.py` - Configuration Constants / Stałe Konfiguracji**
```python
# System parameters and customization
#
# WiFi Configuration:
WIFI_SSID = "Your_Network"          # Network SSID
WIFI_PASSWORD = "your_password"     # Network password
MQTT_BROKER = "mosquitto.local"     # MQTT broker address
MQTT_PORT = 1883                    # MQTT port (default)
MQTT_CLIENT_ID = "ironman-mk85"     # Unique device ID

# Servo Calibration:
SERVO_LEFT_PIN = 20                 # Temple left servo
SERVO_RIGHT_PIN = 21                # Temple right servo
SERVO_MIN = 0                       # Closed position (°)
SERVO_MAX = 85                      # Open position (°)
SERVO_SPEED = 200                   # Animation speed (ms)

# Audio Settings:
MICROPHONE_THRESHOLD = 3000         # Voice detection level
COMMAND_TIMEOUT = 5000              # Listen duration (ms)
PLAYBACK_VOLUME = 100               # Speaker volume (%)

# LED Configuration:
HUD_STRIP_PIN = 5                   # Dome NeoPixel
ARC_REACTOR_PIN = 6                 # Jaw NeoPixel
NUM_HUD_LEDS = 16                   # Strip length
BRIGHTNESS = 200                    # Max brightness (0-255)

# State Machine:
AUTO_IDLE_TIMEOUT = 5000            # 5s no-activity timeout
GESTURE_TRIGGER_TIME = 3000         # 3s hand proximity to open
SERVO_SETTLE_TIME = 500             # Servo movement buffer

# Safety Limits:
MAX_SERVO_CURRENT = 500             # mA (stall protection)
MAX_AMPLIFIER_TEMP = 80             # °C (thermal shutdown)
MIN_BATTERY_VOLTAGE = 3.7           # V (LiPoly cutoff)

# Feature Flags:
ENABLE_VOICE_CONTROL = True         # JARVIS AI
ENABLE_GESTURE_RECOGNITION = True   # Laser-based activation
ENABLE_MQTT = True                  # IoT connectivity
ENABLE_DIAGNOSTICS = False          # Debug logging mode
```

#### **9. `logic_core.py` - Decision Engine / Silnik Decyzyjny**
```python
# Advanced decision-making and automation logic
#
# Behavioral Modes:
#  - SENTINEL: Passive monitoring mode
#  - COMBAT: Aggressive response mode
#  - GUARDIAN: Protective activation mode
#  - DIAGNOSTIC: Self-test automation
#
# Priority-Based Actions:
#  1. Safety checks (thermal, power, mechanical limits)
#  2. Emergency commands (voice "STAND DOWN")
#  3. Gesture recognition (hand proximity)
#  4. Scheduled automation (idle timeouts)
#  5. MQTT remote commands (lowest priority)
#
# Intelligence Features:
#  - Learns preferred activation method (voice vs gesture)
#  - Predicts user intent based on voice emotion
#  - Adaptive LED brightness (based on ambient light)
#  - Servo speed adaptation (based on previous patterns)
#
# Key Functions:
#  - evaluate_context(): Analyze combined sensor inputs
#  - predict_next_state(): ML-based state suggestion
#  - apply_priorities(): Conflict resolution
#  - log_behavior(): Pattern learning database
```

#### **10. `dashboard.html` - Web Interface / Interfejs Sieciowy**
```
Modern HTML5/CSS3 + JavaScript dashboard

Features:
 ✓ Real-time servo position slider (0-85°)
 ✓ State indicator with color-coded badges
 ✓ HUD LED color picker (RGB palette)
 ✓ Audio level meter (microphone sensitivity)
 ✓ Telemetry graphs (servo position vs time)
 ✓ Command console (send raw actions)
 ✓ LED effect presets (pulse, wave, strobe)
 ✓ Voice command history log
 ✓ Temperature/power monitoring
 ✓ Emergency STOP button (red, large)

Access via: http://<mask-ip>:8080/dashboard
```

---

## ⚡ **Power Management & Energy / Zarządzanie Energią**

### **Power Consumption Breakdown / Zużycie Energii**
| System | Mode | Current (mA) | Power (W) |
|--------|------|------|------|
| **RP2040 Processor** | Idle | 30 | 0.15W |
| | Active | 80 | 0.4W |
| **NeoPixel LEDs** | Off | 0 | 0 |
| | Full Brightness | 800 | 4W |
| **Servos** | Idle (holding) | 100 | 0.5W |
| | Moving | 400-800 | 2-4W |
| **Microphone + Amp** | Listening | 200 | 1W |
| | Playback (50% vol) | 350 | 1.75W |
| **WiFi Radio** | Connected | 120 | 0.6W |
| | Transmitting | 250 | 1.25W |
| | Off | 0 | 0 |

### **Runtime Estimate / Szacunkowy Czas Działania**

**Typical Usage Scenario** (Mixed mode):
- 30% active state (servos + audio)
- 40% idle state (listening, HUD dim)
- 30% sleep state (standby)

**Result**: **5-6 hours continuous operation** with standard 5V/2.4A PowerBank

**Optimization**:
- Enable sleep mode between activations
- Reduce LED brightness during day
- Limit WiFi to event-triggered updates
- **Extended mode**: 12+ hours with aggressive power management

---

## 🔌 **Hardware Pinout / Schemat Pinów**

### **RP2040 Pin Assignments**
```
GPIO 0-1   : [RESERVED - I2S Audio Data]
GPIO 2-4   : [Eye LEDs PWM - R/G/B]
GPIO 5     : [NeoPixel Dome HUD - WS2812B]
GPIO 6     : [NeoPixel Arc Reactor - WS2812B]
GPIO 13    : [Jaw Detector - Magnetic Switch]
GPIO 14-15 : [RESERVED - I2S Clock/Frame]
GPIO 20-21 : [Servo Control - PWM (Left/Right)]
GPIO 23    : [Power Enable - Servo/LED outlet]

I2C (SDA/SCL) : [VL53L0X Laser Sensor @ 0x29]
USB-C         : [Serial Programming + Power]
STEMMA QT     : [Expansion connector]
Pogo-Pin (5)  : [Hot-swap jaw power delivery + laser signal]
Pogo-Pin (3)  : [Audio + sense line for jaw autonomy]
```

---

## 🎯 **Usage & Operation / Użytkowanie i Obsługa**

### **Quick Start / Szybki Start**

**1. Power-On Sequence**
```
• Connect PowerBank to Pogo-Pin
• RP2040 boots, initializes subsystems
• Blue HUD illuminates → IDLE state
• JARVIS announces "Systems online"
```

**2. Voice Activation / Aktywacja Głosem**
```
You say: "JARVIS, WAKE UP"
 → Yellow HUD (ARMED state)
 → 3-second "Loading" animation
 → Jaw opens with servo animation
 → Green HUD (ACTIVE state)
```

**3. Gesture Activation / Aktywacja Gestem**
```
Hand proximity <20cm for 3 seconds
 → Red flash alert
 → Jaw opens automatically
 → Green HUD (ACTIVE state)
 → Audio: "Proximity detected"
```

**4. Deactivation / Dezaktywacja**
```
You say: "JARVIS, STAND DOWN"
 → Orange fade animation
 → Jaw closes smoothly
 → Blue HUD (IDLE state)
 → Audio: "Powering down visor"
```

---

## 🛡️ **Safety & Considerations / Bezpieczeństwo**

### **Mechanical Safety / Bezpieczeństwo Mechaniczne**
⚠️ **Finger Trap Risk**: Servo motors have significant torque
- Keep fingers clear during jaw animation
- Emergency stop via GPIO 23 (onboard button)
- Jaw magnetic detach provides passive safety

⚠️ **Power Surge**: Servo stall current can exceed 2A
- 1470µF capacitor bank absorbs transients
- GPIO 23 enable pin cuts servo power if overheating detected

⚠️ **Thermal Issues**: Class D amplifier heats up
- Monitor temperature via onboard sensor
- Auto-shutdown if >80°C
- Ensure airflow in jaw assembly

### **Electrical Safety / Bezpieczeństwo Elektryczne**
⚠️ **5V Power Line**: 2.4A external PowerBank
- Always use approved USB-C charger
- Check magnetic connectors for corrosion
- Replace capacitors if bulging detected (>5 years)

⚠️ **Pogo-Pin Contact**: Hot-swap system requires care
- Position jaw straight before insertion
- Listen for magnetic snap confirmation
- Clean contacts with isopropyl alcohol if corroded

### **Sensor Safety / Bezpieczeństwo Czujników**
⚠️ **Laser Distance Sensor** (VL53L0X)
- Eye-safe: Class 1 laser (IEC 60825-1)
- Do not look directly into sensor at close range
- Covers eyes with mesh to avoid direct beam

⚠️ **Microphone**: I2S MEMS microphone
- Voice command recording - no permanent storage
- Audio buffer cleared after each command
- WiFi transmission encrypted via TLS

---

## 🔧 **Troubleshooting / Rozwiązywanie Problemów**

| Problem | Cause | Solution |
|---------|-------|----------|
| **Jaw won't open** | Servo stalled / Magnetic detach | Check jaw magnets, re-attach, reset GPIO 23 |
| **No sound output** | Amplifier overheated or disconnected | Check speaker wires, cool down amp, test audio jack |
| **Voice not recognized** | Microphone muted / SNR too low | Adjust MICROPHONE_THRESHOLD in config.py |
| **LEDs flickering** | Loose NeoPixel wires / Capacitor failure | Reseat connectors, replace capacitors if >5 years old |
| **WiFi disconnects** | Weak signal / MQTT broker unreachable | Check distance to router, verify broker IP in config.py |
| **Servo jerking** | PID tuning issue / Power glitch | Adjust servo smooth values in config.py, increase capacitor |
| **HUD color wrong** | PWM pin conflict / LED data corruption | Re-upload firmware, check GPIO pin assignments |
| **Mask freezes** | Stack overflow / Memory leak | Check for infinite loops in voice.py, restart device |

---

## 📚 **Project Resources & Links / Zasoby Projektu**

### **Hardware Documentation**
- [Adafruit RP2040 Prop-Maker Feather](https://www.adafruit.com/product/5768) - Main controller datasheet
- [MG90s Servo Specs](https://www.towerpro.com.tw/product/mg90s-metal-gear-servo/) - Servo technical details
- [VL53L0X Laser Sensor](https://www.st.com/en/imaging-and-photonics/vl53l0x.html) - Distance sensor API

### **Software & Libraries**
- [**CircuitPython**](https://circuitpython.org/) - Adafruit's Python implementation for microcontrollers
- **adafruit_circuitpython_neopixel** - NeoPixel LED library
- **adafruit_circuitpython_vl53l0x** - Laser sensor library
- **adafruit_circuitpython_motor** - Servo control library
- **machine** (RP2040 native) - GPIO & PWM control

### **Communication Protocols**
- [MQTT 3.1.1 Specification](https://mqtt.org/) - IoT messaging standard
- [I2S Digital Audio](https://en.wikipedia.org/wiki/I%C2%B2S) - Audio interface protocol
- [WiFi 802.11n Standard](https://en.wikipedia.org/wiki/IEEE_802.11n) - Wireless networking

---

## 📖 **Additional Files / Dodatkowe Pliki**

- **`hardware.md`** - Detailed electrical schematics & pinout diagrams
- **`software.md`** - State machine documentation & flow charts  
- **`datasheet_rp2040.md`** - RP2040 microcontroller specifications
- **`adafruit-rp2040-prop-maker-feather.pdf`** - Official hardware manual (14.9MB)
- **`dashboard.html`** - Standalone web interface for remote control

---

## 👨‍💻 **Developer Notes / Notatki Programisty**

### **Coding Style**
- CircuitPython (MicroPython subset) - Compatible with RP2040
- Object-oriented design with State pattern for transitions
- Asynchronous event handling (non-blocking state machine)
- Comments in English + Polish for international team

### **Testing Checklist**
- [ ] Servos respond to GPIO commands (0-85° range test)
- [ ] All NeoPixel strips light up (color test pattern)
- [ ] Microphone picks up speech (frequency analysis)
- [ ] Laser sensor reads distance (0-1200mm range)
- [ ] WiFi connects to MQTT broker
- [ ] State machine transitions work (all 4 states)
- [ ] Power enable pin (GPIO 23) controls servos
- [ ] Jaw magnetic detach sensor triggers correctly
- [ ] Voice commands recognized (5/5 test phrases)
- [ ] Dashboard loads over WiFi (`http://<ip>:8080`)

### **Known Limitations**
- CircuitPython memory (~256K) limits voice processing to keyword spotting only
- Laser sensor needs calibration for different mask materials (IR absorption varies)
- I2S audio cannot stream from external sources (local WAV only)
- WiFi signal travels through metal faceplate (requires external antenna for 10m+ range)

---

## 📝 **License & Attribution / Licencja**

**This project uses Adafruit libraries and hardware under the MIT License.**

- **Adafruit CircuitPython**: MIT License
- **Prop-Maker Feather Design**: Adafruit Industries  
- **3D Model Base**: MK85 helmet from "Avengers: Infinity War" (fan-made adaptation)
- **Voice Pack**: JARVIS-inspired AI assistant (fictional character homage)

---

## 🤝 **Contributing & Support / Wsparcie**

### **To Report Issues**
Please open GitHub Issues with:
- Problem description (English or Polish)
- Error logs from serial console
- Hardware configuration details
- Reproduction steps

### **For Feature Requests**
Suggest new features on Discussions board:
- Voice command improvements
- Additional LED effects
- Dashboard enhancements
- Sensor integrations

---

## 📞 **Contact & Author / Autor**

**Created by**: Damian Eron (@damianx9x)  
**Status**: Active Development  
**Last Updated**: February 2025

---

**🦾 "Part of the suit, then you take the suit off and the suit doesn't care about you..."**  
*– Tony Stark*
- [Zelda Echoes Of Wisdom Tri Rod](https://learn.adafruit.com/zelda-tri-rod.md)
- [Halo Energy Sword RP2040](https://learn.adafruit.com/halo-energy-sword-rp2040.md)
- [Ahsoka Lightsaber Prop-Maker RP2040 retrofit](https://learn.adafruit.com/lightsaber-retrofit.md)
- [Adabot Toy Robot Friend](https://learn.adafruit.com/adabot-rp2040.md)
- [Motion Sensor Bat](https://learn.adafruit.com/motion-sensor-bat.md)
- [Tombstone Prop-Maker RP2040](https://learn.adafruit.com/tombstone-prop-maker-rp2040.md)
- [ Faz-Wrench - Five Nights at Freddy's](https://learn.adafruit.com/faz-wrench.md)
- [Make a Zelda Master Sword with the RP2040 Prop-Maker Feather](https://learn.adafruit.com/master-sword-rp2040.md)
- [Talking HAL 9000 with RP2040 Prop Maker Feather](https://learn.adafruit.com/hal-9000-rp2040-prop-maker.md)
- [Mario Magic Wand](https://learn.adafruit.com/mario-magic-wand.md)

Skip to main content
Shop Learn Blog Forums IO LIVE! AdaBox
Sign In  0
Adafruit Logo Explore & Learn New Guides Playground 
  Adafruit RP2040 Prop-Maker Feather  Pinouts
Adafruit RP2040 Prop-Maker Feather
This Feather is your one stop shop for making custom props!

by Liz Clark
published June 21, 2023, last edited September 23, 2025
last major update July 26, 2023
posted in Adafruit Products Arduino Compatibles Feather CircuitPython Raspberry Pi/ RP2040
 Save  Link Note  Download
Overview
Pinouts
Power Management
 CircuitPython
 CircuitPython Essentials
 Arduino IDE Setup
Factory Reset
Downloads
Single page
Feedback? Corrections?
Text View
Primary Products
Video of a white hand pressing a button to briefly turn an LED strip into white lights. Also wired up to the microcontroller are a servo motor and a speaker.
Adafruit RP2040 Prop-Maker Feather with I2S Audio Amplifier
$19.95
 41 Beginner Product guide 😍 1 💖 4 👍 2
Pinouts
adafruit_products_frontCroppped.jpg
adafruit_products_backCropped.jpg
This Feather has a lot going on! This page details all of the pin-specific information and various capabilities.

adafruit_products_Adafruit_RP2040_Prop-Maker_Feather_PrettyPins.png
PrettyPins PDF on GitHub.

Power Pins, Connections, and Charge LED
adafruit_products_powerPins.jpg
USB C connector - This is used for power and data. Connect to your computer via a USB C cable to update firmware and edit code.
LiPoly Battery connector - This 2-pin JST PH connector allows you to plug in LiPoly batteries to power the Feather. The Feather is also capable of charging batteries plugged into this port via USB.
chg LED - This small LED is located below the USB C connector. This indicates the charge status of a connected LiPoly battery when charging over USB. Note, it's normal for this LED to flicker when no battery is in place, that's the charge circuitry trying to detect whether a battery is there or not.
GND - This is the common ground for all power and logic.
BAT - This is the positive voltage to/from the 2-pin JST PH jack for the optional LiPoly battery.
USB - This is the positive voltage to/from the USB C connector, if USB is connected.
EN - This is the 3.3V regulator's enable pin. It's pulled up, so connect to ground to disable the 3.3V regulator.
3.3V - These pins are the output from the 3.3V regulator, they can supply 500mA peak.
adafruit_products_lipoChgJump.jpg
LiPo Chg - On the back of the board, behind the USB-C port, is the LiPo charge jumper. If you cut this jumper, it disconnects the lipoly battery charging circuit from the JST PH connector. As a result, you can safely use AA and AAA battery packs after cutting the jumper.
Logic Pins
adafruit_products_logicPins.jpg
I2C and SPI on RP2040
The RP2040 is capable of handling I2C, SPI and UART on many pins. However, there are really only two peripherals each of I2C, SPI and UART: I2C0 and I2C1, SPI0 and SPI1, and UART0 and UART1. So while many pins are capable of I2C, SPI and UART, you can only do two at a time, and only on separate peripherals, 0 and 1. I2C, SPI and UART peripherals are included and numbered below.

PWM on RP2040
The RP2040 supports PWM on all pins. However, it is not capable of PWM on all pins at the same time. There are 8 PWM "slices", each with two outputs, A and B. Each pin on the Feather is assigned a PWM slice and output. For example, A0 is PWM5 A, which means it is first output of the fifth slice. You can have up to 15 PWM objects on this Feather. The important thing to know is that you cannot use the same slice and output more than once at the same time. So, if you have a PWM object on pin A0, you cannot also put a PWM object on D10, because they are both PWM5 A. The PWM slices and outputs are indicated below. Note that PWM3 B is not available on this Feather because the pin is not broken out.

Analog Pins
The RP2040 has four ADCs. These pins are the only pins capable of handling analog, and they can also do digital.

A0/GPIO26 - This pin is ADC0. It is also SPI1 SCK, I2C1 SDA and PWM5 A.
A1/GPIO27 - This pin is ADC1. It is also SPI1 MOSI, I2C1 SCL and PWM5 B.
A2/GPIO28 - This pin is ADC2. It is also SPI1 MISO, I2C1 SDA and PWM6 A.
A3/GPIO29 - This pin is ADC3. It is also SPI1 CS, I2C0 SCL and PWM6 B.
Digital Pins
These are the digital I/O pins. They all have multiple capabilities.

D24/GPIO24 - Digital I/O pin 24. It is also UART1 TX, I2C0 SDA, and PWM4 A.
D25/GPIO25 - Digital I/O pin 25. It is also UART1 RX, I2C0 SCL, and PWM4 B.
SCK/GPIO14 - The main SPI1 SCK. It is also I2C1 SDA, and PWM7 A.
MO/GPIO15 - The main SPI1 MOSI. It is also I2C1 SCL, and PWM7 B.
MI/GPIO8 - The main SPI1 MISO. It is also UART1 TX, I2C0 SDA, and PWM4 A.
RX/GPIO1 - The main UART0 RX pin. It is also I2C0 SDA, SPI0 CS and PWM0 B.
TX/GPIO0 - The main UART0 TX pin. It is also I2C0 SCL, SPI0 MISO and PWM0 A.
D4/GPIO4 - Digital I/O pin 4. It is also RX0, TX1, SDA0 and PWM2A.
D13/GPIO13 - Digital I/O pin 13. It is also SPI1 CS, UART0 RX, I2C0 SCL and PWM6 B.
D12/GPIO12 - Digital I/O pin 12. It is also SPI1 MISO, UART0 TX, I2C0 SDA and PWM6 A.
D11/GPIO11 - Digital I/O pin 11. It is also SPI1 MOSI, I2C1 SCL and PWM5 B.
D10/GPIO10 - Digital I/O pin 10. It is also SPI1 SCK, I2C1 SDA and PWM5 A.
D9/GPIO9 - Digital I/O pin 9. It is also SPI1 CS, UART1 RX, I2C0 SCL and PWM4 B.
D6/GPIO6 - Digital I/O pin 6. It is also SPI0 SCK, I2C1 SDA, and PWM3 A.
D5/GPIO5 - Digital I/O pin 5. It is also SPI0 CS, UART1 RX, I2C0 SCL, and PWM2 B.
D4/GPIO4 - Digital I/O pin 4. It is also RX0, TX1, SDA0 and PWM2 A.
SCL/GPIO3 - The main I2C1 clock pin. It is also SPI0 MOSI, I2C1 SCL and PWM1 B.
SDA/GPIO2 - The main I2C1 data pin. It is also SPI0 SCK, I2C1 SDA and PWM1 A.
CircuitPython I2C, SPI and UART
Note that in CircuitPython, there is a board object each for STEMMA QT, I2C, SPI and UART that use the connector and pins labeled on the Feather. You can use these objects to initialize these peripherals in your code.

board.STEMMA_I2C() uses the STEMMA QT connector (in this case, SCL/SDA pins)
board.I2C() uses SCL/SDA pins (GPIO2 and GPIO3)
board.SPI() uses SCK/MO/MI pins (GPIO14, GPIO15 and GPIO8)
board.UART() uses RX/TX pins (GPIO0 and GPIO1)
Arduino I2C, SPI and UART
I2C, SPI and UART can be accessed with these objects in Arduino:

Wire is used for the default I2C and STEMMA QT connector (GPIO2 and GPIO3).
SPI is used for the default SPI pins (GPIO14, GPIO15 and GPIO8).
Serial1 is used for the default UART pins (GPIO0 and GPIO1).
The peripheral order is defined in the board support definition for Arduino. For example, you'll notice that even though the default I2C (GPIO2 and GPIO3) is located on I2C1, it is defined as Wire rather than Wire1.

GPIO Pins by Pin Functionality
Primary pins based on the silkscreen pin labels are bold.

I2C Pins
I2C0 SCL: A3, D25, RX, D13, D9, D5
I2C0 SDA: A2, D24, MISO, TX, D12, D4
I2C1 SCL: SCL, A1, MOSI, D11
I2C1 SDA: SDA, A0, SCK, D10, D6
SPI Pins
SPI0 SCK: D6, SDA
SPI0 MOSI: SCL
SPI0 MISO: TX
SPI0 CS: RX, D5
SPI1 SCK: SCK, A0, D10
SPI1 MOSI: MOSI, A1, D11
SPI1 MISO: MISO, A2, D24, D12
SPI1 CS: A3, D25, D13, D9
UART Pins
UART0 TX: TX, A2, D12
UART0 RX: RX, A3, D13, D4
UART1 TX: D24, MISO, D4
UART1 RX: D25, D9, D5
PWM Pins
PWM0 A: TX
PWM0 B: RX
PWM1 A: SDA
PWM1 B: SCL
PWM2 A: D4
PWM2 B: D5
PWM3 A: D6
PWM3 B: (none)
PWM4 A: D24, MISO
PWM4 B: D25, D9
PWM5 A: A0, D10
PWM5 B: A1, D11
PWM6 A: A2, D12
PWM6 B: A3, D13
PWM7 A: SCK
PWM7 B: MOSI
Terminal Block Pins (NeoPixel, Button and Speaker)
adafruit_products_terminalBlockPins.jpg
adafruit_products_terminalBlockLabels.jpg
On the front of the board is the terminal block for the special Prop-Maker pins: NeoPixels, button and speaker. On the back of the board, you can see the labels for each terminal block pin on the board silk.

Neo - The external NeoPixel data output pin. Connect your NeoPixel strip's data input pin to this connection. It located on GPIO21 and can be accessed as EXTERNAL_NEOPIXELS in CircuitPython and PIN_EXTERNAL_NEOPIXELS in Arduino.
G - Common ground for the external NeoPixels.
5V - 5V power for the external NeoPixels. This port provides high current drive from either the Feather LiPoly or USB port, whichever is higher. It is connected to a separate control transistor that is controlled by the External Power Pin described below. The External Power Pin is disabled by default, so you need to enable it in code to power the external NeoPixels.
Btn - Extra digital input or output pin. It can be used for button input or digital output, for activation or a simple LED. It located on GPIO19 and can be accessed as EXTERNAL_BUTTON in CircuitPython and PIN_EXTERNAL_BUTTON in Arduino.
+ and - - Positive and negative speaker output connections from the I2S amplifier. You can drive any 4-8Ω speaker, up to 3 Watts. 
Additionally, there is a pin that lets you control the external NeoPixels, servo motor header and I2S amp for low power applications:

External Power Pin - This pin is connected to a separate control transistor for the 5V terminal block pin, servo header and the I2S amplifier so that you can cut power to them for low power usage. It is located on GPIO23 and is accessed with EXTERNAL_POWER in CircuitPython and PIN_EXTERNAL_POWER in Arduino. It is disabled by default, so you will need to set the pin high to power the external NeoPixels, servo motor header pins and I2S amplifier.
You need to enable the External Power Pin in code to use the external NeoPixels, servo motor header and I2S amplifier.
Servo Connection
adafruit_products_servoPins.jpg
On the front of the board, to the left of the terminal block, are three 0.1" spaced header pins for connecting any hobby servo with three wires. The pins are labeled Servo on the board silk.

Sig - Servo motor output pin. It located on GPIO20 and can be accessed as EXTERNAL_SERVO in CircuitPython and PIN_EXTERNAL_SERVO in Arduino.
V+ - 5V power for the servo motor. This pin provides high current drive from either the Feather LiPoly or USB port, whichever is higher. It is connected to a separate control transistor that is controlled by the External Power Pin. The External Power Pin is disabled by default, so you need to enable it in code to power the external NeoPixels.
G - Common ground for the external servo motor.
MAX98357 I2S Amplifier
adafruit_products_i2s_amp.jpg
On the front of the board, above the MISO and RX pins, is the MAX98357 I2S amplifier. It is a 3 Watt Class D audio amplifier that can drive any 4-8Ω speaker, up to 3 Watts. It communicates with the RP2040 via three pins:

Data - Located on GPIO16. It can be accessed via I2S_DATA in CircuitPython and PIN_I2S_DATA in Arduino.
Clock - Located on GPIO17. It can be accessed via I2S_BIT_CLOCK in CircuitPython and PIN_I2S_BIT_CLOCK in Arduino.
Word Select - Located on GPIO18. It can be accessed via I2S_WORD_SELECT in CircuitPython and PIN_I2S_WORD_SELECT in Arduino.
To enable audio output from the amplifier, the External Power Pin needs to be enabled.

adafruit_products_i2s_ampGain.jpg
On the back of the board, above the RX and MI pins, are jumpers to adjust the I2S amp gain. The jumper pads are outlined on the silk and are labeled Amp Gain. The default gain for the amplifier is 9 dB

To set the gain to 6 dB, solder the center jumper to the left jumper labeled 6. This connects the GAIN pin to V+.
To se the gain to 12 dB, solder the center jumper to the right jumper labeled 12. This connects the GAIN pin to GND.
LIS3DH Accelerometer 
adafruit_products_accelWithOrientation.jpg
On the front of the board, to the right of the STEMMA QT connector, is the LIS3DH accelerometer. It is a triple-axis accelerometer with tap detection. You can use it for detection motion, tilt, or taps.

This accelerometer is connected over I2C on address 0x18. If you perform an I2C scan on this Feather with no other I2C devices connected, you will see this address. You can also use its interrupt pin to trigger for motion, tilt, taps, data ready, etc. The interrupt pin is connected to GPIO22 and can be accessed as ACCELEROMETER_INTERRUPT in CircuitPython and PIN_ACCELEROMETER_INTERRUPT in Arduino.

Microcontroller and Flash
adafruit_products_micro_flash.jpg
The large square towards the middle is the RP2040 microcontroller, the "brains" of this Feather board.

The square towards the top-middle is the QSPI Flash. It is connected to 6 pins that are not brought out on the GPIO pads. It is used for program and data storage in Arduino and CircuitPython.

Buttons and RST Pin
adafruit_products_buttons.jpg
The Boot button is the button on the right, located on GPIO7. It is available as board.BUTTON in CircuitPython and PIN_BUTTON in Arduino. It is also used to enter the bootloader. To enter the bootloader, press and hold Boot and then power up the board (either by plugging it into USB or pressing Reset). The bootloader is used to install/update CircuitPython.

The Reset button is on the left. It restarts the board and helps enter the bootloader. You can click it to reset the board without unplugging the USB cable or battery.

The Rst pin can be used to reset the board. Tie to ground manually to reset the board.

NeoPixel and Red LED
adafruit_products_neo_led.jpg
Above the pin labels for 24 and 25 is the status NeoPixel LED, labeled 4 on the board silk. It is connected to GPIO4. In CircuitPython, the NeoPixel is available at board.NEOPIXEL and the library for it is available in the bundle. In Arduino, it is accessible at PIN_NEOPIXEL. The NeoPixel is powered by the 3.3V power supply but that hasn't shown to make a big difference in brightness or color. In CircuitPython, the LED is used to indicate the runtime status.

Above the USB C connector is the D13 LED. This little red LED is controllable in CircuitPython code using board.LED, and in Arduino as PIN_LED.

STEMMA QT
adafruit_products_stemma.jpg
In the middle of the board, to the left of the terminal block, is the STEMMA QT connector! This means you can connect up all sorts of I2C sensors and breakouts, no soldering required! This connector uses the SCL and SDA pins for I2C, which end up being the RP2040's I2C1 peripheral. In CircuitPython, you can initialize the STEMMA connector with board.STEMMA_I2C() (as well as with board.SCL board.SDA). In Arduino it is Wire.

Angled shot of STEMMA QT / Qwiic JST SH 4-pin Cable.
STEMMA QT / Qwiic JST SH 4-pin Cable - 100mm Long
This 4-wire cable is a little over 100mm / 4" long and fitted with JST-SH female 4-pin connectors on both ends. Compared with the chunkier JST-PH these are 1mm pitch instead of...
$0.95
In Stock
Page last edited September 23, 2025

Text editor powered by tinymce.

Related Guides
Glowing orange orb with a jack-o'-lantern face sits atop a gray 3D printed hexagonal base. A small green light is visible inside the base.
PropMaker Jack O'Lantern
By Ruiz Brothers
intermediate
A turquoise 3D printed electronic guitar with a black fretboard featuring multicolored LED lights. Three black knobs and a button are on the body.
Guitar Synth with CircuitPython SynthIO
By Ruiz Brothers
advanced
Someone is pressing the button on the adabot robot head clock. the NeoPixels in his mouth light up and a speech bubble appears that says "the time is 10:26 AM"
Prop-Maker Feather Talking Adabot Clock
By Liz Clark
beginner
A hand holds a Prop-Maker RP2040 based lightsaber with a glowing green blade and a black hilt featuring a silver button and vent-like details.
Lightsaber Prop-Maker RP2040
By Ruiz Brothers
advanced
A hand holds a retro-style Gravity Falls Memory Gun with a clear bulb and red plexi at the front. The gun features a yellow body and a visible trigger.
Gravity Falls Memory Gun
By Ruiz Brothers
intermediate
Person holding a glowing green LED Zelda Echoes Of Wisdom Tri Rod staff with a twisted design, wearing a green hoodie. The staff emits a bright, even light.
Zelda Echoes Of Wisdom Tri Rod
By Ruiz Brothers
beginner
A hand holds a glowing Halo Energy Sword prop with purple LED lights illuminating the blade edges against a dark background.
Halo Energy Sword RP2040
By Ruiz Brothers
intermediate
A person in a brown cloak holds two crossed Ahsoka lightsabers, one red and one white, against a space-themed backdrop with planets and stars.
Ahsoka Lightsaber Prop-Maker RP2040 retrofit
By Ruiz Brothers
beginner
A light blue Adabot toy robot with a lightning bolt on its chest stands on a yellow background. It has flexible arms and a smiling face.
Adabot Toy Robot Friend
By Ruiz Brothers
advanced
A black motion sensor device with a glowing green LED is on a wooden table next to a pumpkin and a cauldron of candy. A backdrop of green flames adds a spooky ambiance.
Motion Sensor Bat
By Ruiz Brothers
beginner
Gargoyle statue with LED matrix display on its grey tombstone base shows scrolling red text. A black crow is perched nearby on the grass.
Tombstone Prop-Maker RP2040
By Ruiz Brothers
intermediate
Person wearing a bear mask holds an orange electronic Faz-Wrench device with antennas, buttons, and a display screen showing text.
Faz-Wrench - Five Nights at Freddy's
By Ruiz Brothers
intermediate
A person holds up a glowing blue 3D printed Zelda Master Sword with a detailed purple hilt, standing in front of lush green foliage and a tree.
Make a Zelda Master Sword with the RP2040 Prop-Maker...
By Ruiz Brothers
beginner
A tall, rectangular grey and silver HAL-9000 interface device with a large red dome light in the center and a small nameplate at the top. A pink cable is connected at the bottom.
Talking HAL 9000 with RP2040 Prop Maker Feather
By Ruiz Brothers
intermediate
A hand holds a glowing Mario Magic Wand with a pink LED-lit dome. The handle features a small circular button and a wrist strap.
Mario Magic Wand
By Ruiz Brothers
intermediate
Contact Us
Tech Support Forums
FAQs
Shipping & Returns
Freebies
Terms of Service
Privacy & Legal
Website Accessibility
LLMs.txt
About Us
Press
Educators
Distributors
Jobs
Gift Cards
"Two aesthetics exist: the passive aesthetic of mirrors and the active aesthetic of prisms"
Jorge Luis Borges
Adafruit Logo
          
A Minority and Woman-owned Business Enterprise (M/WBE)