#!/usr/bin/env python3
# File name   : set_neutral
# Description : Set servo to neutral position
# Author      : [Your Name]
# Date        : [Today's Date]
import Adafruit_PCA9685
import argparse
import time

# Initialize command line argument parser
parser = argparse.ArgumentParser(description='Set servo to its neutral position.')
parser.add_argument('channel', type=int, help='The channel of the servo (0-15)')
args = parser.parse_args()

# Initialize the PCA9685 using the default address (0x40) and the specified I2C bus.
pwm = Adafruit_PCA9685.PCA9685(busnum=1)
pwm.set_pwm_freq(50)  # Set frequency to 50Hz, good for servos.

def set_servo_angle(channel, angle):
    pulse_length = 4096    # 12-bit
    pulse = int((angle * 2.275) + 125)  # Adjust these values for your servo
    pwm.set_pwm(channel, 0, pulse)

# Set the servo to neutral position (typically 90 degrees)
set_servo_angle(args.channel, 90)

print(f"Set servo on channel {args.channel} to neutral position.")
