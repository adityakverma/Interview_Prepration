
# Tags:  Array, FB, MS, AWS, LinkedIn
# ===================================

# The idea is that for each element of the array, you would want to multiply all
# the elements to the left and right. So in the first for loop you are cumulatively
#  multiplying all the previous elements to each other in each iteration, essentially
# multiplying all the elements to the left of the element. In the second for loop,
# you will be doing the same now except now in reverse as you will be multiplying all
# the elements to the right.
#
# [1, 2, 3, 4] <---- input
# [1]
# [1, 1]
# [1, 1, 2]
# [1, 1, 2, 6]
#
# [1, 1, 2, 6] *note that the last element of the array is already its answer because
# it is the product of all the elements to the left of it
# [1, 1, 8, 6]
# [1, 12, 8, 6]
# [24, 12, 8, 6]

def productExceptSelf(self, nums):
    res = [1] * len(nums)

    p = 1
    for i in range(len(nums)): # from left to right
        res[i] *= p # Meaning don't consider current value, instead take previous's value stored in p * resr[i] which is 1. So basically at resr[i] we store product of all elements left to it.
        p *= nums[i]

    p = 1
    for i in range(len(nums) - 1, -1, -1): # from right to left
        res[i] *= p
        p *= nums[i]

    return res


# product of array except nums[i] = product of numbers to the left of nums[i] * product of
# numbers to the right of nums[i]
#
# Please note that nums[0] doesn't have elements to its left, and nums[n-1] doesn't have
# elements to its right. Thus
#
# leftProduct[0] = 1;
# rightProduct[n - 1] = 1;



