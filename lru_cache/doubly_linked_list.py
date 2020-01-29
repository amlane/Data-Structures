class ListNode:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

    def __repr__(self):
        return f"key: {self.key}, value: {self.value}"

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, key, value):
        current_next = self.next
        self.next = ListNode(key, value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, key, value):
        current_prev = self.prev
        self.prev = ListNode(key, value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.key),
            temp = temp.next

    def add_to_head(self, key, value):
        new_node = ListNode(key, value, None, None)
        self.length += 1
        # if list is empty
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def remove_from_head(self):
        key = self.head.key
        self.delete(self.head)
        return key

    def add_to_tail(self, key, value):
        new_node = ListNode(key, value, None, None)
        self.length += 1
        # if list is empty
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_from_tail(self):
        key = self.tail.key
        self.delete(self.tail)
        return key

    def move_to_front(self, node):
        value = node.value
        self.delete(node)
        self.add_to_head(node.key, value)

    def move_to_end(self, node):
        value = node.value
        self.delete(node)
        self.add_to_tail(node.key, value)

    def delete(self, node):
        self.length -= 1
        # only 1 item in the list
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head == node:
            self.head = self.head.next
            node.delete()
        elif self.tail == node:
            self.tail = self.tail.prev
            node.delete()
        else:
            node.delete()

    def get_max(self):
        if not self.head:
            return None
        max_value = self.head.value
        current = self.head
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value
