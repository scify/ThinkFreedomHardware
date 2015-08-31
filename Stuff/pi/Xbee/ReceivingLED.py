import RPi.GPIO as GPIO
import serial

ser = serial.Serial('/dev/ttyAMA0', 9600)

LED=4

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED, GPIO.OUT)




while True:
    button=ser.readline().strip()
    
    if button == 'a':
          GPIO.output(LED, 1)
    elif button == 'b':
          GPIO.output(LED,0)

GPIO.cleanup()
