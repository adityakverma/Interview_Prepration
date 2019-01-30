
# https://docs.python.org/2/library/collections.html#collections.defaultdict
from collections import defaultdict


# Using list as the default_factory, it is easy to group a sequence of key-value pairs into a dictionary of lists:
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)

print "keys",d.keys()
print "Values",d.values()
print d.items()
#[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]

# Setting the default_factory to int makes the defaultdict useful for counting
s = 'mississippi'
d = defaultdict(int)
for k in s:
    d[k] += 1
print d.items()
# [('i', 4), ('p', 2), ('s', 4), ('m', 1)]

# Setting the default_factory to set makes the defaultdict useful for building a
# dictionary of sets: - removes duplicates

s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
d = defaultdict(set)
for k, v in s:
    d[k].add(v)
print d.items()
# [('blue', set([2, 4])), ('red', set([1, 3]))]

#----------------------------------------------------------------------------

