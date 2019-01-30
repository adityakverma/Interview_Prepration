
# IMP : Let me explain it. The 1 means to start at second
# element in the list (note that the slicing index starts at 0)
# . The 4 means to end at the fifth element in the list, but not
# include it. The colon in the middle is how Python's lists recognize
# that we want to use slicing to get objects in the list.


# values = [100, 200, 300, 400, 500]
#              Get elements from...
# values[1:3]  Index 1 through index 3.
# values[2:-1] Index 2 through index one from last.
# values[:2]   Start through index 2.
# values[2:]   Index 2 through end.
# values[::2]  Start through end, skipping ahead 2 places each time.
#

values = [100, 200, 300, 400, 500]
# Get elements from second index to third index.
slice = values[1:3]
print(slice)

values = [100, 200, 300, 400, 500]
# Slice from third index to index one from last.
slice = values[2:-1]
print(slice)

values = [100, 200, 300, 400, 500]
# Slice from start to second index.
slice = values[:2]
print(slice)

# Slice from second index to end.
slice = values[2:]
print(slice)

word = "something"
# Get first four characters.
part = word[:4]
print(part)

values = "AaBbCcDdEe"

# Starting at 0 and continuing until end, take every other char.
evens = values[::2]
print(evens)

a = [1, 2, 3, 4, 5, 6, 7, 8]
print a[1:4:2]
print a[::-1]

# https://stackoverflow.com/questions/509211/understanding-pythons-slice-notation

# It's pretty simple really:
#
# a[start:end] # items start through end-1
# a[start:]    # items start through the rest of the array
# a[:end]      # items from the beginning through end-1
# a[:]         # a copy of the whole array
#
# There is also the step value, which can be used with any of the above:
#
# a[start:end:step] # start through not past end, by step
# a[-1]    # last item in the array
# a[-2:]   # last two items in the array
# a[:-2]   # everything except the last two items
#
# Similarly, step may be a negative number:
#
# a[::-1]    # all items in the array, reversed
# a[1::-1]   # the first two items, reversed
# a[:-3:-1]  # the last two items, reversed
# a[-3::-1]  # everything except the last two items, reversed


#See LC-670

# Underscore: https://hackernoon.com/understanding-the-underscore-of-python-309d1a029edc
