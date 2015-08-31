import RPi.GPIO as GPIO
import time
import serial

up=5
down=6
right=13
left=19
rclick=26
lclick=21
delaytime = 0.03  # psaxnoume gia to grhgorotero on kai off

ser = serial.Serial('/dev/ttyAMA0', 9600)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(up, GPIO.OUT, initial=0)
GPIO.setup(down, GPIO.OUT, initial=0)
GPIO.setup(right, GPIO.OUT, initial=0)
GPIO.setup(left, GPIO.OUT, initial=0)
GPIO.setup(rclick, GPIO.OUT, initial=0)
GPIO.setup(lclick, GPIO.OUT, initial=0)

while True:

    incoming = ser.readline().strip()
    
    if incoming == 'u':
        GPIO.output(up, 1)
        time.sleep(delaytime)
        GPIO.output(up, 0)
        print('You pressed : %s' % incoming)
    elif incoming == 'd':
        GPIO.output(down,1)
        time.sleep(delaytime)
        GPIO.output(down,0)
        print('You pressed : %s' % incoming)
    elif incoming == 'r':
        GPIO.output(right, 1)
        time.sleep(delaytime)
        GPIO.output(right, 0)
        print('You pressed : %s' % incoming)
    elif incoming == 'l':
        GPIO.output(left, 1)
        time.sleep(delaytime)
        GPIO.output(left, 0)
        print('You pressed : %s' % incoming)
    elif incoming == 'b' :
        GPIO.output(rclick, 1)
        time.sleep(delaytime)
        GPIO.output(rclick, 0)
        print('You pressed : %s' % incoming)
    elif incoming == 'a':
        GPIO.output(lclick, 1)
        time.sleep(delaytime)
        print('You pressed : %s' % incoming)
    elif incoming == 'ur':
        GPIO.output(up, 1)
        GPIO.output(right, 1)
        time.sleep(delaytime)
        GPIO.output(up, 0)
        GPIO.output(right, 0)
        print('You pressed : %s' % incoming)
    elif incoming == 'ul':
        GPIO.output(up, 1)
        GPIO.output(left, 1)
        time.sleep(delaytime)
        GPIO.output(up, 0)
        GPIO.output(left, 0)
        print('You pressed : %s' % incoming)
    elif incoming == 'dr':
        GPIO.output(down, 1)
        GPIO.output(right, 1)
        time.sleep(delaytime)
        GPIO.output(down, 0)
        GPIO.output(right, 0)
        print('You pressed : %s' % incoming)
    elif incoming == 'dl':
        GPIO.output(down, 1)
        GPIO.output(left, 1)
        time.sleep(delaytime)
        GPIO.output(down, 0)
        GPIO.output(left, 0)
        print('You pressed : %s' % incoming)
    else:
        GPIO.output(lclick, 0)
        GPIO.output(up, 0)
        GPIO.output(down, 0)
        GPIO.output(right, 0)
        GPIO.output(left, 0)
        GPIO.output(rclick, 0)
        print('You pressed Nothing')

        

GPIO.cleanup() 




        
    


