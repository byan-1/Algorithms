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

class Stack:
    def __init__(self):
        self.head = None

    def push(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def pop(self):
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
                s += str(current.getData()) + "->"
            else:
                s += str(current.getData())
            current = current.getNext()
        return s

s = Stack()
s.push(5)
s.push(7)
s.push(3)
print(s)
s.pop()
print(s)
print(s.peek())