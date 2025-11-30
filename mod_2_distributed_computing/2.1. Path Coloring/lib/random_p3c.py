import random
from lib.node import Node
from lib.p3c import P3C

class RandomP3C(P3C):
    """
    RandomP3C is a distributed algorithm for coloring a path of nodes.
    Args:
        initial_colors: list of initial colors for the nodes
        n: number of nodes
        min_color: minimum color
        max_color: maximum color
    """
    def __init__(self, initial_colors: list[int] | None = None, n: int = 0, min_color: int = 1, max_color: int = 2**16):
        self.steps: int = 0
        
        if initial_colors is None:
            initial_colors = random.sample(range(min_color, max_color + 1), n)

        self.nodes: list[RandomP3CNode] = [RandomP3CNode(color) for color in initial_colors]
            
        for i in range(len(self.nodes)):
            if i > 0:
                self.nodes[i].left = self.nodes[i - 1]
            if i < len(self.nodes) - 1:
                self.nodes[i].right = self.nodes[i + 1]
    
    """
    Run the RandomP3C algorithm.
    Args:
        debug: whether to print debug information
    Returns:
        number of steps taken
    """
    def run(self, debug: bool = False) -> int:
        if debug:
            print(self)
        
        while any(node.stop is False for node in self.nodes):
            self.propose()
            self.collapse()
            self.steps += 1
            if debug:
                print(self)

        if not self.check():
            print(self)
            raise ValueError("RandomP3C failed")

        return self.steps

    """
    Propose a new color for the nodes.
    """
    def propose(self):
        for node in self.nodes:
            node.propose()

    """
    Collapse the nodes.
    """
    def collapse(self):
        for node in self.nodes:
            node.collapse()

    """
    Return a string representation of the RandomP3C.
    Returns:
        string representation of the RandomP3C
    """
    def __str__(self) -> str:
        return "--".join([str(node) for node in self.nodes])


class RandomP3CNode(Node):
    """
    RandomP3CNode is a node in the RandomP3C algorithm.
    Args:
        key: the key of the node
    """
    def __init__(self, key: int):
        super().__init__(key)
        self.left: RandomP3CNode | None = None
        self.right: RandomP3CNode | None = None
        self.stop: bool = False

    """
    Propose a new color for the node.
    """
    def propose(self):
        if self.stop:
            return
            
        self.newKey: int = random.choice([0, 1, 2])

    """
    Collapse the node.
    """
    def collapse(self):
        if self.stop:
            return
        
        neighbor_colors: set[int] = set()
        if self.left:
            neighbor_colors.add(self.left.key)
        if self.right:
            neighbor_colors.add(self.right.key)

        if self.newKey not in neighbor_colors:
            self.key = self.newKey
            self.stop = True