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








# method 2 - Queue using Linkedlist

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Linkedlist:

    def __init__(self,val):
        node = Node(val)
        self.head = node
        self.tail = node
        self.len = 1

    def print(self):
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next

    def append(self,val):
        node = Node(val)
        self.tail.next = node
        self.tail = node
        self.len += 1

    def pop(self):
        temp = self.head.next
        self.head.next = None
        self.head = temp
        self.len -= 1

linkedlist = Linkedlist(1)
# linkedlist.print()
linkedlist.append(2)
linkedlist.append(3)
linkedlist.append(4)
linkedlist.append(5)
# linkedlist.print()
linkedlist.pop()
linkedlist.print()
