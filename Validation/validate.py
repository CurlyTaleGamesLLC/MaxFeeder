# this script is for testing a 0816 style feeders
#  
# It requires Open PNP to be open and the camera settings to be adjusted
# so that the tape is white and the tape holes for the parts are below the threshold (black)
# 
# For more accurate measurements increase the size of the camera view in Open PNP
#
# download and install autohotkey and open the "Window Spy" application, you can use
# Window Spy to measure the pixel position on the screen, as well as the pixel color
# for the threshold

# adjust the screenshot region to be around the part you are measuring drift on
# measure distance in pixels between 4mm sprocket holes, mine was 65.8 pixels / mm


import pyautogui
import csv
import keyboard
import time
import serial
import numpy as np


# Set up serial communication
ser = serial.Serial(
    'COM3', 
    baudrate=115200, 
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=1,
    xonxoff=0,
    rtscts=0
    )

ser.setDTR(False)

# Wait for Arduino to initialize
time.sleep(10)

# Clear out unwanted startup serial data
ser.flushInput()
ser.setDTR(True)


# Take a screenshot of a 600x400 pixel section of the screen
def take_screenshot():
    screenshot = pyautogui.screenshot(region=(680, 330, 20, 140))
    return screenshot

# Convert the screenshot to a grayscale image
def convert_to_grayscale(screenshot):
    gray_image = screenshot.convert("L")
    return gray_image

# Find the coordinates of the top and bottom of the part rectangle
def find_black_pixel_height(gray_image):

    height = gray_image.size[1]
    # x = 10
    threshold = 200
    columns = 10

    # Initialize a counter for the height of black pixels


    black_height = []
    top = []
    bottom = []
    center = []

    # Iterate over 10 columns of pixels to surpress noise or other artifacts
    for x in range(columns):
        black_height.append(0)
        top.append(-1)
        bottom.append(-1)
        center.append(-1)
        # Iterate over each pixel in the image
        for y in range(height):
            # Get the pixel value at (x, y)
            pixel = gray_image.getpixel((x, y))
            # If the pixel is below threshold (black), increment the counter
            if pixel < threshold:
                if top[x] == -1:
                    top[x] = y
                black_height[x] += 1
                bottom[x] = y
        center[x] = top[x] + (black_height[x] / 2)

    # print([top, bottom, black_height, center])
    print([np.average(top), np.average(bottom), np.average(black_height), np.average(center)])
    return [np.average(top), np.average(bottom), np.average(black_height), np.average(center)]
    # return [top, bottom, black_height, center]
    

# Calculate the height of the black rectangle in pixels
def calculate_rectangle_height(top, bottom):
    height = bottom - top
    return height

# Log the result to a CSV file
def log_result(top, bottom, height, center):
    with open("results.csv", "a", newline="") as csv_file:
        writer = csv.writer(csv_file)
        log_data =[top, bottom, height, center]
        writer.writerow(log_data)

# Send a message over serial
def send_message(message):
    # ser.write(message.encode())
    ser.write(message)

# Main loop
while True:
    # Check if the space key has been pressed
    if keyboard.is_pressed("space"):
        break

    # Take a screenshot of the screen
    screenshot = take_screenshot()

    # Convert the screenshot to a grayscale image
    gray_image = convert_to_grayscale(screenshot)

    # Find the coordinates of the black rectangle in the grayscale image
    top, bottom, height, center = find_black_pixel_height(gray_image)

    # Log the result to a CSV file
    log_result(top, bottom, height, center)

    # Sleep for 4 seconds
    time.sleep(4)

    # Send a message over serial
    # send_message("M600 N0 F4" + '\r\n')
    ser.write(b'M600 N0 F4\r\n')

    # Sleep for 4 seconds
    time.sleep(4)

# Close the serial connection
ser.close()

print("Script terminated.")
