import random
from lib.node import Node

class P3C:
    """
    P3C is a distributed algorithm for coloring a path of nodes.
    Args:
        initial_colors: list of initial colors for the nodes
        n: number of nodes
        min_color: minimum color
        max_color: maximum color
    """
    def __init__(self, initial_colors: list[int] | None = None, n: int = 0, min_color: int = 1, max_color: int = 2**128):
        self.steps: int = 0
        
        if initial_colors is None:
            initial_colors = random.sample(range(min_color, max_color + 1), n)

        self.nodes: list[P3CNode] = [P3CNode(color) for color in initial_colors]
            
        for i in range(len(self.nodes)):
            if i > 0:
                self.nodes[i].left = self.nodes[i - 1]
            if i < len(self.nodes) - 1:
                self.nodes[i].right = self.nodes[i + 1]
    
    """
    Run the P3C algorithm.
    Args:
        debug: whether to print debug information
    Returns:
        tuple containing the final state of the nodes and the number of steps taken
        final state of the nodes: list of P3CNode objects
        number of steps taken: int
    """
    def run(self, debug: bool = False) -> tuple[list[P3CNode], int]:
        if debug: print(self)
        
        while True:
            change: bool = self.propagate()
            if not change:
                break

            self.update()
            self.steps += 1
            if debug: print(self)

        if not self.check():
            print(self)
            raise ValueError("P3C failed")

        return self.nodes, self.steps

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
            if node.left and node.left.key == node.key:
                return False
            if node.right and node.right.key == node.key:
                return False
        return True

    """
    Return a string representation of the P3C.
    Returns:
        string representation of the P3C
    """
    def __str__(self) -> str:
        return "--".join([str(node) for node in self.nodes])


class P3CNode(Node):
    """
    P3CNode is a node in the P3C algorithm.
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
            
        for color in [0, 1, 2]:
            if color not in neighbor_colors:
                if self.key != color:
                    self.newKey = color
                    return True
                break
                
        return False

    def __str__(self) -> str:
        return f"( {self.key} )"