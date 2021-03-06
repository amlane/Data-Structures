
from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        # a doubly-linked list that holds the key-value entries in the correct order
        self.order = DoublyLinkedList()
        # a storage dict that provides fast access to every node stored in the cache
        self.storage = dict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        # If item with key exists,
        if key in self.storage:
            # return the value and move it to MRU
            self.order.move_to_end(self.storage[key])
            return self.storage[key].value[1]
        # Else return None
        return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        # check if key already exists
        if key in self.storage:
            node = self.storage[key]
            node.value = (key, value)
            return self.order.move_to_end(node)
        elif self.size == self.limit:
            # if at size limit remove LRU from cache
            del self.storage[self.order.head.value[0]]
            # and ordered list
            self.order.remove_from_head()
            # decrease the size of list
            self.size -= 1
        # continue with inserting new item
        # add item to the head of DLL
        self.order.add_to_tail((key, value))
        # store item in dict with key
        self.storage[key] = self.order.tail
        # increase size compile
        self.size += 1
