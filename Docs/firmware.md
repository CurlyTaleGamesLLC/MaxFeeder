# Max Feeder Shield Firmware

To use the Max Feeder Shield you'll need to upload the latest firmware onto an Arduino Mega. 

If you purchase the Max Feeder Shield + Microcontroller from [store.curlytalegames.com](https://store.curlytalegames.com/pages/max-feeders) you can skip this, it comes pre-loaded with the latest firmware. 
> The online store is almost ready, hang tight! It'll be open very soon

I have included a modified version the 0816 feeder firmware originally written by mgrl in this repository. I added support for things like Software Servo control, and auto detaching for servos so they don't burn themselves out.

[You can find it located here.](/Firmware/0816feeder/)

<br/>

## Installation

To flash the firmware onto an Arduino Mega you'll need to install the [Arduino IDE](https://www.arduino.cc/en/software)

Open the **"0816feeder.ino"** inside the **"Firmware > 0816feeder"** folder

Go to **"Tools > Manage Libraries"**

Search for **"EEPROMex"** and install the latest version

Search for **"SoftServo" by AlexGyver** and install the latest version

Connect to the Arduino Mega over serial by going to **"Tools > Port > COMx"** if you're on a Mac or Linux computer it will display the serial port as "/dev/xxxx"

**Press the Upload button** to write the firmware to the Arduino Mega

<br/>

### [Next Step: Max Feeder PCB Assembly](pcb.md)

