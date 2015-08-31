import RPi.GPIO as GPIO
import time
import serial


Button=21
delaytime = 0.03  # psaxnoume gia to grhgorotero on kai off

ser = serial.Serial('/dev/ttyAMA0', 9600)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(Button, GPIO.OUT, initial=0)

while True:

    incoming = ser.readline().strip()
    
    if  incoming == 'a':
        GPIO.output(Button, 1)
        time.sleep(delaytime)
	GPIO.output(Button, 0)
        print('You pressed : %s' % incoming)
    else:
        GPIO.output(Button, 0)
        print('You pressed Nothing')

        

GPIO.cleanup() 




        
    


