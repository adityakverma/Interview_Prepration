
# ==================================================================
# Implement the following operations of a queue using stacks.
#
#     push(x) -- Push element x to the back of queue.
#     pop() -- Removes the element from in front of queue.
#     peek() -- Get the front element.
#     empty() -- Return whether the queue is empty.
#
# Example:
# MyQueue queue = new MyQueue();
#
# queue.push(1);
# queue.push(2);
# queue.peek();  // returns 1
# queue.pop();   // returns 1
# queue.empty(); // returns false
# ==================================================================


class MyQueue(object):

    # initialize your data structure here.
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

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
        if len(self.stack1)==0 and len(self.stack2)==0:
            return True
        else:
            return False

#####################################################################################################

# 225. Implement Stack using Queues
import collections

class MyStack(object):

    # initialize your data structure here.
    def __init__(self):
        self.stack = collections.deque([])

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stack.append(x)

    # @return nothing
    def pop(self):
        for i in range(len(self.stack) - 1):
           self.stack.append(self.stack.popleft())
        return self.stack.popleft()

        # Note:  I am wondering why use for loop in def pop(self) instead of directly use self.stack.pop().
        # Ans: Hey you are implementing a stack thus you don't have stack.pop() yet right? That's the function you are currently implementing ;) You can only do standard queue operations which means pop from the head only (popleft())
        # return self.stack.pop()

    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an boolean
    def empty(self):
        return len(self.stack) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

# ==============================================================================

