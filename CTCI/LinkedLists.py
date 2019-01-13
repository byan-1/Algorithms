class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def insertTail(self, data):
        cur = self
        while cur.next != None:
            cur = cur.next
        new = Node(data)
        cur.next = new

def insertHead(head, data):
    new = Node(data)
    new.next = head
    head = new
    return head

def deleteNode(head,data):
    cur = head
    if cur.data == data:
        return head.next

    while cur.next != None:
        if cur.next.data == data:
            cur.next = cur.next.next
            return head
        cur = cur.next
    return head

def printlist(head):
    cur = head
    while cur != None:
        print('{}-->'.format(cur.data), end = '')
        cur = cur.next
    print('None')

def removedups(head):
    seen = {}
    prev = None
    cur = head
    while cur != None:
        if cur.data not in seen:
            seen[cur.data] = 1
            prev = cur
        else:
            prev.next = cur.next
        cur = cur.next
    return head

ll = Node(5)
for i in range(10):
    ll.insertTail(i)
ll.insertTail(11)
ll = insertHead(ll,2)
ll = insertHead(ll, 10)
ll = insertHead(ll, 11)
ll = insertHead(ll,2)
ll = deleteNode(ll, 9)
ll = removedups(ll)
printlist(ll)