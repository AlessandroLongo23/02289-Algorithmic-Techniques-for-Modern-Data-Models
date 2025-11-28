import random
from lib.P3C import P3CNode, P3C

class FastP3C(P3C):
    def __init__(self, initial_colors: list[int] | None = None, n: int = 0, min_color: int = 1, max_color: int = 2**16):
        self.steps: int = 0
        
        if initial_colors is None:
            initial_colors: list[int] = random.sample(range(min_color, max_color + 1), n)

        self.nodes: list[FastP3CNode] = [FastP3CNode(color) for color in initial_colors]
            
        for i in range(len(self.nodes)):
            if i > 0:
                self.nodes[i].left = self.nodes[i - 1]
            if i < len(self.nodes) - 1:
                self.nodes[i].right = self.nodes[i + 1]
    
    def run(self, debug: bool = False) -> int:
        if debug:
            print(self)

        for i in range(7):
            self.propagate()
            self.update()
            self.steps += 1
            if debug and i < 6:
                print(self)

        self.p3c = P3C([node.key for node in self.nodes])
        self.steps += self.p3c.run(debug=debug)

        if not self.check():
            print(self)
            raise ValueError("FastP3C failed")

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

    def __str__(self):
        return "--".join([str(node) for node in self.nodes])


class FastP3CNode(P3CNode):
    def __init__(self, key):
        super().__init__(key)

    def getBin(self, n=128):
        return bin(self.key)[2:].zfill(n)

    def propagate(self):
        if not self.right:
            right = FastP3CNode(self.key - 1)
        else:
            right = self.right

        x = self.getBin()
        y = right.getBin()

        index = None
        value = None
        for i in range(127, -1, -1):
            if x[i] != y[i]:
                index = 127 - i
                value = int(x[i])
                break
            
        self.newKey = 2 * index + value

        if self.newKey != self.key:
            return True
        return False
        
