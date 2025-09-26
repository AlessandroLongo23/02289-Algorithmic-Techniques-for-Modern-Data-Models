class Node:
    def __init__(self, key):
        self.key = key
        self.newKey = None

    def __str__(self):
        return f"( {self.key} )"

    def isLocalMax(self):
        left_key = self.left.key if self.left else -float('inf')
        right_key = self.right.key if self.right else -float('inf')
        return self.key > left_key and self.key > right_key

    def update(self):
        if self.newKey is not None:
            self.key = self.newKey
            self.newKey = None