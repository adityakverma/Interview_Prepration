
# Design a data structure that supports all following operations in average O(1) time.
#
#     insert(val): Inserts an item val to the set if not already present.
#     remove(val): Removes an item val from the set if present.
#     getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
#
# Example:
#
# // Init an empty set.
# RandomizedSet randomSet = new RandomizedSet();
#
# // Inserts 1 to the set. Returns true as 1 was inserted successfully.
# randomSet.insert(1);
#
# // Returns false as 2 does not exist in the set.
# randomSet.remove(2);
#
# // Inserts 2 to the set, returns true. Set now contains [1,2].
# randomSet.insert(2);
#
# // getRandom should return either 1 or 2 randomly.
# randomSet.getRandom();
#
# // Removes 1 from the set, returns true. Set now contains [2].
# randomSet.remove(1);
#
# // 2 was already in the set, so return false.
# randomSet.insert(2);
#
# // Since 2 is the only number in the set, getRandom always return 2.
# randomSet.getRandom();


# https://leetcode.com/problems/insert-delete-getrandom-o1/discuss/85397/Simple-solution-in-Python

import random

class RandomizedSet1(object):
    def __init__(self):
        self.set = set()

    def insert(self, val):
        if val in self.set:
            return False
        else:
            self.set.add(val)
            return True

    def remove(self, val):
        if val in self.set:
            self.set.remove(val)
            return True
        else:
            return False

    def getRandom(self):
        t = len(self.set) - 1
        list_set = list(self.set)
        return list_set[random.randint(0, t)]

    #def getRandom(self):
    #    return random.choice(self.set)  # Note: random only works on list and not set

###################################################################

# https://leetcode.com/problems/insert-delete-getrandom-o1/discuss/85397/Simple-solution-in-Python
# We just keep track of the index of the added elements, so when we remove them, we copy the last one into it.
# From Python docs (https://wiki.python.org/moin/TimeComplexity) we know that list.append() takes O(1), both average and amortized.
# Dictionary get and set functions take O(1) average, so we are OK

class RandomizedSet2(object):

    def __init__(self):
        self.nums, self.pos = [], {}

    def insert(self, val):
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums) - 1
            return True
        return False

    def remove(self, val):
        if val in self.pos:
            idx, last = self.pos[val], self.nums[-1]
            self.nums[idx], self.pos[last] = last, idx
            self.nums.pop();
            self.pos.pop(val, 0)
            return True
        return False

    def getRandom(self):
        return self.nums[random.randint(0, len(self.nums) - 1)]

#########################################################################

if __name__ == '__main__':
    s = RandomizedSet1()
    print "\nTesting-1: ", s.insert(1), s.remove(2), s.insert(2), s.getRandom(), s.remove(1), s.insert(2), s.getRandom()

    r = RandomizedSet2()
    print "\nTesting-2: ", r.insert(1), r.remove(2), r.insert(2), r.getRandom(), r.remove(1), r.insert(2), r.getRandom()


# Question: I still don't understand why do you need a list ? you can store everything in a dictionary ?
# Answer: When you store everything in a dictionary or set, it's fine when you insert or remove.
# But if you want to achieve O(1) on getRandom(), it's impossible.
# You have to turn it into a list first, which is O(n

# Sample Input:
# ["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]
# [[],[1],[2],[2],[],[1],[2],[]]
# Expected Answer: [null,true,false,true,1,true,false,2]

# Next Challenge.
# 381. Insert Delete GetRandom O(1) - Duplicates allowed

# ============================================================================================

# https://docs.python.org/2/library/sets.html
# The following table lists operations available in Set but not found in ImmutableSet:
# Operation 	Equivalent 	Result

# s.update(t) 	s |= t 	return set s with elements added from t
# s.intersection_update(t) 	s &= t 	return set s keeping only elements also found in t
# s.difference_update(t) 	s -= t 	return set s after removing elements found in t
# s.symmetric_difference_update(t) 	s ^= t 	return set s with elements from s or t but not both
# s.add(x) 	  	add element x to set s
# s.remove(x) 	  	remove x from set s; raises KeyError if not present
# s.discard(x) 	  	removes x from set s if present
# s.pop() 	  	remove and return an arbitrary element from s; raises KeyError if empty
# s.clear() 	  	remove all elements from set s

# ============================================================================================

# https://docs.python.org/2/library/sets.html
# nstances of Set and ImmutableSet both provide the following operations:
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

# ============================================================================================

# https://www.programiz.com/python-programming/set
