
class Stack:
    def __init__(self):
        self.stack = []
        self.len = 0

    def print(self):
        if self.len == 0:
            return False
        else:
            return (self.stack)

    def pop(self):
        if self.len == 0:
            return False
        else:
            a = self.stack.pop()
            return a

    def add_element(self, int):
        self.stack.append(int)
        self.len += 1
        return True


stack1 = Stack()
print(stack1.add_element(5))
stack1.add_element(2)
print(stack1.print())
print(stack1.pop())
print(stack1.print())

