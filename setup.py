#!/usr/bin/env python3
# Improved setup.py
# Enhancements include error handling, efficiency, and better user interaction.

import os
import subprocess
import sys

def run_command(command):
    """Run a system command with error handling."""
    try:
        subprocess.check_call(command, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing {command}: {e}", file=sys.stderr)
        sys.exit(1)

def install_packages():
    """Install system and Python packages."""
    print("Updating package lists...")
    run_command("sudo apt-get update")

    # System packages
    sys_packages = [
        "python3-dev", "python3-pip", "libfreetype6-dev", "libjpeg-dev",
        "build-essential", "i2c-tools", "python3-smbus", "util-linux",
        "procps", "hostapd", "iproute2", "iw", "haveged", "dnsmasq"
    ]
    for package in sys_packages:
        run_command(f"sudo apt-get install -y {package}")

    # Python packages
    python_packages = [
        "rpi_ws281x", "mpu6050-raspberrypi", "flask",
        "flask_cors", "websockets", "numpy", "opencv-contrib-python",
        "imutils", "zmq", "pybase64", "psutil"
    ]
    for package in python_packages:
        run_command(f"pip install {package}")

#def configure_i2c():
#    """Enable I2C and configure necessary settings."""
#    print("Configuring I2C...")
#    with open("/boot/config.txt", 'a') as f:
#        f.write("\ndtparam=i2c_arm=on\nstart_x=1\n")

def install_create_ap():
    """Clone and install create_ap."""
    if not os.path.exists("./create_ap"):
        run_command("git clone https://github.com/oblique/create_ap")
    os.chdir("create_ap")
    run_command("sudo make install")
    os.chdir("..")

def configure_startup_script():
    """Configure startup script."""
    startup_script = "/home/pi/startup.sh"
    print(f"Configuring startup script: {startup_script}")
    with open(startup_script, 'w') as file:
        file.write("#!/bin/sh\nsudo python3 server/webServer.py")
    run_command(f"sudo chmod 777 {startup_script}")
    run_command(f"echo '@reboot root {startup_script}' | sudo tee -a /etc/crontab > /dev/null")

def main():
    print("Starting setup...")
    install_packages()
    #configure_i2c()
    install_create_ap()
    configure_startup_script()
    print("Setup completed. It's recommended to reboot your system.")

if __name__ == "__main__":
    main()
