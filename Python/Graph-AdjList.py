from collections import deque
import pythonds
#add_edge: add edge between 2 vertices
#remove_edge: remove edge between 2 vertices
#edges: returns edges of the graph
#vertices: returns a list of all vertices of the graph
#add vertex: adds a vertex to the graph
#remove vertex: removes all references to that vertex
#Implement DFS and BFS.
#Check for cycle
#Topological sort
#Count connected components
#List strongly connected components
#Check for bipartite graph
#Single source shortest path (Dijkstra)
#Minimum spanning tree

class Node:
    def __init__(self, key):
        self.key = key
        self.neighbours = {}
        self.visited = 0
        self.processed = 0
        self.hasIncEdge = 0
        self.inbound = 0
        self.color = None

    def addNeighbour(self, neighbour, weight = 0):
        self.neighbours[neighbour] = weight

    def getNeighbours(self):
        return self.neighbours

    def deleteOutgoing(self):
        self.neighbours = {}

class Graph:
    def __init__(self):
        self.nodeDict = {}

    def incomingEdges(self):
        for node in self.nodeDict.values():
            for elem in node.neighbours:
                self.nodeDict[elem].inbound += 1

    def addEdge(self, key1, key2, weight=0):
        self.nodeDict[key1].addNeighbour(key2, weight)

    def getEdges(self):
        edges = {}
        for key in self.nodeDict:
            edges[key] = self.nodeDict[key].getNeighbours()
        return edges

    def noIncEdges(self):
        self.resetIncEdges()
        outgoing = []
        for node in self.nodeDict.values():
            for neighbour in node.neighbours:
                self.nodeDict[neighbour].hasIncEdge = 1

        for key, node in self.nodeDict.items():
            if node.hasIncEdge == 0:
                outgoing.append(node)
        return outgoing


    def addNode(self, key):
        newNode = Node(key)
        self.nodeDict[key] = newNode

    def getNodes(self):
        return list(self.nodeDict.keys())

    def __str__(self):
        print("Nodes: {}".format(self.showNodes))
        print("Edges: {}".format(self.showEdges))

    def resetVisited(self):
        for key in self.nodeDict:
            self.nodeDict[key].visited = 0
            self.nodeDict[key].processed = 0
            self.nodeDict[key].color = None

    def resetIncEdges(self):
        for key in self.nodeDict:
            self.nodeDict[key].hasIncEdge = 0



def BFS(graph, root):
    q = deque()
    rootnode = graph.nodeDict[root]
    q.append(rootnode)
    while len(q) != 0:
        cur = q.popleft()
        cur.visited = 1
        print(cur.key, end = ' ')
        for key in cur.neighbours:
            if graph.nodeDict[key].visited == 0:
                q.append(graph.nodeDict[key])
                graph.nodeDict[key].visited = 1
    print('\n')

def DFS(graph, root):
    def _DFS(graph, node):
        print(node.key, end = ' ')
        node.visited = 1
        for key in node.neighbours:
            if graph.nodeDict[key].visited == 0:
                _DFS(graph, graph.nodeDict[key])

    graph.resetVisited()
    _DFS(graph, graph.nodeDict[root])
    print('\n')

def findCycle(graph):
    def _DFS(graph, node):
        node.visited = 1
        node.onStack = 1
        for key in node.neighbours:
            if graph.nodeDict[key].visited == 0:
                _DFS(graph, graph.nodeDict[key])
            if graph.nodeDict[key].onStack == 1:
                return True
        node.onStack = 0
        return False

    outgoing = graph.noIncEdges()
    if len(outgoing) == 0:
        return True
    graph.resetVisited()
    return _DFS(graph, outgoing[0])


def topologicalSort(graph):
    topsorted = []
    if findCycle(graph):
        return topsorted

    processNext = deque()
    graph.incomingEdges()
    for node in graph.nodeDict.values():
        if node.inbound == 0:
            processNext.append(node)

    while len(processNext) > 0:
        outgoing = processNext.popleft()
        for key in outgoing.neighbours:
            graph.nodeDict[key].inbound -= 1
        for key in outgoing.neighbours:
            if graph.nodeDict[key].inbound == 0:
                processNext.append(graph.nodeDict[key])
        topsorted.append(outgoing.key)
    return topsorted

def _DFS(graph, node):
    print(node.key, end = ' ')
    node.visited = 1
    for key in node.neighbours:
        if graph.nodeDict[key].visited == 0:
            _DFS(graph, graph.nodeDict[key])

def find_connected(graph):
    graph.resetVisited()
    for node in graph.nodeDict.values():
        if node.visited == 0:
            _DFS(graph, node)
            print('\n')


