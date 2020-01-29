
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
        self.storage = DoublyLinkedList()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        node = self.storage.head
        while(node):
            # If item with key exists,
            if node.key == key:
                # return the value and move it to MRU
                self.storage.move_to_end(node)
                return node.value
            else:
                # Otherwise keep checking until the end of the list
                node = node.next
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
        node = self.storage.head
        while(node):
            if node.key == key:
                # if the key exists, update the value
                node.value = value
                # update to MRU
                return self.storage.move_to_end(node)
            else:
                # Otherwise keep checking until the end of the list
                node = node.next
        # If key doesn't exist...
        # check if list is at it's max size
        if self.size == self.limit:
            # remove the oldest entry in the cache
            self.storage.remove_from_head()
            # then add the new item to the head
            return self.storage.add_to_tail(key, value)
        else:
            # increment the size counter
            self.size += 1
            # add the item to the head
            return self.storage.add_to_tail(key, value)
