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

def kthtolast(head, k):
    fwd = head
    count = 0
    while count < k:
        if fwd is None:
            return
        count += 1
        fwd = fwd.next

    cur = head
    while fwd is not None:
        cur = cur.next
        fwd = fwd.next
    print(cur.data)


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

def deletemiddle(node):
    cur = node
    while cur != None:
        if cur.next.next is None:
            cur.next = None
            return
        cur.data = cur.next.data
        cur = cur.next

def partition(head, val):
    part = head
    while part is not None:
        if part.next is None:
            return
        if part.data >= val:
            break
        part = part.next

    cur = part.next
    while cur is not None:
        if cur.data < val:
            cur.data, part.data = part.data, cur.data
            part = part.next
        cur = cur.next
    return head

def sumlist(head1,head2):
    cur1 = head1
    cur2 = head2
    sum = cur1.data + cur2.data
    carryover = sum//10
    val = sum - 10*carryover
    sumlist = Node(val)

    while cur1.next is not None:
        sum = carryover + cur1.data + cur2.data
        carryover = sum//10
        val = sum - 10*carryover
        sumlist.insertTail()










ll = Node(5)
for i in range(10):
    ll.insertTail(i)
ll.insertTail(11)
ll = insertHead(ll,2)
ll = insertHead(ll, 10)
ll = insertHead(ll, 11)
ll = insertHead(ll,2)
ll = deleteNode(ll, 8)
ll = removedups(ll)
printlist(ll)
middle = ll.next.next
ll = partition(ll, 8)
printlist(ll)
kthtolast(ll,2)