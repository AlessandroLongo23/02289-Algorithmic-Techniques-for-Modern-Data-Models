import random
from lib.Node import Node
from lib.P3C import P3C

class RandomP3C(P3C):
    def __init__(self, initial_colors=None, n=0, min_color=1, max_color=2**16):
        self.steps = 0
        
        if initial_colors is None:
            initial_colors = random.sample(range(min_color, max_color + 1), n)

        self.nodes = [RandomP3CNode(color) for color in initial_colors]
            
        for i in range(len(self.nodes)):
            if i > 0:
                self.nodes[i].left = self.nodes[i - 1]
            if i < len(self.nodes) - 1:
                self.nodes[i].right = self.nodes[i + 1]
    
    def run(self, debug=False):
        if debug:
            print(self)
        
        while any(node.stop == False for node in self.nodes):
            self.propose()
            self.collapse()
            self.steps += 1
            if debug:
                print(self)

        if not self.check():
            print(self)
            raise ValueError("RandomP3C failed")

        return self.steps

    def propose(self):
        for node in self.nodes:
            node.propose()

    def collapse(self):
        for node in self.nodes:
            node.collapse()

    def __str__(self):
        return "--".join([str(node) for node in self.nodes])


class RandomP3CNode(Node):
    def __init__(self, key):
        super().__init__(key)
        self.left = None
        self.right = None
        self.stop = False

    def propose(self):
        if self.stop:
            return
            
        self.newKey = random.randint(0, 2)

    def collapse(self):
        if self.stop:
            return
        
        neighbor_colors = set()
        if self.left:
            neighbor_colors.add(self.left.key)
        if self.right:
            neighbor_colors.add(self.right.key)

        if self.newKey not in neighbor_colors:
            self.key = self.newKey
            self.stop = True