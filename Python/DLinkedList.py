class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
        self.back = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

    def setBack(self, newback):
        self.back = newback

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        current = self.head
        while(current.getNext != None):
            current = current.getNext
        self.tail = current