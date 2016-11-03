import pygame
from pygame.locals import *
import time, sys, threading, Queue
from array import array

class CWNode:
    def __init__(self, char):
        self.dit = None
        self.dah = None
        self.char = char

class CWAudio(threading.Thread, pygame.mixer.Sound):
    def __init__(self, notificationQ):
        super(CWAudio, self).__init__()

        # worker init
        self.notificationQ = notificationQ
        self.stopRequest = threading.Event()

        # sound init
        pygame.mixer.pre_init(44100, -16, 1, 1024)
        pygame.init()
        pygame.mixer.Sound.__init__( self, buffer=self.getToneBuffer() )
        self.set_volume(0.75)

    def run(self):
        while not self.stopRequest.isSet():
            try:
                cmd = self.notificationQ.get(True, 0.05)
                if cmd == 'DAH':
                    self.playDah()
                elif cmd == 'DIT':
                    self.playDit()
            except Queue.Empty:
                continue

    def getToneBuffer(self):
        period = 110
        samples = array("h", [0] * period)
        amplitude = 2 ** ( abs( pygame.mixer.get_init()[1] ) - 1 ) - 1
        for time in xrange(period):
            if time < period / 2:
                samples[time] = amplitude
            else:
                samples[time] = -amplitude
        return samples

    def playDah(self):
        self.play( -1 )
        time.sleep( 0.30 )
        self.stop()
        time.sleep( 0.02 )

    def playDit(self):
        self.play( -1 )
        time.sleep( 0.10 )
        self.stop()
        time.sleep( 0.02 )

class CWTree:
    DIT = False
    DAH = True
    def __init__(self):
        self.start = CWNode( None )
        self.state = self.start
        self.frequency = 650

        # Level 1
        self.start.dit = CWNode("E")
        self.start.dah = CWNode("T")

        # Level 2
        self.start.dit.dit = CWNode("I")
        self.start.dit.dah = CWNode("A")
        self.start.dah.dit = CWNode("N")
        self.start.dah.dah = CWNode("M")

        # Level 3
        self.start.dit.dit.dit = CWNode("S")
        self.start.dit.dit.dah = CWNode("U")
        self.start.dit.dah.dit = CWNode("R")
        self.start.dit.dah.dah = CWNode("W")
        self.start.dah.dit.dit = CWNode("D")
        self.start.dah.dit.dah = CWNode("K")
        self.start.dah.dah.dit = CWNode("G")
        self.start.dah.dah.dah = CWNode("O")

        # Level 4
        self.start.dit.dit.dit.dit = CWNode("H")
        self.start.dit.dit.dit.dah = CWNode("V")
        self.start.dit.dit.dah.dit = CWNode("F")
        self.start.dit.dit.dah.dah = CWNode(None)
        self.start.dit.dah.dit.dit = CWNode("L")
        self.start.dit.dah.dit.dah = CWNode(None)
        self.start.dit.dah.dah.dit = CWNode("P")
        self.start.dit.dah.dah.dah = CWNode("J")
        self.start.dah.dit.dit.dit = CWNode("B")
        self.start.dah.dit.dit.dah = CWNode("X")
        self.start.dah.dit.dah.dit = CWNode("C")
        self.start.dah.dit.dah.dah = CWNode("Y")
        self.start.dah.dah.dit.dit = CWNode("Z")
        self.start.dah.dah.dit.dah = CWNode("Q")
        self.start.dah.dah.dah.dit = CWNode(None)
        self.start.dah.dah.dah.dah = CWNode(None)

        # Level 5
        self.start.dit.dit.dit.dit.dit = CWNode("5")
        self.start.dit.dit.dit.dit.dah = CWNode("4")
        self.start.dit.dit.dit.dah.dah = CWNode("3")
        self.start.dit.dit.dah.dah.dah = CWNode("2")
        self.start.dit.dah.dit.dah.dit = CWNode("+")
        self.start.dit.dah.dah.dah.dah = CWNode("1")
        self.start.dah.dit.dit.dit.dit = CWNode("6")
        self.start.dah.dit.dit.dit.dah = CWNode("=")
        self.start.dah.dit.dit.dah.dit = CWNode("/")
        self.start.dah.dah.dit.dit.dit = CWNode("7")
        self.start.dah.dah.dah.dit.dit = CWNode("8")
        self.start.dah.dah.dah.dah.dit = CWNode("9")
        self.start.dah.dah.dah.dah.dah = CWNode("0")

        # Start Audio
        self.alertQ = Queue.Queue()
        self.speaker = CWAudio( self.alertQ )
        self.speaker.start()
        

    def traverse(self, direction):
        if self.state == None:
            return
        if direction and self.state.dah != None:
            self.state = self.state.dah
            self.alertQ.put('DAH')
        elif self.state.dit != None:
            self.state = self.state.dit
            self.alertQ.put('DIT')
            
    def reset(self):
        self.state = self.start
        
    def flush(self):
        if self.state.char != None:
            sys.stdout.write( self.state.char )
            sys.stdout.flush()
        self.reset()
