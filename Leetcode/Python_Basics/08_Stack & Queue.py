#
# #
# Using List as Stack and Queues in Python
#
# Prerequisite : list in Python
#
# The concept of Stack and Queue is easy to implement in Python.
#
# Stack works on the principle of “Last-in, first-out”. Also, the inbuilt functions in Python make the code short and simple. To add an item to the top of the list, i.e., to push an item, we use append() function and to pop out an element we use pop() function. These functions work quiet efficiently and fast in end operations.
#
# Let’s look at an example and try to understand the working of push() and pop() function:
# Example:
# # Python code to demonstrate Implementing
# # stack using list
# stack = ["Amar", "Akbar", "Anthony"]
# stack.append("Ram")
# stack.append("Iqbal")
# print(stack)
# print(stack.pop())
# print(stack)
# print(stack.pop())
# print(stack)
#
# Output :
#
# ['Amar', 'Akbar', 'Anthony', 'Ram', 'Iqbal']
# Iqbal
# ['Amar', 'Akbar', 'Anthony', 'Ram']
# Ram
# ['Amar', 'Akbar', 'Anthony']
#
# Implementing queue is a bit different. Queue works on the principle of “First-in, first-out”. Time plays an important factor here. We saw that during the implementation of stack we used append() and pop() function which was efficient and fast because we inserted and popped elements from the end of the list, but in queue when insertion and pops are made from the beginning of the list, it is slow. This occurs due to the properties of list, which is fast at the end operations but slow at the beginning operations, as all other elements have to be shifted one by one. So, we prefer the use of collections.deque over list, which was specially designed to have fast appends and pops from both the front and back end.
#
#
# Let’s look at an example and try to understand queue using collections.deque:
# # Python code to demonstrate Implementing
# # Queue using deque and list
# from collections import deque
# queue = deque(["Ram", "Tarun", "Asif", "John"])
# print(queue)
# queue.append("Akbar")
# print(queue)
# queue.append("Birbal")
# print(queue)
# print(queue.popleft())
# print(queue.popleft())
# print(queue)


# https://www.geeksforgeeks.org/stack-queue-python-using-module-queue/

# https://www.geeksforgeeks.org/using-list-stack-queues-python/
