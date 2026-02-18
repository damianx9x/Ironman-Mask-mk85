# Adafruit RP2040 Prop-Maker Feather

## Overview

![](https://cdn-learn.adafruit.com/assets/assets/000/121/720/medium800/adafruit_products_5768-05.jpg?1686337581)

The Adafruit Feather series gives you lots of options for a small, portable, rechargeable microcontroller board. By picking a Feather and stacking on a FeatherWing you can create advanced projects quickly. One popular combo is the Adafruit [Feather M4](https://www.adafruit.com/product/3857) or [Feather RP2040](https://www.adafruit.com/product/4884) with a [Prop-Maker FeatherWing](https://www.adafruit.com/product/3988) on top to create animatronics or props that boot up instantly and can drive LEDs, and small speakers.

![](https://cdn-learn.adafruit.com/assets/assets/000/121/721/medium800/adafruit_products_5768-02.jpg?1686337671)

We've used the Prop-Maker FeatherWing to make lots of li'l robots, swords, and other prop projects. However, what if we made it _even easier_ for people to make props? What if we made it so many projects can be built with minimal or no soldering at all? Yeah that would be pretty nice!

Thus, the creation of the Feather P2040 Prop-Maker: an all-in-one combination of the [Feather RP2040](https://www.adafruit.com/product/4884) with a [Prop-Maker FeatherWing](https://www.adafruit.com/product/3988), with a few tweaks based on feedback from expert prop-builders. Perfect for fitting into your next prop build! This Feather will unlock the prop-maker inside all of us, with tons of stuff packed in to make sabers and swords, props, toys, cosplay pieces, and more.

![](https://cdn-learn.adafruit.com/assets/assets/000/121/723/medium800/adafruit_products_5768-01.jpg?1686337832)

We looked at hundreds of prop builds, and thought about what would make for a great low-cost (but well-designed) add-on for our Feather boards. Here's what we came up with:

- **Terminal Block NeoPixel Port -** With easy-to-use screw terminals you can quickly connect and disconnect your NeoPixel strips and rings. This port provides high current drive from either the Feather Lipoly or USB port, whichever is higher. A 5V level up-shifter gives you a clean voltage signal to reduce glitchiness no matter what chip you're using. You can also cut power to the entire strip instantly to reduce quiescent power, thanks to a separate control transistor.
- **MAX98357 I2S 3 Watt Class D Audio Amplifier** - Drive any 4-8Ω speaker, up to 3 Watts, for sound effects. Audio comes out on two of the terminal blocks so you can screw in any wires to a speaker you like - [we're partial to this small 3W speaker](https://www.adafruit.com/product/3968) with pre-attached wires. [Thanks to the I2S digital inputs](https://www.adafruit.com/product/3006), you'll get excellent audio quality
- **Triple-Axis Accelerometer with Tap Detection** - The LIS3DH is our favorite accelerometer, you can use this for detection motion, tilt, or taps. [Here's an example of a lightsaber that makes sounds when swung or hit.](https://learn.adafruit.com/hallowing-lightsaber) We have code for this chip in both Arduino and CircuitPython.
- **Extra Button or Output Pin** - One more pin on the terminal screw block can be used for button input or digital output, for activation or a simple LED.
- **Servo Connection** - [Plug any hobby servo with 3 wires](https://www.adafruit.com/search?q=servo) into the 0.1" spaced header, and you can have quick motion control.
- **Low power mode!** The power system for the NeoPixels and speaker amplifier can be controlled by a pin to cut power to them, so you have lower power usage when the prop is in sleep or off mode (but can wake up fast by listening to the button press or accelerometer data).

![](https://cdn-learn.adafruit.com/assets/assets/000/121/724/medium800/adafruit_products_5768-06.jpg?1686337904)

At the Feather's heart is an RP2040 chip, clocked at 133 MHz and at 3.3V logic, the same one used in the [Raspberry Pi Pico](https://www.adafruit.com/product/4864). This chip has a whopping 8 MB of onboard QSPI FLASH and 264K of RAM! There's even room left over for a STEMMA QT connector for plug-and-play of I2C devices.

To make it easy to use for portable projects, we added a connector for any of our 3.7V Lithium polymer batteries and built in battery charging. You don't need a battery, it will run just fine straight from the USB Type C connector. But, if you do have a battery, you can take it on the go, then plug in the USB to recharge. The Feather will automatically switch over to USB power when it's available.

![](https://cdn-learn.adafruit.com/assets/assets/000/121/722/medium800/adafruit_products_5768-04.jpg?1686337732)

 **Here're some handy specs! You get:**

- Measures 52.1mm x 22.8mm x 12.2mm / 2.1" x 0.9" x 0.5 without headers soldered in
- Light as a (large?) feather - ~7grams
- RP2040 32-bit Cortex M0+ dual core running at ~133 MHz @ 3.3V logic and power
- 264 KB RAM
- **8 MB SPI FLASH** chip for storing files, images, and CircuitPython/MicroPython code storage. No EEPROM
- **Tons of GPIO! 21 x GPIO pins with following capabilities:**
  - **Four** 12-bit ADCs (one more than Pico)
  - Two I2C, Two SPI, and two UART peripherals, we label one for the 'main' interface in standard Feather locations
  - 16 x PWM outputs - for servos, LEDs, etc

- **Built-in 200mA+ lipoly charger** with charging status indicator LED
- **Pin #13 red LED** for general purpose blinking
- **RGB NeoPixel** for full-color indication.
- On-board **STEMMA QT connector** that lets you quickly connect any Qwiic, STEMMA QT or Grove I2C devices with no soldering!
- **Both Reset button and Bootloader select button for quick restarts** (no unplugging-replugging to relaunch code)
- **USB Type C connector** lets you access built-in ROM USB bootloader and serial port debugging
- 3.3V regulator with 500mA peak current output and power enable pin
- 4 mounting holes
- 12 MHz crystal for perfect timing.
- **Prop-Making section with I2S 3W audio amplifier, 5V NeoPixel level shifting, accelerometer, servo port, and terminal blocks for fast solder-free connections.**

Comes assembled and tested, with some header. You'll need a soldering iron to attach the header if you'd like to use it on a breadboard!

- [Next Page](https://learn.adafruit.com/adafruit-rp2040-prop-maker-feather/pinouts.md)

## Primary Products

### Adafruit RP2040 Prop-Maker Feather with I2S Audio Amplifier

[Adafruit RP2040 Prop-Maker Feather with I2S Audio Amplifier](https://www.adafruit.com/product/5768)
The Adafruit Feather series gives you lots of options for a small, portable, rechargeable microcontroller board. By picking a feather and stacking on a FeatherWing you can create advanced projects quickly. One popular combo is our [Feather M4](https://www.adafruit.com/product/3857)...

In Stock
[Buy Now](https://www.adafruit.com/product/5768)
[Related Guides to the Product](https://learn.adafruit.com/products/5768/guides)

## Related Guides

- [PropMaker Jack O'Lantern](https://learn.adafruit.com/propmaker-jack-o-lantern.md)
- [Guitar Synth with CircuitPython SynthIO](https://learn.adafruit.com/guitar-synth-with-circuitpython-synthio.md)
- [Prop-Maker Feather Talking Adabot Clock](https://learn.adafruit.com/prop-maker-feather-talking-adabot-clock.md)
- [Lightsaber Prop-Maker RP2040](https://learn.adafruit.com/lightsaber-rp2040.md)
- [Gravity Falls Memory Gun](https://learn.adafruit.com/gravity-falls-memory-gun.md)
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