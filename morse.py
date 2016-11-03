import time, sys
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
keyUpStart = 0.0
spaceTimerStart = 0.0

def bumpLeftCheck(reading):
   if ( leftSwitch and not reading ):
      morse.traverse(morse.DIT)

def bumpRightCheck(reading):
   if ( rightSwitch and not reading ):
      morse.traverse(morse.DAH)

def timeCapture(readLeft, readRight):
   global keyUpStart
   global spaceTimerStart
   if ( readLeft and readRight and ( not leftSwitch or not rightSwitch ) ):
      keyUpStart = spaceTimerStart = time.time()

if __name__ == "__main__":
   print("Ready!")
   while True:
      readLeft = GPIO.input(pinL)
      readRight = GPIO.input(pinR)
      timeCapture(readLeft, readRight)
      bumpLeftCheck(readLeft)
      bumpRightCheck(readRight)
      leftSwitch = readLeft
      rightSwitch = readRight
      if ( keyUpStart > 0.0 and time.time() - keyUpStart > 1.00 ):
         morse.flush()
         keyUpStart = 0.0
      if ( spaceTimerStart > 0.0 and time.time() - spaceTimerStart > 2.00 ):
         sys.stdout.write( ' ' )
         sys.stdout.flush()
         spaceTimerStart = 0.0
      time.sleep(0.01)
