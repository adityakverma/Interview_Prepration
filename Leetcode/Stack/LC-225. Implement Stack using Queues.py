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

