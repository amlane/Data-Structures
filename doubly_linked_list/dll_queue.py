from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')

# FIFO First in first out


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
    # enqueue should add an item to the back of the queue.

    def enqueue(self, value):
        self.size += 1
        DoublyLinkedList.add_to_tail(self, value)
    # dequeue should remove and return an item from the front of the queue.

    def dequeue(self):
        self.size -= 1
        return DoublyLinkedList.remove_from_head(self)
    # len returns the number of items in the queue

    def len(self):
        return self.size
