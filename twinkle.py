#!/usr/bin/env python3
# File name   : servo_twinkle.py
# Description : Move servo to the melody of Twinkle Twinkle Little Star
# Author      : [Your Name]
# Date        : [Today's Date]

import Adafruit_PCA9685
import time

# Initialize the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685(busnum=1)
pwm.set_pwm_freq(60)  # Set frequency to 60Hz

# Define a function to set the servo angle
def set_servo_angle(channel, angle):
    pulse_length = 4096    # The 12-bit resolution of the PWM
    pulse = int((angle * 2.275) + 125)  # Convert angle to pulse length
    pwm.set_pwm(channel, 1, pulse)

# Melody: A list of tuples where each tuple is (angle, duration)
# This is a simplified representation and you can adjust angles and durations
melody = [
    (90, .1), (90, .1), (80, .1), (0, 1), (180, 1), (180, 1), (90, 1),  # Twinkle twinkle little star
    (45, 1), (45, 1), (135, 1), (135, 1), (90, 1),  # How I wonder what you are
    # Repeat or continue the melody as needed
]

channel = 0  # Adjust for your servo's channel

# Play the melody
for angle, duration in melody:
    set_servo_angle(channel, angle)
    time.sleep(duration)
