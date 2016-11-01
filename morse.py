import time
from RPi import GPIO

pinL = 16
pinR = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinL, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pinR, GPIO.IN, pull_up_down=GPIO.PUD_UP)

LEFT = False
RIGHT = True

class CWNode:
   def __init__(self, char):
      self.left = None
      self.right = None
      self.char = char

class CW:
   def __init__(self):
      self.start = CWNode(None)
      self.state = self.start

      # Level 1
      self.start.left = CWNode("E")
      self.start.right = CWNode("T")

      # Level 2
      self.start.left.left = CWNode("I")
      self.start.left.right = CWNode("A")
      self.start.right.left = CWNode("N")
      self.start.right.right = CWNode("M")

      # Level 3
      self.start.left.left.left = CWNode("S")
      self.start.left.left.right = CWNode("U")
      self.start.left.right.left = CWNode("R")
      self.start.left.right.right = CWNode("W")
      self.start.right.left.left = CWNode("D")
      self.start.right.left.right = CWNode("K")
      self.start.right.right.left = CWNode("G")
      self.start.right.right.right = CWNode("O")

      # Level 4
      self.start.left.left.left.left = CWNode("H")
      self.start.left.left.left.right = CWNode("V")
      self.start.left.left.right.left = CWNode("F")
      self.start.left.left.right.right = CWNode(None)
      self.start.left.right.left.left = CWNode("L")
      self.start.left.right.left.right = CWNode(None)
      self.start.left.right.right.left = CWNode("P")
      self.start.left.right.right.right = CWNode("J")
      self.start.right.left.left.left = CWNode("B")
      self.start.right.left.left.right = CWNode("X")
      self.start.right.left.right.left = CWNode("C")
      self.start.right.left.right.right = CWNode("Y")
      self.start.right.right.left.left = CWNode("Z")
      self.start.right.right.left.right = CWNode("Q")
      self.start.right.right.right.left = CWNode(None)
      self.start.right.right.right.right = CWNode(None)

      # Level 5
      self.start.left.left.left.left.left = CWNode("5")
      self.start.left.left.left.left.right = CWNode("4")
      self.start.left.left.left.right.right = CWNode("3")
      self.start.left.left.right.right.right = CWNode("2")
      self.start.left.right.left.right.left = CWNode("+")
      self.start.left.right.right.right.right = CWNode("1")
      self.start.right.left.left.left.left = CWNode("6")
      self.start.right.left.left.left.right = CWNode("=")
      self.start.right.left.left.right.left = CWNode("/")
      self.start.right.right.left.left.left = CWNode("7")
      self.start.right.right.right.left.left = CWNode("8")
      self.start.right.right.right.right.left = CWNode("9")
      self.start.right.right.right.right.right = CWNode("0")

   def traverse(self, direction):
      if direction:
         self.state = self.state.right
      else:
         self.state = self.state.left

      if self.state.right == None:
         print(self.state.char)
         self.state = self.start

   def reset(self):
      self.state = self.start

   def flush(self):
      print(self.state.char)
      self.reset()

morse = CW()
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
