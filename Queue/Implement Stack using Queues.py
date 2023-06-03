
# Implimenting stack using Queue.

class MyStack:

    def __init__(self):
        self.Q1 = []

    def push(self, x: int) -> None:
        self.Q1.append(x)

    def pop(self) -> int:
        return self.Q1.pop()

    def top(self) -> int:
        len_q1 = len(self.Q1)
        return self.Q1[len_q1 - 1]

    def empty(self) -> bool:
        return False if self.Q1 else True

    # Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
