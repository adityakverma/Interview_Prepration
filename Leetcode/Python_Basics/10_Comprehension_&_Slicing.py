

# https://www.geeksforgeeks.org/python-list-comprehension-and-slicing/

#-------- list comprehensions ----------------

multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)
# Output: [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]

#-------------------

squared = []
for x in range(10):
    squared.append(x**2)

# You can simplify it using list comprehensions. For example:

squared = [x**2 for x in range(10)]
print "\nSQUARED: ",squared

#------------------- COMPREHENSION -----------------------------

# below list contains square of all odd numbers from
# range 1 to 10
odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1]
print odd_square

# for understanding, above generation is same as,
odd_square = []
for x in range(1, 11):
    if x % 2 == 1:
        odd_square.append(x ** 2)
print odd_square

# below list contains power of 2 from 1 to 8
power_of_2 = [2 ** x for x in range(1, 9)]
print power_of_2

#--------  set comprehensions ----------------

# set comprehensions
# They are also similar to list comprehensions. The only difference is that they use braces {}

squared = {x**2 for x in [1, 1, 2]}
print(squared)
# Output: {1, 4}

# ---------------- LIST SLICING ---------------------------------

# So [: stop] will slice list from starting till stop index and [start : ] will slice list from start
# index till end Negative value of steps shows right to left traversal instead of left to right traversal
# that is why [: : -1] prints list in reverse order.

# Let us first create a list to demonstrate slicing
# lst contains all number from 1 to 10
lst = range(1, 11)
print "\nSLICING\n",lst

#  below list has numbers from 2 to 5
lst1_5 = lst[1: 5]
print lst1_5

#  below list has numbers from 6 to 8
lst5_8 = lst[5: 8]
print lst5_8

#  below list has numbers from 10 to 1
lst_rev = lst[:: -1]
print lst_rev

#  below list has numbers from 10 to 6 in step 2
lst_rev_9_5_2 = lst[9: 4: -2]
print lst_rev_9_5_2

#---------------------------------- FILTER ---------------------------

# We can use filter function to filter a list based on some condition provided as a lambda expression as first
# argument and list as second argument, example of which is shown below :

#  filtering odd numbers
lst = filter(lambda x: x % 2 == 1, range(1, 20))
print "\nFILTER\n", lst

#  filtering odd square which are divisble by 5
lst = filter(lambda x: x % 5 == 0,
             [x ** 2 for x in range(1, 11) if x % 2 == 1])
print lst

#   filtering negative numbers
lst = filter((lambda x: x < 0), range(-5, 5))
print lst

#  implementing max() function, using
print reduce(lambda a, b: a if (a > b) else b, [7, 12, 45, 100, 15])

