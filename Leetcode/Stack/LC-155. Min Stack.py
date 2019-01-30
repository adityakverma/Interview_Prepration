# Tags: Stack, Design, Google, AWS, Bloomberg, Uber

#  Design a stack that supports push, pop, top, and retrieving the minimum
#  element in constant time.
#     push(x) -- Push element x onto stack.
#     pop() -- Removes the element on top of the stack.
#     top() -- Get the top element.
#     getMin() -- Retrieve the minimum element in the stack.
# Example:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.

class MinStack1():      # Accepted in First attempt
    def __init__(self):
        self.items = []

    def notEmpty(self):
        return len(self.items) == 0

    def push(self,elem):
        self.items.append(elem)

    def pop(self):
        if( not self.notEmpty()):
            self.items.pop()

    def top(self):
        return self.items[len(self.items) -1]

    def getMin(self):
        return min(self.items)

###########################################################
# There are two approaches:
#
#     Use 2 stacks. 1 stack contains all elements and the other stack tracks the minimum element.
#     Directly store a tuple in this format in one stack- (element, minimum element till now in stack).
#     The code posted below follows approach 2.

class MinStack2:  # Doesn't uses Min Function

    def __init__(self):
        self.q = []

    def push(self, x):
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        self.q.append((x, curMin)) # Smart - Each push stores kind of structure or we call tuple in python

    def pop(self):
        self.q.pop()

    # @return an integer
    def top(self):
        if len(self.q) == 0:  # Good - took care of empty case
            return None
        else:
            return self.q[-1][0]

    # @return an integer
    def getMin(self):
        if len(self.q) == 0:  # again took care of empty case
            return None
        else:
            return self.q[-1][1]


############################################################


if __name__ == '__main__':
    s = MinStack2()
    s.push(10)
    s.push(5)
    s.push(-5)
    s.push(30)
    print "\nMin element:",s.getMin()
    #print s.items
    s.pop()
    s.pop()
    #print s.items
    print "\nMin element:",s.getMin()
    #print "\nIs empty?",s.notEmpty()




