import serial 
import pyautogui

print('Press Ctrl-C to quit.')

ser = serial.Serial('/dev/ttyAMA0',9600)


while True:    
                    
    incoming = ser.readline().strip()
    while (len(incoming) == 0):
        incoming = ser.readline().strip()
    
    print('You pressed : %s' % incoming)
                                        
    move = 20
    
    if incoming == b'u':      
        pyautogui.moveRel(None,-move,0)
    elif incoming == b'd':
        pyautogui.moveRel(None,move,0)
    elif incoming == b'r':
        pyautogui.moveRel(move,None,0)
    elif incoming == b'l':
        pyautogui.moveRel(-move,None,0)
    elif incoming == b'a':
        pyautogui.click(button='left')
    elif incoming == b'b':
        pyautogui.click(button='right')
    elif incoming == b'ur':
        pyautogui.moveRel(move,-move,0)
    elif incoming == b'ul':
        pyautogui.moveRel(-move,-move,0)              
    elif incoming == b'dr':
        pyautogui.moveRel(move,move,0)              
    elif incoming == b'dl':
        pyautogui.moveRel(-move,move,0)  
