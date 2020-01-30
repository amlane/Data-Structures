from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    # enqueue should add an item to the back of the queue.
    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    # dequeue should remove and return an item from the front of the queue.
    def dequeue(self):
        if self.size == 0:
            return
        else:
            self.size -= 1
            return self.storage.remove_from_head()

    # len returns the number of items in the queue
    def __len__(self):
        return self.size
