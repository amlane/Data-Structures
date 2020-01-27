from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')

# LIFO Last in first out


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    # should add item to end of stack
    def push(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    # should remove last item in stack

    def pop(self):
        if self.size == 0:
            return
        else:
            self.size -= 1
            return self.storage.remove_from_tail()

    def len(self):
        return self.size
