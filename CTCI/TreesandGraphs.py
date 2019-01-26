from collections import deque
from collections import defaultdict

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

    def findmin(self):
        if self.left is not None:
            return self.left.findmin()
        else:
            return self

    def delete(self, val):
        if val < self.data:
            self.left._delete(self, val)
        if val > self.data:
            self.left._delete(self, val)
        if val == self.data:
            minnode = self.right.findmin()
            self.data = minnode.data
            self._delete(self, minnode.data)

    def _delete(self, parent, val):
        if self is None:
            return False
        if val < self.data:
            self.left._delete(self, val)
        if val > self.data:
            self.right._delete(self, val)
        if val == self.data:
            if self.left is None and self.right is None:
                parent.left = None
                parent.right = None
            elif self.left is None:
                if parent.left is self:
                    parent.left = self.right
                if parent.right is self:
                    parent.right = self.right
            elif self.right is None:
                if parent.left is self:
                    parent.left = self.left
                if parent.right is self:
                    parent.right = self.left
            else:
                minnode = self.right.findmin()
                self.data = minnode.data
                self.right._delete(self, minnode.data)

def fmn(cur):
    if cur.left is not None:
        return fmn(cur.left)
    else:
        return cur

def deleteNode(cur, parent, val):
    if cur is None:
        return False
    if val < cur.data:
        deleteNode(cur.left, cur, val)
    if val > cur.data:
        deleteNode(cur.right, cur, val)
    if val == cur.data:
        if cur.left is None and cur.right is None:
            if cur is parent.left:
                parent.left is None
            if cur is parent.right:
                parent.right is None
        elif cur.left is None:
            if parent.left is cur:
                parent.left = cur.right
            if parent.right is cur:
                parent.right = cur.right
        elif cur.right is None:
            if parent.left is cur:
                parent.left = cur.left
            if parent.right is cur:
                parent.right = cur.left
        else:
            minnode = fmn(cur.right)
            cur.data = minnode.data
            deleteNode(cur.right, cur, minnode.data)



def printlevelorder(root):
    q = deque()
    q.append(root)
    while len(q) > 0:
        levelnodes = len(q)
        while levelnodes > 0:
            k = q.popleft()
            print(k.data, end = ' ')
            if k.left is not None:
                q.append(k.left)
            if k.right is not None:
                q.append(k.right)
            levelnodes -= 1
        print()


def printpre(curnode):
    if curnode is not None:
        print(curnode.data, end = ' ')
        printpre(curnode.left)
        printpre(curnode.right)

def printiniter(root):
    stack = []
    while len(stack) > 0 or root is not None:
        if root is not None:
            stack.append(root)
            # print(root.data, end=' ')
            root = root.left
        else:
            root = stack.pop()
            # print(root.data, end = ' ')
            root = root.right


def printin(curnode):
    if curnode is not None:
        printin(curnode.left)
        print(curnode.data, end=' ')
        printin(curnode.right)


def minimaltree(l):
    if len(l) % 2 == 1:
        midindex = len(l)//2
    elif len(l) % 2 == 0:
        midindex = len(l)/2 - 1
    t = BSTNode(l[midindex])
    minimaltreehelper(t, l[:midindex])
    minimaltreehelper(t, l[midindex + 1:])
    return t


def minimaltreehelper(t, l):
    if len(l) == 0:
        return
    else:
        if len(l) % 2 == 1:
            midindex = len(l) // 2
        elif len(l) % 2 == 0:
            midindex = len(l)//2 - 1
        t.insert(l[midindex])
        minimaltreehelper(t, l[:midindex])
        minimaltreehelper(t, l[midindex + 1:])

def isbalanced(t):
    q = deque()
    q.append(t)
    lastlvl = False
    pow = 1
    while len(q) > 0:
        if lastlvl is True:
            return False
        levelnodes = len(q)
        if levelnodes < pow:
            lastlvl = True
        while levelnodes > 0:
            cur = q.popleft()
            if cur.left is not None:
                q.append(cur.left)
            if cur.right is not None:
                q.append(cur.right)
            levelnodes -= 1
        pow *= 2
    return True

# def validateBST(root):
#     if root is None:
#         return True
#     if root.left is not None and root.left.data > root.data:


mintree = minimaltree([1,2,3,4,5,6,7,8,9])
mintree.right.left.data = 10
print(validateBST(mintree))
printlevelorder(mintree)

t = BSTNode(12)
t.insert(8)
t.insert(15)
t.insert(1)
t.insert(3)
t.insert(7)
t.insert(5)
t.insert(10)
t.insert(9)
t.insert(20)
t.insert(11)
print(isbalanced(t))


class Graph:
    def __init__(self):
        self.nodes = defaultdict()

    def addNode(self, key):
        self.nodes[key] = []

    def addEdge(self, nodea, nodeb):
        self.nodes[nodea].append(nodeb)

    def addUDEdge(self, nodea, nodeb):
        self.nodes[nodea].append(nodeb)
        self.nodes[nodeb].append(nodea)

class WeightedGraph:
    def __init__(self):
        self.nodes = defaultdict()

    def addNode(self, key):
        self.nodes[key] = defaultdict()

    def addEdge(self, nodea, nodeb, weight):
        self.nodes[nodea][nodeb] = weight

    def addUDEdge(self, nodea, nodeb, weight):
        self.nodes[nodea][nodeb] = weight
        self.nodes[nodeb][nodea] = weight

def DFS(gr, start, visited):
    print(start, end=' ')
    visited.append(start)
    for neighbour in gr.nodes[start]:
        if neighbour not in visited:
            DFS(gr, neighbour, visited)


def BFS(gr, start):
    visited = []
    q = deque()
    q.append(start)
    while len(q) > 0:
        cur = q.popleft()
        if cur not in visited:
            visited.append(cur)
        print(cur, end = ' ')
        for neighbour in gr.nodes[cur]:
            if neighbour not in visited:
                q.append(neighbour)
                visited.append(neighbour)


def isroute(gr, a, b, visited):
    visited.append(a)
    k = False
    for neighbour in gr.nodes[a]:
        if neighbour == b and b not in visited:
            return True
        if neighbour not in visited and k is False:
            k = isroute(gr, neighbour, b, visited)
    return k

g = Graph()
g.addNode('A')
g.addNode('B')
g.addNode('C')
g.addNode('D')
g.addNode('E')
g.addNode('F')
g.addUDEdge('A', 'B')
g.addUDEdge('A', 'C')
g.addUDEdge('B', 'D')
g.addUDEdge('B', 'E')
g.addUDEdge('E', 'F')
g.addUDEdge('C', 'F')
# DFS(g, 'A', [])
# print()
# BFS(g, 'A')

g2 = Graph()
g2.addNode('A')
g2.addNode('B')
g2.addNode('C')
g2.addNode('D')
g2.addNode('E')
g2.addNode('F')
g2.addEdge('A', 'B')
g2.addEdge('A', 'C')
g2.addEdge('B', 'D')
g2.addEdge('B', 'E')
g2.addEdge('E', 'F')
g2.addEdge('C', 'F')
