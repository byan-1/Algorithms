#implement:
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

class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(self.root, val)

    def _insert(self, node, val):
        if val < node.data:
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
        while(len(q) > 0):
            levelNodes = len(q)
            while(levelNodes > 0):
                n = q.dequeue()
                print(n.data, end=' ')
                if n.left != None:
                    q.enqueue(n.left)
                if n.right != None:
                    q.enqueue(n.right)
                levelNodes -= 1
            print('')

    def GetHeight(self):
        if self.root == None:
            return 0
        height = 1
        q = Queue()
        q.enqueue(self.root)
        while(len(q) > 0):
            levelNodes = len(q)
            while(levelNodes > 0):
                n = q.dequeue()
                if n.left != None:
                    q.enqueue(n.left)
                if n.right != None:
                    q.enqueue(n.right)
                levelNodes -= 1
            height += 1
        return height

    def NodeCount(self):
        if self.root == None:
            return 0
        count = 0
        q = Queue()
        q.enqueue(self.root)
        while(len(q) > 0):
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
        print(node.data, end = '')
        if node.left:
            self._preorder(node.left)
        if node.right:
            self._preorder(node.right)

    def IsInTree(self, val):
        return self._IsInTree(self.root, val)

    def _IsInTree(self, node, val):
        if node is None:
            return False
        if node.data == val:
            return True
        if val < node.data:
            return self._IsInTree(node.left, val)
        if val > node.data:
            return self._IsInTree(node.right, val)

    def GetMin(self):
        return self._GetMin(self.root)

    def _GetMin(self, node):
        if node is None:
            return None
        if node.left is not None:
            return self._GetMin(node.left)
        else:
            return node.data

    def GetMax(self):
        return self._GetMax(self.root)

    def _GetMax(self, node):
        if node is None:
            return None
        if node.right is not None:
            return self._GetMax(node.right)
        else:
            return node.data

    def isBST(self):
        return self._isBST(self.root, self.GetMin() - 1, self.GetMax() + 1)

    def _isBST(self, node, min, max):
        if node is None:
            return True
        return node.data > min and node.data < max and self._isBST(node.left, min ,node.data) and self._isBST(node.right, node.data, max)

    def _GetMinNode(self, node):
        if node is None:
            return None
        if node.left is not None:
            return self._GetMinNode(node.left)
        else:
            return node

    def deleteValue(self, val):
        if val < self.root.data:
            self._deleteValue(self.root.left, self.root, val)
        if val > self.root.data:
            self._deleteValue(self.root.right, self.root, val)

    def _deleteValue(self, cur, parent, val):
        if cur is None:
            return False
        if val < cur.data:
            self._deleteValue(cur.left, cur, val)
        if val > cur.data:
            self._deleteValue(cur.right, cur, val)
        if val == cur.data:
            if cur.left is None and cur.right is None:
                if parent.left is cur:
                    parent.left = None
                if parent.right is cur:
                    parent.right = None
            if cur.left is None and cur.right:
                parent.right = cur.right
            if cur.right is None and cur.left:
                parent.left = cur.left
            if cur.left and cur.right:
                min = self._GetMinNode(cur.right)
                cur.data = min.data
                self._deleteValue(cur.right, cur, min.data)

    def _FindVal(self, node, val):
        if val < node.data:
            return self._FindVal(node.left, val)
        if val > node.data:
            return self._FindVal(node.right, val)
        if val == node.data:
            return node

    def getSucc(self, val):
        node = self._FindVal(self.root, val)
        return self._getSucc(self.root, node).data

    def _getSucc(self, root, node):
        if node.right is not None:
            return self._GetMinNode(node.right)
        while root is not None:
            #go down left roots , saving the previous left root as a possible successor until the root becomes smaller than the node, then look in right subtree
            if root.data > node.data:
                succ = root
                root = root.left
            elif root.data < node.data:
                root = root.right
            else:
                return succ

def NodeCountR(node):
    if node is None:
        return 0
    else:
        return 1 + NodeCountR(node.left) + NodeCountR(node.right)

t = Tree()
t.PrintLevelOrder()
t.insert(6)
t.insert(4)
t.insert(5)
t.insert(3)
t.insert(8)
t.insert(7)
t.insert(12)
t.insert(2)
t.insert(1)
t.insert(9)
t.PrintLevelOrder()
print('')
print(t.getSucc(9))
