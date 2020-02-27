import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

        # LEFT CASE
        # check if our new nodes value is less than the current nodes value
          # does it have a child to the left?
            # place our new node here
            # otherwise
          # repeat process for the left
    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
          if not self.left:
            node = BinarySearchTree(value)
            self.left = node
          else:
            self.left.insert(value)
        
        # RIGHT CASE
        # check if the new nodes value is greater than or equal to the current nodes value
            # does it have a child to the right?
                # place our new node here
            # otherwise
                # repeat the process for the right
        if value >= self.value:
          if not self.right:
            node = BinarySearchTree(value)
            self.right = node
          else:
            self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
          return True
        
        #LHS
        if target < self.value:
          if not self.left:
            return False
          else:
            return self.left.contains(target)

        #RHS
        if target >= self.value:
          if not self.right:
            return False
          else:
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        #BASE CASE
        # if empty tree
        if not self:
            return None
        
        # if there is no right value 
        if not self.right:
          # return the root node value
            return self.value
        else:
          # return get max of the right hand child
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # base case run the callback passing in the selfs value
        cb(self.value)
        # if left exists
        if self.left:
          # run the for each on left
            self.left.for_each(cb)
        # if right exists
        if self.right:
          # run the for each on right
            self.right.for_each(cb)


   


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        #check if there is a left node:
        if node.left is not None:
          #stack the node to the left
          self.stack.push(node.left)
        #check if there is a right node:
        if node.right is not None:
          #stack the node to the right
          self.stack.push(node.left)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # create the queue instance
        queue = Queue()
        # add the node to queue
        queue.enqueue(node)

        # if there is a node in the queue
        if queue.len():
            # dequeue the queue
            current_node = queue.dequeue()
            # print the value of the node
            # print(current_node.value)

            # if there is a left node add it to the queue
            if current_node.left is not None:
                queue.enqueue(current_node.left)

            # if there is a right node add it to the queue
            if current_node.right is not None:
                queue.enqueue(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
         # create the stack instance
        stack = Stack()
        # add the node to stack
        stack.push(node)

        # if there is a node in the stack
        if stack.len():
            # pop the stack
            current_node = stack.pop()
            # print the value of the node
            # print(current_node.value)

            # if there is a left node add it to the stack
            if current_node.left is not None:
                stack.push(current_node.left)

            # if there is a right node add it to the stack
            if current_node.right is not None:
                stack.push(current_node.right)


    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
