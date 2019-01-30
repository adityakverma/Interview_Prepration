
#Tags: Stack, Design, MS, Bloomberg

# Queue is FIFO (first in - first out) data structure, in which the elements are inserted
# from one side - rear and removed from the other - front. The most intuitive way to
# implement it is with linked lists, but this article will introduce another approach using
#  stacks. Stack is LIFO (last in - first out) data structure, in which elements are added
#  and removed from the same end, called top. To satisfy FIFO property of a queue we need
# to keep two stacks. They serve to reverse arrival order of the elements and one of them
# store the queue elements in their final order.

class MyQueue(object):

    # initialize your data structure here.
    def __init__(self):
        self.stack1 = []  # To push the elements on stack S1. Helpful with push operation.
        self.stack2 = []  # Helps to reverse the order of S1 to provide FIFO property. Helpful with pop() and peek() operation

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stack1.append(x)

    # @return nothing
    def pop(self):
        if len(self.stack2)!=0:
            return self.stack2.pop()  # Same as peek except we pop instead of stack2[-1]
        else:
            while len(self.stack1)!=0:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()

    # @return an integer
    def peek(self):
        if len(self.stack2)!=0:
            return self.stack2[-1]
        else:
            while len(self.stack1)!=0:
                self.stack2.append(self.stack1.pop())
            return self.stack2[-1]

    # @return an boolean
    def empty(self):
        if len(self.stack1)==0 and len(self.stack2)==0: # Important - Verify both S1 and S2
            return True
        else:
            return False


