class MinStack:
    def __init__(self):
        self.a = []
        self.min_stack = []

    # @param x, an integer
    def push(self, x):
        if len(self.min_stack) == 0:
            self.min_stack.append(x)
        elif x <= self.min_stack[-1]:
            self.min_stack.append(x)
        self.a.append(x)

    # @return nothing
    def pop(self):
        if len(self.a) != 0:
            popped = self.a.pop()
            if popped == self.min_stack[-1]:
                self.min_stack.pop()

    # @return an integer
    def top(self):
        if len(self.a) != 0:
            return self.a[-1]
        else:
            return -1

    # @return an integer
    def getMin(self):
        if len(self.min_stack) != 0:
            return self.min_stack[-1]
        else:
            return -1

m = MinStack()
print(m.push(4))
print(m.getMin())
print(m.push(3))
print(m.getMin())

print(m.pop())
print(m.getMin())
print(m.pop())
print(m.getMin())
print(m.top())