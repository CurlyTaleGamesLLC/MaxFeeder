# MAX Feeder Shield

This project is a work in progress, it is not currently in a working state.

This shield is designed to control the [0816 feeders](https://docs.mgrl.de/maschine:pickandplace:feeder:0816feeder:nativeshield) for use with OpenPNP. It plugs into an Arduino Mega and can control up to 34 feeders. 

## Firmware

This shield requires a modified version of the 0816 feeder firmware originally written by mgrl. The firmware is included in this repository.

### Installation

To flash the firmware onto an Arduino Mega you'll need to install the [Arduino IDE](https://www.arduino.cc/en/software)

Open the **"0816feeder.ino"** inside the **"Firmware > 0816feeder"** folder

Go to **"Tools > Manage Libraries"**

Search for **"EEPROMex"** and install the latest version

Connect to the Arduino Mega over serial by going to **"Tools > Port > COMx"** if you're on a Mac or Linux computer it will display the serial port as "/dev/xxxx"

**Press the Upload button** to write the firmware to the Arduino Mega

## Hardware

### MAX Feeder Shield PCB
- 1 - MAX Feeder Shield PCB
- 34 - 4 Pin 2.54mm JST connectors
- 34 - 4 Pin 2.54mm JST cables 30cm in length
- 1 - Arduino Mega
- 1 - 10uf Capacitor
- 1 - Barrel Jack
- 1 - 3.81mm Screw Terminal - Optional
- 1 - 6mm Through Hole Tacticle Switch
- 1 - 5v DC 5A Power Supply
- LOTS of 2.54mm Male Header

### 0816 Feeders

Full list of hardware here
[https://docs.mgrl.de/maschine:pickandplace:feeder:0816feeder:mechanics](https://docs.mgrl.de/maschine:pickandplace:feeder:0816feeder:mechanics)