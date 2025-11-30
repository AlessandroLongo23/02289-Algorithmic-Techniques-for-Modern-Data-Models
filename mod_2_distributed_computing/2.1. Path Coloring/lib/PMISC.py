import random
from lib.node import Node

class PMISC:
    """
    PMISC is a distributed algorithm for coloring a path of nodes.
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

        self.nodes: list[PMISCNode] = [PMISCNode(color) for color in initial_colors]

        for i in range(len(self.nodes)):
            if i > 0:
                self.nodes[i].left = self.nodes[i-1]
            if i < len(self.nodes) - 1:
                self.nodes[i].right = self.nodes[i+1]

    """
    Run the PMISC algorithm.
    Args:
        debug: whether to print debug information
    Returns:
        number of steps taken
    """
    def run(self, debug: bool = False) -> int:
        if debug:
            print(self)
        
        while True:
            change: bool = self.propagate()
            if not change:
                break

            self.update()
            self.steps += 1
            if debug:
                print(self)

        if not self.check():
            raise ValueError("PMISC failed")

        return self.steps

    """
    Propagate the colors through the nodes.
    Returns:
        whether any node changed its color
    """
    def propagate(self) -> bool:
        change: bool = False
        for node in self.nodes:
            if node.propagate():
                change = True
        return change

    """
    Update the nodes.
    """
    def update(self):
        for node in self.nodes:
            node.update()

    """
    Check if the nodes are colored correctly.
    Returns:
        whether the nodes are colored correctly
    """
    def check(self) -> bool:
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

    """
    Return a string representation of the PMISC.
    Returns:
        string representation of the PMISC
    """
    def __str__(self) -> str:
        return "--".join([str(node) for node in self.nodes])


class PMISCNode(Node):
    """
    PMISCNode is a node in the PMISC algorithm.
    Args:
        key: the key of the node
    """
    def __init__(self, key: int):
        super().__init__(key)
        self.left = None
        self.right = None
    
    """
    Propagate the colors through the node.
    Returns:
        whether the node changed its color
    """
    def propagate(self) -> bool:
        if not self.isLocalMax():
            return False
            
        neighbor_colors: set[int] = set()
        if self.left:
            neighbor_colors.add(self.left.key)
        if self.right:
            neighbor_colors.add(self.right.key)
            
        if 1 in neighbor_colors:
            self.newKey = 0
        else:
            self.newKey = 1

        return self.newKey != self.key