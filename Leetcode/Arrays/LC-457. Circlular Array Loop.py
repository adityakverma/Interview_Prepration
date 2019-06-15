

class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def getIndex(i):
            n = len(nums)
            return (i + nums[i] + n ) % n

        # start from every position in the array
        for i, val in enumerate(nums):
            if val == 0:
                continue

            # slow/fast pointer
            j = i
            k = getIndex(i)

            # as long as moving in the same direction - either forward or backward
            while nums[k] * nums[i] > 0 and nums[getIndex(k)] * nums[i] > 0:
                if j == k:
                    # check for loop with only one element. Meaning len(nums) ==1 so loop of 1 element is not allowed.
                    if j == getIndex(j):
                        break
                    return True

                j = getIndex(j)
                k = getIndex(getIndex(k))

            # loop was either not found or if found, it was not unidirectional
            # traverse entire loop again from start (i) and mark the ones which have been visited. Set all element along the way to 0
            # This means this path doesn't have loop, so try for next value of i ( from outer for loop)
            j = i
            while nums[j] * val > 0:
                next = getIndex(j)
                nums[j] = 0
                j = next

        return False


# Just think it as finding a loop in Linkedlist, except that loops with only 1 element do not count. Use a slow and fast pointer, slow pointer moves 1 step a time while fast pointer moves 2 steps a time. If there is a loop (fast == slow), we return true, else if we meet element with different directions, then the search fail, we set all elements along the way to 0. Because 0 is fail for sure so when later search meet 0 we know the search will fail.


# Question: Is there a need to use fast slow pointer, why not just set visited indices to 0? (array does not have any 0s set)
# Answer: If you just set all visited to indices to zero, you have no way to differentiate between elements you've visited in the current iteration of i (in which case seeing the same element twice means you have a loop) and elements you've visited in a prior iteration of i (in which case you can exit early as is done in the code here).
# The fast->slow loop iteration is a good way to test for a loop without using any extra storage to store a state.