import serial
import time
 

ser = serial.Serial('/dev/ttyAMA0', 9600)



while True:

    #string = 'Hello from Pi'
    
    #print 'Sending "%s"' % string

   # ser.write('%s\n' % string)
	
   # time.sleep(2)

   incoming = ser.readline().strip()

   print ('Received %s' % incoming)

