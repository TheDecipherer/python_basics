class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) == 0:
            return -1
        print(self.stack[-1])
        del self.stack[-1]

    def peek(self):
        if len(self.stack) == 0:
            return -1
        print(self.stack[-1])

    def is_empty(self):
        if not self.stack:
            return True
        return False


stack = Stack()
stack.push(1)
stack.push(3)
stack.push(5)
stack.peek()
stack.pop()
stack.pop()
stack.peek()
