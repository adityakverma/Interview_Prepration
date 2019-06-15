
# Suppose you have a long flowerbed in which some of the plots are planted and some are not.
# However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

# Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.
#
# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: True ; Because we can plant '1' flowerbed here at index 2 ( if we are starting from index 0)
#
# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: False; Because we cannot plant '2' flowerbeds between index 1 to 3. It will violate the rule.


class Solution():

    # Accepted LC Solution
    def canPlaceFlowers_LC605(self, flowerbed, n): # All TC passes on LC. Accepted
        count = 0
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
                flowerbed[i] = 1
                count += 1
        return count >= n


    # My Solution, but fails TC-05
    def CanPlaceFlowers(self, nums, n): # Works, but all test cases don't pass
        count = max_count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
                max_count = max(max_count,count)
            else:
                count = 0

        if (max_count == (2*n + 1)) or ((nums[0] == 0 or nums[len(nums)-1] == 0) and max_count >= n):
            return True
        return False


if __name__ == '__main__':

    s = Solution()
    flowerbed1 = [1, 0, 0, 0, 0, 0, 1]  # TC-01
    flowerbed2 = [0, 0, 1, 0, 1]  # TC-02
    flowerbed3 = [1, 0, 0, 0, 1, 0, 0]
    flowerbed4 = [0, 0, 1, 0, 0]
    flowerbed5 = [1]
    n1 = 2
    n2 = 1
    n3 = 2
    n4 = 2
    n5 = 0
    # print "\nCan place flowers?",s.CanPlaceFlowers(flowerbed3,n3)
    print "\nCan place flowers?", s.canPlaceFlowers_LC605(flowerbed2, n2)