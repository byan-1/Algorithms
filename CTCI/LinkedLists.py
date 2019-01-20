class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __len__(self):
        l = 0
        while self is not None:
            l += 1
            self = self.next
        return l


def insertTail(head, data):
    if head is None:
        return Node(data)
    cur = head
    while cur.next != None:
        cur = cur.next
    new = Node(data)
    cur.next = new
    return head

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




def sumlist(head1,head2, carryover = 0):
    if head1 is None and head2 is None:
        if carryover == 0:
            return None
        else:
            return Node(carryover)
    next1 = None
    next2 = None
    sum = 0
    if head1 is not None:
        sum += head1.data
        next1 = head1.next
    if head2 is not None:
        sum += head2.data
        next2 = head2.next

    sum += carryover
    carryover = sum//10
    val = sum - 10*carryover
    sumnode = Node(val)
    rest = sumlist(next1, next2, carryover)
    sumnode.next = rest
    return sumnode

def sumlist2(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    prev1 = head1
    prev2 = head2
    diff = abs(len(head1) - len(head2))
    if len(head1) > len(head2):
        while diff > 0:
            prev2 = insertHead(prev2,0)
            diff -= 1
    if len(head1) < len(head2):
        while diff > 0:
            prev1 = insertHead(prev1,0)
            diff -= 1
    result = _sumlist2(prev1, prev2)
    if result[1] == 1:
        result[0] = insertHead(result[0], 1)
    return result[0]

def _sumlist2(cur1, cur2):
    if cur1.next is None and cur2.next is None:
        sum = cur1.data + cur2.data
        carryover = sum//10
        val = sum - carryover*10
        sumnode = Node(val)
        return [sumnode, carryover]

    rest = _sumlist2(cur1.next, cur2.next)
    sum = cur1.data + cur2.data + rest[1]
    carryover = sum // 10
    val = sum - carryover * 10
    sumnode = Node(val)
    sumnode.next = rest[0]
    return [sumnode, carryover]

def palindrome(head):
    slow = head
    fast = head
    stack1 = []
    while fast != None and fast.next != None:
        stack1.append(slow.data)
        slow = slow.next
        fast = fast.next.next
    if fast is not None:
        slow = slow.next
    while slow is not None:
        temp = stack1.pop()
        if temp != slow.data:
            return False
        slow = slow.next
    return True

def intersection(head1, head2):
    cur1 = head1
    cur2 = head2
    while cur1.next is not None:
        cur1 = cur1.next
    while cur2.next is not None:
        cur2 = cur2.next
    if cur1 is cur2:
        return True
    return False

def loopdetect(head):
    slow = head
    fast = head
    nodedict = {}
    loop = False
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            loop = True



ll = None
for i in range(0, 10):
    ll = insertTail(ll,i)
for i in range(0, 10):
    ll = insertHead(ll,i)

ll.next.next.next.next.next.next.next.next.next.next.next.next.next = ll.next.next.next.next.next
print(loopdetect(ll))
