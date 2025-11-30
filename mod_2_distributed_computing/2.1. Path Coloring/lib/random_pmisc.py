import random
from lib.node import Node
from lib.pmisc import PMISC

class RandomPMISC(PMISC):
    """
    RandomPMISC is a distributed algorithm for coloring a path of nodes.
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

        self.nodes: list[RandomPMISCNode] = [RandomPMISCNode(color) for color in initial_colors]
            
        for i in range(len(self.nodes)):
            if i > 0:
                self.nodes[i].left = self.nodes[i - 1]
            if i < len(self.nodes) - 1:
                self.nodes[i].right = self.nodes[i + 1]
    
    """
    Run the RandomPMISC algorithm.
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
            raise ValueError("RandomPMISC failed")

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
    Return a string representation of the RandomPMISC.
    Returns:
        string representation of the RandomPMISC
    """
    def __str__(self) -> str:
        return "--".join([str(node) for node in self.nodes])


class RandomPMISCNode(Node):
    """
    RandomPMISCNode is a node in the RandomPMISC algorithm.
    Args:
        key: the key of the node
    """
    def __init__(self, key: int):
        super().__init__(key)
        self.left: RandomPMISCNode | None = None
        self.right: RandomPMISCNode | None = None
        self.stop: bool = False

    """
    Propose a new color for the node.
    """
    def propose(self):
        if self.stop:
            return
            
        self.newKey = random.randint(0, 2)

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

        if (self.newKey == 1 and 1 not in neighbor_colors) or (self.newKey == 0 and 1 in neighbor_colors):
            self.key = self.newKey
            self.stop = True