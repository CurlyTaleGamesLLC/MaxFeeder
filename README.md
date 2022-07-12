# MAX Feeder & MAX Feeder Shield

This project is a work in progress.

![Max Feeder](/Docs/MaxFeeder.JPG)

This feeder is designed to be set up as an Auto Feeder in OpenPNP. I designed it to mount to a Lumen PNP. It uses an Arduino Mega which listens to GCODE sent over a USB serial connection in Open PNP. The Max Feeder Shield can control up to 34 feeders.

I originally based this design on [the 0816 feeder design from mgrl.](https://docs.mgrl.de/maschine:pickandplace:feeder:0816feeder:nativeshield)

I'd also like to give a should to Nicmoly for making a Lumen PNP Remix of the 0816 feeder.

## Firmware

This shield requires a modified version of the 0816 feeder firmware originally written by mgrl. The firmware is included in this repository.

### Installation

To flash the firmware onto an Arduino Mega you'll need to install the [Arduino IDE](https://www.arduino.cc/en/software)

Open the **"0816feeder.ino"** inside the **"Firmware > 0816feeder"** folder

Go to **"Tools > Manage Libraries"**

Search for **"EEPROMex"** and install the latest version

Search for **"SoftServo" by AlexGyver** and install the latest version

Connect to the Arduino Mega over serial by going to **"Tools > Port > COMx"** if you're on a Mac or Linux computer it will display the serial port as "/dev/xxxx"

**Press the Upload button** to write the firmware to the Arduino Mega

## Hardware

### MAX Feeder Shield PCB
- 1 - MAX Feeder Shield PCB
- 34 - 4 Pin 2.54mm JST connectors
- 34 - 4 Pin 2.54mm JST cables 100cm in length ("stepper motor cable")
- 1 - Arduino Mega
- 1 - 10uf Capacitor
- 1 - Barrel Jack
- 1 - 3.81mm Screw Terminal - Optional
- 1 - 6mm Through Hole Tacticle Switch
- 1 - 5v DC 5A Power Supply
- LOTS of 2.54mm Male Header

### MAX Feeder
- 1 - MAX Feeder PCB
- 3D printed files in the "3D" folder
- - FeederPokerPETG.3mf must be printed in PETG
- 4 - 3M 6mm screws
- 3 - 3M 20mm screws
- 1 - [SPDT Limit Switch](https://www.amazon.com/dp/B088W8WMTB)
- 1 - 1N4001 Diode
- 1 - 5 pin 2.54mm Angled Male Header
- 1 - 2 pin 2.54mm Female header cable
- 1 - N20 Geared DC Motor 60 RPM
- 1 - 9G SG90 Servo
- 1 - [2mm diameter rod cut to 12mm in length](https://www.amazon.com/dp/B0962RMLVJ)
- [Replacement Pen Springs](https://www.amazon.com/dp/B089JYV7BT)
- [Latex Free Orthodontic Elastics](https://www.amazon.com/dp/B08NCK1K6P)
