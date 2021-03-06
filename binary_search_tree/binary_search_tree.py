from dll_stack import Stack
from dll_queue import Queue
# import sys
# sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare the root value to the new value being added
        if self.value >= value:
            # if the value is less than the root, move left
            # if no child on that side insert
            if self.left is None:
                self.left = BinarySearchTree(value)
            # else keeping moving left and call insert again
            else:
                self.left.insert(value)
        # if the value is greater than the root, move right
        elif self.value < value:
            # if the value is greater than the root, move right
            # if no child on that side insert
            if self.right is None:
                self.right = BinarySearchTree(value)
            # else keeping moving left and call insert again
            else:
                self.right.insert(value)

    def contains(self, target):
        # look at the root and compare it to  target
        # if the target is less than the current node value,
        if target < self.value:
            # and can move left and repeat
            if self.left is not None:
                return self.left.contains(target)
            else:
                return False
        # if the target is greater than the current node value move right and repeat
        elif target > self.value:
            if self.right is not None:
                return self.right.contains(target)
            else:
                return False
        # if the target equals the value return true
        elif target == self.value:
            return True
        # if left and right are None return false
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is not None:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        # traverse through BST on every branch until there are no more nodes at left/right
        if self.left is not None:
            self.left.for_each(cb)
        if self.right is not None:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node=None):
        # traverse through BST on every branch until there are no more nodes at left/right
        if self.left is not None:
            self.left.in_order_print()
        print(self.value)
        if self.right is not None:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node=None):
        storage = Queue()
        storage.enqueue(self)

        while(len(storage) > 0):
            node = storage.dequeue()
            print(node.value)
            if node.left:
                storage.enqueue(node.left)
            if node.right:
                storage.enqueue(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node=None):
        storage = Stack()
        storage.push(self)

        while(len(storage) > 0):
            node = storage.pop()
            print(node.value)
            if node.left:
                storage.push(node.left)
            if node.right:
                storage.push(node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node=None):
        print(self.value)
        if self.left:
            self.left.pre_order_dft()
        if self.right:
            self.right.pre_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self, node=None):
        if self.left:
            self.left.post_order_dft()
        if self.right:
            self.right.post_order_dft()
        print(self.value)


root = BinarySearchTree(5)
root.insert(2)
root.insert(3)
root.insert(7)
root.insert(6)
