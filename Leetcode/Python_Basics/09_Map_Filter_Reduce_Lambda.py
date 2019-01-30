
# http://book.pythontips.com/en/latest/debugging.html   <==== Important Tips on Python


# Iterating With Python Lambdas

# https://caisbalderas.com/blog/iterating-with-python-lambdas/
# https://medium.com/@happymishra66/lambda-map-and-filter-in-python-4935f248593

# http://www.secnetix.de/olli/Python/lambda_functions.hawk



############################# MAP ##############################

# Map applies a function to all the items in an input_list. Here is the blueprint:

# Blueprint
# map(function_to_apply, list_of_inputs)

# Python program to demonstrate working
# of map.

# Return double of n
def addition(n):
    return n + n

# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))



def multiply(x):
    return (x*x)
def add(x):
    return (x+x)

funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)

# Output:
# [0, 0]
# [1, 2]
# [4, 4]
# [9, 6]
# [16, 8]

#----------------------------

items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print "\nMAP: ",squared

# Note: here even if you do filter instead of map, you get same output.

#------------------------------

# List of strings
l = ['sat', 'bat', 'cat', 'mat']

# map() can listify the list of strings individually
test = list(map(list, l))
print(test)

############################## FILTER ############################

# As the name suggests, filter creates a list of elements for which a function returns true.
# [Aditya] Filter should have some condition in 'funtion' part, to filter
a = [1, 2, 3, 4, 5, 6]
print "\nFILTER", filter(lambda x : x % 2 == 0, a)


number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print "FILTER", less_than_zero

# Output: [-5, -4, -3, -2, -1]

#---------------------
# https://caisbalderas.com/blog/iterating-with-python-lambdas/

#### Example-01 ###########

x = [2, 3, 4, 5, 6]
y = []
for v in x:
    if v % 2:
        y += [v * 5]
assert x == [2, 3, 4, 5, 6]
assert y == [15, 25]
print "\nREGULAR WAY", y
# -------------------

# list comprehension of the same process done in loop...
#
#     x = [2, 3, 4, 5, 6]
#     y = [v * 5 for v in x if v % 2]  <============ IMP


x = [2, 3, 4, 5, 6]
y = map(lambda v: v * 5, filter(lambda u: u % 2, x))  # <============ IMP: 1st one is fn and 2nd one in inputs
z = filter(lambda v: v * 5, filter(lambda u: u % 2, x))
print "USING MAP-FILTER: ", y
print "USING FILTER: ", z

# filter() takes in a function(lambda) and iterable(x) and returns an iterable containing "filtered" values that passed through the function.
# filter(function, iterable) --> [item for item in iterable if function(item)]

####### Example-2  #####

# x = [2, 3, 4]
#     y = [4, 5]
#     z = []
#     for v in x :
#         for w in y :
#             z += [v + w]
#
# Now with a list comprehension...
#
#     x = [2, 3, 4]
#     y = [4, 5]
#     z = [v + w for v in x for w in y]   # <================ IMP
#
# And finally with lamdas....
#
# x = [2, 3, 4]
# y = [4, 5]
# t = map(lambda v : map(lambda w : v + w, y), x)  <=========== IMP
# print t


##############

list_a = [1, 2, 3]
list_b = [10, 20, 30]

print map(lambda x, y: x + y, list_a, list_b)  # Output: [11, 22, 33]


#-------------

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))

numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))

############################# REDUCE ############################

# Reduce is a really useful function for performing some computation
# on a list and returning the result.

product = 1
list = [1, 2, 3, 4]
for num in list:
    product = product * num

# product = 24

# Now let us try it with reduce:
from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print "\nREDUCE: ", product

# Output: 24

############################### ZIP in Python #######################

# https://medium.com/@happymishra66/zip-in-python-48cb4f70d013

# zip takes n number of iterables and returns list of tuples. ith element of the tuple is created using the ith element from each of the iterables.

list_a = [1, 2, 3, 4, 5]
list_b = ['a', 'b', 'c', 'd', 'e']

zipped_list = zip(list_a, list_b)

print "\nZIP:", zipped_list # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]