def checkBipartite(graph, root):
    q = deque()
    graph.resetVisited()
    rootnode = graph.nodeDict[root]
    q.append(rootnode)
    rootnode.color = 'b'
    while len(q) != 0:
        cur = q.popleft()
        cur.visited = 1
        for key in cur.neighbours:
            if graph.nodeDict[key].color == cur.color:
                print('Not Bipartite')
                return
            if cur.color == 'b':
                graph.nodeDict[key].color = 'r'
            elif cur.color == 'r':
                graph.nodeDict[key].color = 'b'
            if graph.nodeDict[key].visited == 0:
                q.append(graph.nodeDict[key])
                graph.nodeDict[key].visited = 1
    print('Bipartite')


def strongCons(graph, root):
    def _DFS(graph, node):
        print(node.key, end = ' ')
        node.visited = 1
        for key in node.neighbours:
            if graph.nodeDict[key].visited == 0:
                _DFS(graph, graph.nodeDict[key])

    graph.resetVisited()
    _DFS(graph, graph.nodeDict[root])
    print('\n')


def listConv(graph, root):
    l = []
    for key,val in graph.nodeDict.items():
        for nodekey, weight in val.neighbours.items():
            l.append([key,nodekey,weight])
    return l

def kruskal(l, n):
    s = sorted(l, key = lambda x: x[2])
    k = UnionFind(s, len(s), n)
    e = k.id
    w = [x[2] for x in s]
    f = [e[i] + [w[i]] for i in range (0, len(s))]
    result = []
    i = 0
    while len(result) < n - 1:
        x = k.findParent(e[i][0])
        y = k.findParent(e[i][1])
        if x != y:
            result.append(f[i])
            k.union(e[i][0], e[i][1])
        i += 1
    print(k.parent)
    return result


class UnionFind:
    def __init__(self, l, n, nodecount):
        self.parent = []
        for i in range(nodecount):
            self.parent.append(i)
        self.id = []
        for i in range(n):
            self.id.append([])
        self.convert(l)

    def union(self,edge1,edge2):
        parentedge1 = self.findParent(edge1)
        parentedge2 = self.findParent(edge2)
        self.parent[parentedge2] = parentedge1

    def findParent(self, nodeid):
        if self.parent[nodeid] != nodeid:
            self.parent[nodeid] = self.findParent(self.parent[nodeid])
        return self.parent[nodeid]

    def convert(self, l):
        k = 0
        for elem in l:
            for i in range(2):
                if elem[i] == 'A':
                    self.id[k].append(0)
                if elem[i] == 'B':
                    self.id[k].append(1)
                if elem[i] == 'C':
                    self.id[k].append(2)
                if elem[i] == 'D':
                    self.id[k].append(3)
                if elem[i] == 'E':
                    self.id[k].append(4)
                if elem[i] == 'F':
                    self.id[k].append(5)
                if elem[i] == 'G':
                    self.id[k].append(6)
            k += 1


gr = Graph()
gr.addNode('a')
gr.addNode('b')
gr.addNode('c')
gr.addNode('d')
gr.addNode('e')
gr.addNode('f')
gr.addNode('g')
gr.addNode('h')
# gr.addEdge('a', 'c')
# gr.addEdge('c', 'a')
gr.addEdge('a', 'b')
gr.addEdge('b', 'a')
gr.addEdge('d', 'c')
gr.addEdge('c', 'd')
gr.addEdge('e', 'c')
gr.addEdge('c', 'e')
gr.addEdge('d', 'e')
gr.addEdge('e', 'd')
# gr.addEdge('a', 'd')
# gr.addEdge('d', 'a')
gr.addEdge('f', 'e')
gr.addEdge('e', 'f')
gr.addEdge('d', 'f')
gr.addEdge('f', 'd')
gr.addEdge('e', 'g')
gr.addEdge('g', 'e')
gr.addEdge('f', 'g')
gr.addEdge('g', 'f')
gr.addEdge('b', 'h')
gr.addEdge('h', 'b')



gr = Graph()
gr.addNode('a')
gr.addNode('b')
gr.addNode('c')
gr.addNode('d')
gr.addNode('e')
gr.addNode('f')
gr.addNode('g')
gr.addNode('h')
gr.addEdge('a', 'b')
gr.addEdge('a', 'c')
gr.addEdge('d', 'c')
gr.addEdge('e', 'c')
gr.addEdge('d', 'e')
gr.addEdge('a', 'd')
gr.addEdge('f', 'e')
gr.addEdge('d', 'f')
gr.addEdge('e', 'g')
gr.addEdge('f', 'g')
gr.addEdge('b', 'h')
# gr.addEdge('h', 'a')


w = Graph()
w.addNode('A')
w.addNode('B')
w.addNode('C')
w.addNode('D')
w.addNode('E')
w.addNode('F')
w.addNode('G')
w.addEdge('A', 'B', 1)
w.addEdge('A','F', 3)
w.addEdge('A','G', 2)
w.addEdge('B', 'C', 2)
w.addEdge('B', 'F', 1)
w.addEdge('C', 'D', 6)
w.addEdge('D','E',3)
w.addEdge('D','F',3)
w.addEdge('E','F',4)
w.addEdge('E','G', 1)
w.addEdge('F','G',1)
l=listConv(w,'A')
print(kruskal(l, 7))