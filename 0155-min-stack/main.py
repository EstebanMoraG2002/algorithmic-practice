class MinStack:
    def __init__(self):
        self.st = []
        self.mn = []

    def push(self, val):
        self.st.append(val)
        if not self.mn:
            self.mn.append(val)
        else:
            self.mn.append(min(val, self.mn[-1]))

    def pop(self):
        self.st.pop()
        self.mn.pop()

    def top(self):
        return self.st[-1]

    def getMin(self):
        return self.mn[-1]


if __name__ == "__main__":
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    print(stack.getMin())  # -3
    stack.pop()
    print(stack.top())     # 0
    print(stack.getMin())  # -2
