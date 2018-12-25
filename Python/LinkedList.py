class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def insertHead(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    def size(self):
        current = self.head
        if (self.head == None):
            return 0
        count = 0
        while current != None:
            count = count + 1
            current = current.next
        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.data == item:
                found = True
            else:
                current = current.next
        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.data == item:
                found = True
            else:
                previous = current
                current = current.next

        if previous == None:
            self.head = current.next
        else:
            previous.next = current.next

    def __str__(self):
        current = self.head
        s = ""
        while current != None:
            if current.next != None:
                s += str(current.data) + "-->"
            else:
                s += str(current.data)
            current = current.next
        return s

    def insertTail(self, item):
        current = self.head
        if current == None:
            self.head = Node(item)
        else:
            while current.next != None:
                current = current.next
            current.next = Node(item)

    def insert(self, item, i):
        current = self.head
        previous = None
        count = 0
        if i == 0:
            temp = Node(item)
            temp.next = self.head
            self.head = temp
        else:
            while (count < i and current != None):
                previous = current
                current = current.next
                count += 1
            previous.next = Node(item)
            previous.next.next = current.next

    def index(self, i):
        current = self.head
        count = 0
        while (count < i and current != None):
            current = current.next
            count += 1
        return current.data

    def pop(self):
        current = self.head
        previous = None
        if current == None:
            print("List is empty")
        elif current.next == None:
            self.head = None
            return current.data
        else:
            while current.next != None:
                previous = current
                current = current.next
            previous.setNext(None)
            return current.next

    def slice(self, start, stop):
        count = 0
        current = self.head
        self.length = len
        while(count < start):
            current = current.next
            count += 1
        start = current

        while(count < stop):
            current = current.next
            count += 1
        current.next = None
        l = LinkedList()
        l.head = start
        return l

    def reverse(self):
        if self.head.next.next == None:
            temp = self.head
            self.head = self.head.next
            self.head.next = temp
            return self.head
        else:
            current = self.head
            self.head = current.next
            self.reverse()
            temp = current.next
            temp.next = current
            current.next = None

    def reverseNonRec(self):
        if self.head is None or self.head.next is None:
            return
        prev = self.head
        cur = self.head.next
        next = self.head.next.next
        prev.next = None
        while next.next is not None:
            cur.next = prev
            prev = cur
            cur = next
            next = next.next

        next.next = cur
        self.head = next
        cur.next = prev

#alternatively, middle node jumps once per loop, another node jumps twice. Stop loop when the other node reaches the end.
#or only traverse middle on odd numbers
def middleNode(list):
    size = (list.size()-1)//2
    count = 0
    current = list.head
    while count < size:
        current = current.next
        count += 1
    return current


l = LinkedList()
l.insert(5,0)
l.insertTail(15)
l.insertHead(10)
print(l)
l.reverseNonRec()
print(l)
l.insertHead(1)
l.insertTail(0)
l.insert(3,3)
l.insertTail(12)
l.insertTail(9)
l.insert(4,0)
l.remove(5)
l.insertTail(3)
# print(l)
# print(l)