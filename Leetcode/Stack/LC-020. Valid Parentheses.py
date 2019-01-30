
# Tags: String, Stack, Google, FB, MS, AWS.

# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 2:
# Input: "()[]{}"
# Output: true

# Example 4:
# Input: "([)]"
# Output: false
###################################################################
class Solution(object):

    def isValid(self, s): # Accepted
        stack = []         # Basically we are treating list as stack here and using list functions like append(), pop().
        match = {'(': ')', '[': ']', '{': '}'}

        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
                #print "After appending",stack

            elif not stack or match[stack.pop()] != c:
                #print "popped",stack, stack.pop(),"--", match[stack.pop()], "--",c
                return False
            #print "ok", c, stack, not stack
        return not stack # or return true

if __name__ == '__main__':
    brackets = "(({)})"
    s = Solution()
    print "\n%s sequence is %s" %(brackets,s.isValid(brackets))




# Python List Methods
# --------------------

# append() - Add an element to the end of the list
# extend() - Add all elements of a list to the another list
# insert() - Insert an item at the defined index
# remove() - Removes an item from the list
# pop() - Removes and returns an element at the given index
# clear() - Removes all items from the list
# index() - Returns the index of the first matched item
# count() - Returns the count of number of items passed as an argument
# sort() - Sort items in a list in ascending order
# reverse() - Reverse the order of items in the list
# copy() - Returns a shallow copy of the list


# pop() parameter
# ---------------
# The pop() method takes a single argument (index) and removes the element present at that index from the list.
# If the index passed to the pop() method is not in the range, it throws IndexError: pop index out of range exception.
# The parameter passed to the pop() method is optional. If no parameter is passed, the default index -1 is passed as an
#  argument which returns the last element.


