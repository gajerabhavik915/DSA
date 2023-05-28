# method - 1. implement queue through array.

class array_queue:
    def __init__(self):
        self.list1 = []
        self.len = 0

    def print_queue(self):
        if self.list1:
            # for i in self.list1:
            #     print(i)
            print(self.list1)
            return True
        else:
            return False

    def add_element(self, val):
        self.list1.append(val)
        self.len += 1
        return True

    def pop_left(self):
        a = self.list1.pop(0)
        self.len -= 1
        return a

queue = array_queue()
queue.print_queue()
queue.add_element(1)
queue.add_element(2)
queue.add_element(3)
queue.add_element(4)
queue.print_queue()
queue.pop_left()
queue.print_queue()
