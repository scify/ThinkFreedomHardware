import serial
import RPi.GPIO as GPIO
from xbee import XBee

serial_port = serial.Serial('/dev/ttyACM0',9600)
xbee = ZigBee(serial_port)

while True:
    try:
        print xbee.wait_read_frame()
        except KeyboardInterrupt:
            break


serial_port.close()
