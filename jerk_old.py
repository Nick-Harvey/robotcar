#!/usr/bin/env python3
# File name   : servo_swing.py
# Description : Moves servo up and down 30 degrees from neutral position as fast as it can
# Author      : [Your Name]
# Date        : [Today's Date]
import Adafruit_PCA9685
import argparse
import time

# Initialize command line argument parser
parser = argparse.ArgumentParser(description='Move servo up and down 30 degrees from neutral position rapidly.')
parser.add_argument('channel', type=int, help='The channel of the servo (0-15)')
args = parser.parse_args()

# Initialize the PCA9685 using the default address (0x40) and the specified I2C bus.
pwm = Adafruit_PCA9685.PCA9685(busnum=1)
pwm.set_pwm_freq(50)  # Set frequency to 50Hz, good for servos.

def set_servo_angle(channel, angle):
    # Using the pulse calculation method that was confirmed to work
    pulse = int((angle * 2.275) + 125)
    pwm.set_pwm(channel, 0, pulse)

def swing_servo(channel):
    central_position = 90
    up_position = central_position + 30  # 120 degrees
    down_position = central_position - 30  # 60 degrees
    
    while True:  # Infinite loop to continuously swing the servo
        set_servo_angle(channel, up_position)  # Move servo up
        time.sleep(0.5)  # Adjust this delay as needed
        set_servo_angle(channel, down_position)  # Move servo down
        time.sleep(0.5)  # Adjust this delay as needed

# Start swinging the servo on the specified channel
swing_servo(args.channel)

print(f"Swinging servo on channel {args.channel} up and down 30 degrees from neutral position.")
