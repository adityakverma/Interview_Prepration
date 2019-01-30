
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

q=Queue()

q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
print(q.size())

###############################################################################

# Python3 program for array implementation of queue

# Class Queue to represent a queue
class Queue:
    # __init__ function
    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        self.Q = [None] * capacity
        self.capacity = capacity

    # Queue is full when size becomes
    # equal to the capacity
    def isFull(self):
        return self.size == self.capacity

    # Queue is empty when size is 0
    def isEmpty(self):
        return self.size == 0

    # Function to add an item to the queue.
    # It changes rear and size
    def EnQueue(self, item):
        if self.isFull():
            print("Full")
            return
        self.rear = (self.rear + 1) % (self.capacity)
        self.Q[self.rear] = item
        self.size = self.size + 1
        print("%s enqueued to queue" % str(item))

    # Function to remove an item from queue.
    # It changes front and size
    def DeQueue(self):
        if self.isEmpty():
            print("Empty")
            return

        print("%s dequeued from queue" % str(self.Q[self.front]))
        self.front = (self.front + 1) % (self.capacity)
        self.size = self.size - 1

    # Function to get front of queue
    def que_front(self):
        if self.isEmpty():
            print("Queue is empty")

        print("Front item is", self.Q[self.front])

    # Function to get rear of queue
    def que_rear(self):
        if self.isEmpty():
            print("Queue is empty")
        print("Rear item is", self.Q[self.rear])


# Driver Code
if __name__ == '__main__':
    print "\n\n"
    queue = Queue(30)
    queue.EnQueue(10)
    queue.EnQueue(20)
    queue.EnQueue(30)
    queue.EnQueue(40)
    queue.DeQueue()
    queue.que_front()
    queue.que_rear()
###############################################################################

# http://interactivepython.org/runestone/static/pythonds/BasicDS/SimulationPrintingTasks.html
#
# from pythonds.basic.queue import Queue
#
# import random
#
# class Printer:
#     def __init__(self, ppm):
#         self.pagerate = ppm
#         self.currentTask = None
#         self.timeRemaining = 0
#
#     def tick(self):
#         if self.currentTask != None:
#             self.timeRemaining = self.timeRemaining - 1
#             if self.timeRemaining <= 0:
#                 self.currentTask = None
#
#     def busy(self):
#         if self.currentTask != None:
#             return True
#         else:
#             return False
#
#     def startNext(self,newtask):
#         self.currentTask = newtask
#         self.timeRemaining = newtask.getPages() * 60/self.pagerate
#
# class Task:
#     def __init__(self,time):
#         self.timestamp = time
#         self.pages = random.randrange(1,21)
#
#     def getStamp(self):
#         return self.timestamp
#
#     def getPages(self):
#         return self.pages
#
#     def waitTime(self, currenttime):
#         return currenttime - self.timestamp
#
#
# def simulation(numSeconds, pagesPerMinute):
#
#     labprinter = Printer(pagesPerMinute)
#     printQueue = Queue()
#     waitingtimes = []
#
#     for currentSecond in range(numSeconds):
#
#       if newPrintTask():
#          task = Task(currentSecond)
#          printQueue.enqueue(task)
#
#       if (not labprinter.busy()) and (not printQueue.isEmpty()):
#         nexttask = printQueue.dequeue()
#         waitingtimes.append( nexttask.waitTime(currentSecond))
#         labprinter.startNext(nexttask)
#
#       labprinter.tick()
#
#     averageWait=sum(waitingtimes)/len(waitingtimes)
#     print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,printQueue.size()))
#
# def newPrintTask():
#     num = random.randrange(1,181)
#     if num == 180:
#         return True
#     else:
#         return False
#
# for i in range(10):
#     simulation(3600,5)
