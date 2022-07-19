# MAX Feeder & MAX Feeder Shield

This project is a work in progress.

![Max Feeder Shield Front](/Docs/max-front.jpg)

![Max Feeder Shield Back](/Docs/max-back.jpg)

![Max Feeder](/Docs/MaxFeeder.JPG)

This feeder is designed to be set up as an Auto Feeder in OpenPNP. I designed it to mount to a Lumen PNP. It uses an Arduino Mega which listens to GCODE sent over a USB serial connection in Open PNP. The Max Feeder Shield can control up to 34 feeders.

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

### MAX Feeder Shield PCB
- 1 - MAX Feeder Shield PCB
- 34 - 4 Pin 2.54mm JST connectors
- 34 - [4 Pin 2.54mm JST cables 100cm in length ("stepper motor cable")](https://www.amazon.com/Wires-Motor-XH2-54-4P-PH2-0-6P-Printers-Accessories%EF%BC%8C3D/dp/B08PV6XGK2/)
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
- 4 - [3M 6mm screws](https://www.amazon.com/Alloy-Steel-Socket-Screws-Black/dp/B00W8YSCIS/)
- 3 - [3M 20mm screws](https://www.amazon.com/Prime-Line-9180478-Socket-Screws-10-Pack/dp/B07D5S3154/)
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

Included is a 3MF file which as all the parts oriented and ready to print in one file, or if your slicer doesn't support 3MF included are the individual STL files.

These files were designed to be printed with a standard 0.4mm nozzle, and without supports.

# Feeder Assembly

![Pressure Arm](/Docs/assembly_01_pressure_arm.jpg)
Connect the Pressure Arm onto Feeder Base. Slide Pen Spring and 3D printed washer onto M3 20mm screw. Screw the Pressure Arm onto Feeder Base. Don't screw it in all the way, the Pressure Arm should be able to move up and down.

![Servo Poker Arm](/Docs/assembly_02_servo_poker.jpg)
From the servo kit, cut the servo horn at the third hole with some side cutters. Use one of the servo kit screws into the 2nd hole to attach it to the poker arm, and an M3 6mm screw assemble the Poker Arm as shown. The screws should be loose enough that the pieces of the poker arm can still move. Using a knife, cut the tip of the Poker Arm. Push the 2mm diameter rod through the Poker Arm.

![Servo and Pressure Arm](/Docs/assembly_03_poker_pressure.jpg)
Using an M3 6mm screw, screw the right side of the Servo to the Feeder Base. Slide the Poker arm into the feeder base.

![Tape Motor](/Docs/assembly_04_tape_motor.jpg)
Using two M3 20mm screws, the N20 geared DC motor, and 3d printed tape gear parts assemble as shown. The 8 tooth gear has a keyed side and a round side, make sure the keyed side slides onto the motor shaft. 

**PRO TIP:** It's a good idea to not fully tighten the 20mm screws down, when you run the motor the gears need to be broken in. Let it run for a min, then tighten it down. Also don't manually turn the gear on the motor, you can strip out the key gears.

![Sub Assemblies](/Docs/assembly_05_pcb_motor.jpg)
Using an M3 6mm screw attach the tape motor sub assembly to the feeder base. Slide the Feeder PCB into the Feeder Base. Route the wires around the servo, and then back up through the slot on the right as shown.

![Tape Lever](/Docs/assembly_06_lever.jpg)
Slide the lever 3d print onto the Feeder Base. Loop a Latex-Free Orthodontic Neon Elastic onto the hook on the lever and the hook on the Feeder Base.

![Max Feeder Assembled](/Docs/assembly_07_max_feeder.jpg)
Using three M3 6mm screws attach the Feeder Cover to the Feeder Base, don't over tighten, you are threading into plastic. And that's it! You're done!