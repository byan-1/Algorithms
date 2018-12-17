# implement:
# insert // insert value into tree
#  get_node_count // get count of values stored
#  print_values // prints the values in the tree, from min to max
#  is_in_tree // returns true if given value exists in the tree
#  get_height // returns the height in nodes (single node's height is 1)
#  get_min // returns the minimum value stored in the tree
#  get_max // returns the maximum value stored in the tree
#  is_binary_search_tree
#  delete_value
#  get_successor // returns next-highest value in tree after given value, -1 if none
class Queue:
    def __init__(self):
        self.list = []

    def enqueue(self, val):
        self.list.append(val)

    def dequeue(self):
        if len(self.list) == 0:
            return None
        temp = self.list[0]
        del self.list[0]
        return temp

    def __len__(self):
        return len(self.list)

class Tree:
    def __init__(self, initdata):
        self.data = initdata
        self.left = None
        self.right = None

    def insert(self, node, val):
        if val < self.data:
            if node.left == None:
                node.left = Node(val)
            else:
                self._insert(node.left, val)
        if val > node.data:
            if node.right == None:
                node.right = Node(val)
            else:
                self._insert(node.right, val)

    def PrintLevelOrder(self):
        if self.root == None:
            print('')
            return

        q = Queue()
        q.enqueue(self.root)
        while (len(q) > 0):
            levelNodes = len(q)
            while (levelNodes > 0):
                n = q.dequeue()
                print(n.data, end=' ')
                if n.left != None:
                    q.enqueue(n.left)
                if n.right != None:
                    q.enqueue(n.right)
                levelNodes -= 1
            print('')

    def NodeCount(self):
        if self.root == None:
            return 0
        count = 0
        q = Queue()
        q.enqueue(self.root)
        while (len(q) > 0):
            n = q.dequeue()
            count += 1
            if n.left != None:
                q.enqueue(n.left)
            if n.right != None:
                q.enqueue(n.right)
        return count

    def preorder(self):
        self._preorder(self.root)

    def _preorder(self, node):
        print(node.data, end='')
        if node.left:
            self._preorder(node.left)
        if node.right:
            self._preorder(node.right)


def NodeCountR(node):
    if node is None:
        return 0
    else:
        return 1 + NodeCountR(node.left) + NodeCountR(node.right)
