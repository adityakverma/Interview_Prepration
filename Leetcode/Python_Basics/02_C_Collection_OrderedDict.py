
# 8.3.6.1. OrderedDict Examples and Recipes
# OrderedDict Examples and Recipes
#
# Since an ordered dictionary remembers its insertion order, it can be used in
# conjunction with sorting to make a sorted dictionary:
# >>>
#
# >>> # regular unsorted dictionary
# >>> d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
#
# >>> # dictionary sorted by key
# >>> OrderedDict(sorted(d.items(), key=lambda t: t[0]))
# OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])
#
# >>> # dictionary sorted by value
# >>> OrderedDict(sorted(d.items(), key=lambda t: t[1]))
# OrderedDict([('pear', 1), ('orange', 2), ('banana', 3), ('apple', 4)])
#
# >>> # dictionary sorted by length of the key string
# >>> OrderedDict(sorted(d.items(), key=lambda t: len(t[0])))
# OrderedDict([('pear', 1), ('apple', 4), ('orange', 2), ('banana', 3)])

# ------------------------------------------------------------------------------