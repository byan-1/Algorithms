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

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self,item):
        temp = Node(item)
        if self.head == None:
            self.head = temp
            self.tail = temp
            self.head.next = None
        else:
            self.tail.next = temp
            self.tail = temp

    def dequeue(self):
        current = self.head
        previous = None
        if current == None:
            print("List is empty")
        else:
            self.head = current.getNext()
            return current.getData()

    def peek(self):
        return self.head.getData()

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def __str__(self):
        current = self.head
        s = ""
        while current != None:
            if current.getNext() != None:
                s += str(current.getData()) + "<--"
            else:
                s += str(current.getData())
            current = current.getNext()
        return s

q = Queue()
q.enqueue(5)
q.enqueue(7)
q.enqueue(3)
print(q)
q.dequeue()
print(q)