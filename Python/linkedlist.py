class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def __str__(self):
        current = self.head
        s = ""
        while current != None:
            if current.getNext() != None:
                s += str(current.getData()) + "-->"
            else:
                s += str(current.getData())
            current = current.getNext()
        return s

    def append(self, item):
        current = self.head
        if current == None:
            self.head = Node(item)
        else:
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(Node(item))

    def insert(self, item, i):
        current = self.head
        previous = None
        count = 0
        if (i == 0):
            temp = Node(item)
            temp.setNext(self.head)
            self.head = temp
        else:
            while (count < i and current != None):
                previous = current
                current = current.getNext()
                count += 1
            previous.setNext(Node(item))
            previous.getNext().setNext(current)

    def index(self, i):
        current = self.head
        count = 0
        while (count < i and current != None):
            current = current.getNext()
            count += 1
        return current.getData()

    def pop(self):
        current = self.head
        previous = None
        if current == None:
            print("List is empty")
        elif current.getNext() == None:
            self.head = None
            return current.getData()
        else:
            while current.getNext() != None:
                previous = current
                current = current.getNext()
            previous.setNext(None)
            return current.getData()

    def slice(self, start, stop):
        count = 0
        current = self.head
        self.length = len
        while(count < start):
            current = current.getNext()
            count += 1
        start = current

        while(count < stop):
            current = current.getNext()
            count += 1
        current.setNext(None)
        l = LinkedList()
        l.head = start
        return l

if(__name__ == '__main__'):
    l = LinkedList()
    l.insert(5,0)
    l.append(15)
    l.add(5)
    l.add(1)
    l.append(0)
    l.insert(3,3)
    print(l)
    print(l.slice(2,4))