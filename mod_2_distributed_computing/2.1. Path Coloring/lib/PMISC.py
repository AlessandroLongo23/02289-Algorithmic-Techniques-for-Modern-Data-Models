import random
from lib.Node import Node

class PMISC:
    def __init__(self, initial_colors=None, n=0, min_color=1, max_color=2**16):
        self.steps = 0
        
        if initial_colors is None:
            initial_colors = random.sample(range(min_color, max_color + 1), n)

        self.nodes = [PMISCNode(color) for color in initial_colors]

        for i in range(len(self.nodes)):
            if i > 0:
                self.nodes[i].left = self.nodes[i-1]
            if i < len(self.nodes) - 1:
                self.nodes[i].right = self.nodes[i+1]

    def run(self, debug=False):
        if debug:
            print(self)
        
        while True:
            change = self.propagate()
            if not change:
                break

            self.update()
            self.steps += 1
            if debug:
                print(self)

        if not self.check():
            raise ValueError("PMISC failed")

        return self.steps

    def propagate(self):
        change = False
        for node in self.nodes:
            if node.propagate():
                change = True
        return change

    def update(self):
        for node in self.nodes:
            node.update()

    def check(self):
        for node in self.nodes:
            if node.key == 0:
                if node.left and node.right and node.left.key == 0 and node.right.key == 0:
                    return False
            else:
                if node.left and node.left.key == 1:
                    return False
                if node.right and node.right.key == 1:
                    return False

        return True

    def __str__(self):
        return "--".join([str(node) for node in self.nodes])


class PMISCNode(Node):
    def __init__(self, key):
        super().__init__(key)
        self.left = None
        self.right = None
    
    def propagate(self):
        if not self.isLocalMax():
            return False
            
        neighbor_colors = set()
        if self.left:
            neighbor_colors.add(self.left.key)
        if self.right:
            neighbor_colors.add(self.right.key)
            
        if 1 in neighbor_colors:
            self.newKey = 0
        else:
            self.newKey = 1

        return self.newKey != self.key