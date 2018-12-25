class Stack:
    def __init__(self):
        self.s = []

    def isEmpty(self):
        return len(self.s) == 0

    def push(self, c):
        self.s.append(c)

    def pop(self):
        temp = self.s[len(self.s) - 1]
        del self.s[len(self.s) - 1]
        return temp

def balanced(string):
    s = Stack()
    for char in string:
        if char == "(":
            s.push("(")
        if char == ")":
            if s.isEmpty():
                return False
            s.pop()
    return s.isEmpty()
