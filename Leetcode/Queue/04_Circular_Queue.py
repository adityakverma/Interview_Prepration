
# https://www.geeksforgeeks.org/circular-queue-set-1-introduction-array-implementation/

# Circular Queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is
# connected back to the first position to make a circle. It is also called Ring Buffer.
#
# In a normal Queue, we can insert elements until queue becomes full. But once queue becomes full, we can not insert the next element even if there is a space in front of queue.
#
# Operations-on-Circular queue
#
# Operations on Circular Queue:
#
#     Front: Get the front item from queue.
#     Rear: Get the last item from queue.
#     enQueue(value) This function is used to insert an element into the circular queue. In a circular queue, the new element is always inserted at Rear position.
#         Steps:
#
#         Check whether queue is Full – Check ((rear == SIZE-1 && front == 0) || (rear == front-1)).
#         If it is full then display Queue is full. If queue is not full then, check if (rear == SIZE – 1 && front != 0) if it is true then set rear=0
#         and insert element.
#     deQueue() This function is used to delete an element from the circular queue. In a circular queue, the element is always deleted from front position.
#         Steps:
#
#         Check whether queue is Empty means check (front==-1).
#         If it is empty then display Queue is empty. If queue is not empty then step 3
#         Check if (front==rear) if it is true then set front=rear= -1 else check if (front==size-1), if it is true then set front=0 and return the element.
#
# --------------------------
#
# Time Complexity: Time complexity of enQueue(), deQueue() operation is O(1) as there is no loop in any of the operation.
#
# Applications:
#
#     Memory Management: The unused memory locations in the case of ordinary queues can be utilized in circular queues.
#     Traffic system: In computer controlled traffic system, circular queues are used to switch on the traffic lights one by one repeatedly as per the time set.
#     CPU Scheduling: Operating systems often maintain a queue of processes that are ready to execute or that are waiting for a particular event to occur.
