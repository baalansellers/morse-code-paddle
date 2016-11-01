import time
from CWTree import CWTree
from RPi import GPIO

pinL = 16
pinR = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinL, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pinR, GPIO.IN, pull_up_down=GPIO.PUD_UP)

morse = CWTree()
leftSwitch = True
rightSwitch = True
keyUpStart = 0
keyUpEnd = 0

def bumpLeftCheck(reading):
   if ( leftSwitch and not reading ):
      morse.traverse(LEFT)

def bumpRightCheck(reading):
   if ( rightSwitch and not reading ):
      morse.traverse(RIGHT)

def timeCapture(readLeft, readRight):
   if ( readLeft and readRight and ( not leftSwitch or not rightSwitch ) ):
      keyUpStart = time.time()
   if ( not readLeft and leftSwitch or not readRight and rightSwitch ):
      keyUpEnd = time.time()

if __name__ == "__main__":
   #morse.traverse(LEFT)
   #morse.traverse(LEFT)
   #morse.traverse(LEFT)
   #morse.traverse(LEFT)
   #morse.traverse(LEFT)
   while True:
      readLeft = GPIO.input(pinL)
      readRight = GPIO.input(pinR)
      timeCapture(readLeft, readRight)
      bumpLeftCheck(readLeft)
      bumpRightCheck(readRight)
      leftSwitch = readLeft
      rightSwitch = readRight
      if keyUpEnd - keyUpStart > 0.15:
         morse.flush()
      #print("Left: HIGH" if reading else "Left: LOW")
      #print("Right: HIGH" if reading else "Right: LOW")
      time.sleep(1)
