# Max Feeder

<video autoplay loop muted src="https://user-images.githubusercontent.com/25337335/216802715-1deb94b0-7a2f-4627-93f5-1e41935b5955.mp4">
</video>

## Part Feeding Simplified
### Designed to automate feeding parts for your Open PnP compatible pick and place machine
<br/>

![Max Feeders of multiple widths](/Docs/max-feeder-multiple-widths.jpg)

This feeder is designed to be set up as an AutoFeeder in OpenPNP. It easily clips to 2020 aluminum extrusion and uses an Arduino Mega to receive Gcode commands sent over a USB serial connection in Open PnP. The Max Feeder Shield can control up to 34 feeders.

The design of the Max Feeder is based on [the 0816 feeder design from mgrl.](https://docs.mgrl.de/maschine:pickandplace:feeder:0816feeder) However after two years of development I redesigned every piece of it to improve and simplify the feeder as much as possible.

During development, I also referenced the remix of the 0816 feeder made Nicmoly for the Lumen PNP.

<br/>

# Where can I get a Max Feeder?

[I am selling kits of the Max Feeder Shield and kits of 5x 8mm Max Feeders.](https://store.curlytalegames.com/pages/max-feeders)
> The online store is now live! Thanks for supporting this open hardware project!

This is an Open Hardware project, so all of the design files and the BOM are included in this repo as well.

[If you like what I'm doing consider becoming a Github Sponsor :gift_heart:](https://github.com/sponsors/CurlyTaleGames)

<br/>

# Hardware

![Max Feeder Shield](/Docs/max-front.jpg)

## Max Feeder Shield
- 1 - Max Feeder Shield PCB
- 34 - 4 Pin 2.54mm JST connectors
- 1 - Arduino Mega
- 1 - 10uf Capacitor
- 1 - Barrel Jack
- 1 - 3.81mm Screw Terminal - Optional
- 1 - 6mm Through Hole Tacticle Switch
- 1 - 5v DC 3A (or more) Power Supply
- LOTS of 2.54mm Male Header
- Mounting Bracket in the "3D" folder

<br/>

![Max Feeder 8mm](/Docs/max-feeder-photo.jpg)

## Max Feeder
- 1 - Max Feeder PCB
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
- 1 - [M2 14mm dowel pin](https://www.amazon.com/MroMax-2-5x14mm-Stainless-Rust-Proof-Elements/dp/B07ZF4X7VQ/) or [2mm diameter rod cut to 14mm in length](https://www.amazon.com/dp/B0962RMLVJ)
- [Replacement Pen Springs](https://www.amazon.com/dp/B089JYV7BT)
- [Latex Free Orthodontic Elastics](https://www.amazon.com/dp/B08NCK1K6P)

<br/>

# 3D Prints

![Max Feeder Parts](/Docs/3mf.jpg)

## Max Feeder

Included are two 3MF files which has all the parts oriented and ready to print. Also there are the individual STL files if your slicer doesn't support 3MF files.

The files that need to be printed with a 0.4mm nozzle are labeled, all the other parts can be printed with 0.4mm, 0.6mm, or 0.8mm nozzles. Everything is designed to be printed without supports. If you print with a 0.8mm nozzle you can print a whole feeder in less than 1.5 hours.

[Download the 8mm Max Feeder.](/3D/8mm/) [12mm](/3D/12mm/), [16mm](/3D/16mm/), and [24mm](/3D/24mm/) versions are available in beta status. All of the feeder widths use the same hardware. The only difference between them are the 3D print files.

<br/>

![Max Feeder](/Docs/max-feeder-mount.PNG)

## Max Feeder Shield

Included is a bracket to bolt a Max Feeder Shield + Arduino Mega compatible microcontroller to the side of some 2020 aluminum extrusion. The current bracket was designed to be used with a Lumen PNP but might work for other pick and place machines too.

[Download it here](/3D/Bracket/)

<br/>

# Feeder Assembly & Configuration

- [Uploading Firmware](./Docs/firmware.md)
- [Max Feeder PCB Assembly](./Docs/pcb.md)
- [Servo Poker Assembly](./Docs/poker.md)
- [Tape Gear Motor Assembly](./Docs/motor.md)
- [Final Feeder Assembly](./Docs/finishing-assembly.md)
- [Open PnP AutoFeeder Configuration](./Docs/finishing-assembly.md)
- [Loading and Unloading Tape into Max Feeder](./Docs/finishing-assembly.md)

<br/>

![Max Feeder](/Docs/max-feeder-cad.PNG)

## Troubleshooting

If you are still having problems after going through the "Feeder Assembly & Configuration" [here are some solutions to common problems](./Docs/troubleshooting.md)

## Notes

There are a few optional parts for the feeder you can print.

### QR Code Cap

This part is attached to the front of your feeder and is designed to have a 1/2" x 1/2" QR code stuck onto it. [Atanisoft](https://github.com/atanisoft) and I have been working on [FeederUtils](https://github.com/atanisoft/FeederUtils), which features a way to import and automatically set up part feeders in Open PnP. The QR code portion of the project is still under development.

[Check it out here](https://github.com/atanisoft/FeederUtils)
