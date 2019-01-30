
# https://docs.python.org/2/library/sets.html
# https://www.geeksforgeeks.org/sets-in-python/


# A Set is an unordered collection data type that is iterable, mutable, and
# has no duplicate elements. Pythons set class represents the mathematical
# notion of a set. The major advantage of using a set, as opposed to a list,
# is that it has a highly optimized method for checking whether a specific
# element is contained in the set. This is based on a data structure known
# as a hash table.

# The sets module provides classes for constructing and manipulating unordered
# collections of unique elements. Common uses include membership testing,
# removing duplicates from a sequence, and computing standard math operations on
# sets such as intersection, union, difference, and symmetric difference


# Sets and frozen sets support the following operators:
#
# key in s  # containment check
# key not in s  # non-containment check
# s1 == s2  # s1 is equivalent to s2
# s1 != s2  # s1 is not equivalent to s2
# s1 <= s2  # s1is subset of s2 s1 < s2     # s1 is proper subset of s2 s1 >= s2    # s1is superset of s2
# s1 > s2  # s1 is proper superset of s2
# s1 | s2  # the union of s1 and s2
# s1 & s2  # the intersection of s1 and s2
# s1 - s2  # the set of elements in s1 but not s2


# Python program to demonstrate working# of
# Set in Python

# Creating two sets
set1 = set()
set2 = set()

# Adding elements to set1
for i in range(1, 6):
    set1.add(i)

# Adding elements to set2
for i in range(3, 8):
    set2.add(i)

print("Set1 = ", set1)
print("Set2 = ", set2)
print("\n")

# Union of set1 and set2
set3 = set1 | set2  # set1.union(set2)
print("Union of Set1 & Set2: Set3 = ", set3)

# Intersection of set1 and set2
set4 = set1 & set2  # set1.intersection(set2)
print("Intersection of Set1 & Set2: Set4 = ", set4)
print("\n")

# Checking relation between set3 and set4
if set3 > set4:  # set3.issuperset(set4)
    print("Set3 is superset of Set4")
elif set3 < set4:  # set3.issubset(set4)
    print("Set3 is subset of Set4")
else:  # set3 == set4
    print("Set3 is same as Set4")

# displaying relation between set4 and set3
if set4 < set3:  # set4.issubset(set3)
    print("Set4 is subset of Set3")
    print("\n")

# difference between set3 and set4
set5 = set3 - set4
print("Elements in Set3 and not in Set4: Set5 = ", set5)
print("\n")

# checkv if set4 and set5 are disjoint sets
if set4.isdisjoint(set5):
    print("Set4 and Set5 have nothing in common\n")

# Removing all the values of set5
set5.clear()

print("After applying clear on sets Set5: ")
print("Set5 = ", set5)

# Output:
#
# ('Set1 = ', set([1, 2, 3, 4, 5]))
# ('Set2 = ', set([3, 4, 5, 6, 7]))
#
# ('Union of Set1 & Set2: Set3 = ', set([1, 2, 3, 4, 5, 6, 7]))
# ('Intersection of Set1 & Set2: Set4 = ', set([3, 4, 5]))


# =========================================================================
# Instances of Set and ImmutableSet both provide the following operations:

# Operation 	Equivalent 	Result
# len(s) 	  	number of elements in set s (cardinality)
# x in s 	  	test x for membership in s
# x not in s 	  	test x for non-membership in s
# s.issubset(t) 	s <= t 	test whether every element in s is in t
# s.issuperset(t) 	s >= t 	test whether every element in t is in s
# s.union(t) 	s | t 	new set with elements from both s and t
# s.intersection(t) 	s & t 	new set with elements common to s and t
# s.difference(t) 	s - t 	new set with elements in s but not in t
# s.symmetric_difference(t) 	s ^ t 	new set with elements in either s or t but not both
# s.copy() 	  	new set with a shallow copy of s

# =========================================================================
