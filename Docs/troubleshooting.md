# Max Feeder Troubleshooting Guide

## Servo Not Ratcheting Tape

There can be a few reasons why the tape isn't being pushed forward. Here a few things to check:

* Make sure The tip of the poker is sharp and pointy. Cut it with a sharp fresh knife blade. This should not be an issue with the new PCB poker tips.
* If the tape moves back and forth when the servo actuates, make sure to tighten the screw on the top front of the Max Feeder to put pressure on the tape.
* If the servo actuates but the tape doesn't move, loosen the screw on the top front of the Max Feeder.


## Tape Gears Binding

There are a couple things that could bind the gears, here are a few things that have happened and how to fix it.

### Loose Part Jammed in Gears
After doing a lot of test feeds I had a 0805 resistor get stuck to the adhesive on the cover tape. The resistor somehow made it all the way back to the tape gears and jammed them. Unscrew the idler gear and pull out the n20 motor to remove the loose part. Under normal opperation this wouldn't happen. The pick and place machine would pick up the part so you wouldn't have loose parts.

### Excessive Pressure on Idler Gear

![](troubleshooting/scraping.jpg)

One user reported that the M3 20mm screw was putting exessive pressure on the idler gear causing the motor to bind. In order for the gears to hold the tape, the M3 20mm screw needs to be very close to the n20 motor. It's normal for the head of the M3 20mm screw to scrape on the side of the motor, but the gears should be able to turn.

![](troubleshooting/drill-file.jpg)
![](troubleshooting/filed-screw.jpg)

What fixed it was filing down the head of the screw. Wrap the threads of the screw with some tape, and put it in a drill chuck and press it against the file.

