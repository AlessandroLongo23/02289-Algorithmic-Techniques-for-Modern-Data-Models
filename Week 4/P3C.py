import random
from Node import Node

class P3C:
    def __init__(self, initial_colors=None, n=0, min_color=1, max_color=2**128):
        self.steps = 0
        
        if initial_colors is None:
            initial_colors = random.sample(range(min_color, max_color + 1), n)

        self.nodes = [P3CNode(color) for color in initial_colors]
            
        for i in range(len(self.nodes)):
            if i > 0:
                self.nodes[i].left = self.nodes[i - 1]
            if i < len(self.nodes) - 1:
                self.nodes[i].right = self.nodes[i + 1]
    
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
            print(self)
            raise ValueError("P3C failed")

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
            if node.left and node.left.key == node.key:
                return False
            if node.right and node.right.key == node.key:
                return False
        return True

    def __str__(self):
        return "--".join([str(node) for node in self.nodes])


class P3CNode(Node):
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
            
        for color in [0, 1, 2]:
            if color not in neighbor_colors:
                if self.key != color:
                    self.newKey = color
                    return True
                break
                
        return False