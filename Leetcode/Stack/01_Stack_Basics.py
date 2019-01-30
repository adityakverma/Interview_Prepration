
# Now that we have clearly defined the stack as an abstract data type we will turn
# our attention to using Python to implement the stack.

#     The Stack Abstract Data Type:
#
#     Stack() creates a new stack that is empty. It needs no parameters and
#       returns an empty stack.
#     push(item) adds a new item to the top of the stack. It needs the item
#       and returns nothing.
#     pop() removes the top item from the stack. It needs no parameters and
#       returns the item. The stack is modified.
#     peek() returns the top item from the stack but does not remove it.
#       It needs no parameters. The stack is not modified.
#     isEmpty() tests to see whether the stack is empty. It needs no parameters
#       and returns a boolean value.
#     size() returns the number of items on the stack. It needs no parameters and returns an integer.


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item): # Add or push which uses append()
        self.stack.append(item)

    def pop(self): # Pop or remove which uses pop()
        if len(self.stack) <= 0:
            return ("No element in the Stack")
        else:
            return self.stack.pop()

    def peek(self):     # peek() returns the top item from the stack but does not remove it.
        return self.stack[-1]

    def isEmpty(self):
        return self.stack == [] # OR return len(stack) == 0

    def size(self):
        return len(self.stack)

s = Stack()
s.push('hello')
s.push('true')
print(s.pop())

############################################################################

# Python program for implementation of stack

# import maxsize from sys module
# Used to return -infinite when stack is empty
from sys import maxsize


# Function to create a stack. It initializes size of stack as 0
def createStack():
    stack = []
    return stack


# Stack is empty when stack size is 0
def isEmpty(stack):
    return len(stack) == 0


# Function to add an item to stack. It increases size by 1
def push(stack, item):
    stack.append(item)
    print("pushed to stack " + item)


# Function to remove an item from stack. It decreases size by 1
def pop(stack):
    if (isEmpty(stack)):
        return str(-maxsize - 1)  # return minus infinite

    return stack.pop()


# Driver program to test above functions
# stack = createStack()
# push(stack, str(10))
# push(stack, str(20))
# push(stack, str(30))
# print(pop(stack) + " popped from stack")