class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, val):
        if val < self.data:
            if self.left is not None:
                self.left.insert(val)
            else:
                self.left = BSTNode(val)
        if val > self.data:
            if self.right is not None:
                self.right.insert(val)
            else:
                self.right = BSTNode(val)


    def delete(self, val):

    def __str__(self):



class Graph:
    def __init__(self):
        self.nodes = []

class GraphNode:
    def __init__(self, key):
        self.key = key
        self.neighbours = []

