class CWNode:
    def __init__(self, char):
        self.left = None
        self.right = None
        self.char = char

class CWTree:
    LEFT = False
    RIGHT = True
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
        if self.state == None:
            return
        if direction and self.state.right != None:
            self.state = self.state.right
        elif self.state.left != None:
            self.state = self.state.left
            
    def reset(self):
        self.state = self.start
        
    def flush(self):
        if self.state.char != None:
            print(self.state.char)
        self.reset()