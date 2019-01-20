class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self,data):
        self.stack1.append(data)

    def dequeue(self):
        self.shiftstacks()
        return self.stack2.pop()

    def shiftstacks(self):
        if len(self.stack1) > 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())



q = MyQueue()
for i in range(10):
    q.enqueue(i)
print(q)
print(q.dequeue())
print(q.dequeue())

