# MAX Feeder & MAX Feeder Shield

This project is a work in progress.

![Max Feeder Shield](/Docs/max-front.jpg)

![Max Feeder 8mm](/Docs/max-feeder-photo.jpg)

![Max Feeder](/Docs/max-feeder-cad.PNG)

This feeder is designed to be set up as an AutoFeeder in OpenPNP. I designed it to mount to a Lumen PNP. It uses an Arduino Mega which listens to GCODE sent over a USB serial connection in Open PNP. The Max Feeder Shield can control up to 34 feeders.

I originally based this design on [the 0816 feeder design from mgrl.](https://docs.mgrl.de/maschine:pickandplace:feeder:0816feeder:nativeshield)

I'd also like to give a shout out to Nicmoly for making a Lumen PNP Remix of the 0816 feeder.

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

### MAX Feeder Shield
- 1 - MAX Feeder Shield PCB
- 34 - 4 Pin 2.54mm JST connectors
- 1 - Arduino Mega
- 1 - 10uf Capacitor
- 1 - Barrel Jack
- 1 - 3.81mm Screw Terminal - Optional
- 1 - 6mm Through Hole Tacticle Switch
- 1 - 5v DC 3A (or more) Power Supply
- LOTS of 2.54mm Male Header
- Mounting Bracket in the "3D" folder

### MAX Feeder
- 1 - MAX Feeder PCB
- 3D printed files in the "3D" folder
- 5 - [M3 6mm screws](https://www.amazon.com/Alloy-Steel-Socket-Screws-Black/dp/B00W8YSCIS/)
- 1 - [4 Pin 2.54mm JST cables 100cm in length ("stepper motor cable")](https://www.amazon.com/Wires-Motor-XH2-54-4P-PH2-0-6P-Printers-Accessories%EF%BC%8C3D/dp/B08PV6XGK2/)
- 3 - [M3 20mm screws](https://www.amazon.com/Prime-Line-9180478-Socket-Screws-10-Pack/dp/B07D5S3154/)
- 1 - [SPDT Limit Switch](https://www.amazon.com/dp/B088W8WMTB)
- 1 - [1N4001 Diode](https://www.amazon.com/MCIGICM-Rectifier-Electronic-Silicon-Doorbell/dp/B071YWNBVM/)
- 1 - [5 pin 2.54mm Angled Male Header](https://www.amazon.com/Antrader-2-54mm-Right-Header-Connector/dp/B07M88GRHG/)
- 1 - [2 pin 2.54mm Female header cable](https://www.amazon.com/Mayata-Female-Jumper-Dupont-Printer/dp/B07H1WDN3R/) or [Female to Female Dupont cables](https://www.amazon.com/EDGELEC-Breadboard-1pin-1pin-Connector-Multicolored/dp/B07GCZVCGS/)
- 1 - [N20 Geared DC Motor 60 RPM](https://www.aliexpress.com/item/3256803042731079.html?pdp_ext_f=%7B"sku_id":"12000024757391447"%7D)
- 1 - [9G SG90 Servo](https://www.amazon.com/Dorhea-Helicopter-Airplane-Walking-Compatible/dp/B08FJ27Q1H/)
- 1 - [2mm diameter rod cut to 12mm in length](https://www.amazon.com/dp/B0962RMLVJ)
- [Replacement Pen Springs](https://www.amazon.com/dp/B089JYV7BT)
- [Latex Free Orthodontic Elastics](https://www.amazon.com/dp/B08NCK1K6P)


## 3D Prints

![Max Feeder Parts](/Docs/3mf.jpg)

Included are two 3MF files which has all the parts oriented and ready to print. Also there are the individual STL files if your slicer doesn't support 3MF files.

The files that need to printed with a 0.4mm nozzle are labeled, all the other parts can be printed with 0.4mm, 0.6mm, or 0.8mm nozzles. Everything is designed to be printed without supports.

# Feeder Assembly Documentation

- [PCB Assembly](./Docs/pcb.md)
- [Servo Poker Assembly](./Docs/poker.md)
- [Tape Gear Motor Assembly](./Docs/motor.md)
- [Final Feeder Assembly](./Docs/finishing-assembly.md)



# Open PnP AutoFeeder Configuration

### Documentation for this is coming soon