

# https://www.geeksforgeeks.org/list-methods-in-python-set-1-in-not-in-len-min-max/
# https://www.geeksforgeeks.org/list-methods-python/

# https://www.programiz.com/python-programming/methods/list/sort


################# SORT LIST #####################

# The syntax of sort() method is:
#   list.sort(key=..., reverse=...)
#
# Alternatively, you can also use Python's in-built function sorted() for the same purpose.
#   sorted(list, key=..., reverse=...)


# take second element for sort
def takeSecond(elem):
    return elem[1]

# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# sort list with key
random.sort(key=takeSecond)

# print list
print('Sorted list:', random)
####################################

# vowels list
vowels = ['e', 'a', 'u', 'o', 'i']

# sort the vowels
vowels.sort(reverse=True)

# print vowels
print('Sorted list (in Descending):', vowels)