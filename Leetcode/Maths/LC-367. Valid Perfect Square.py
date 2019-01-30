


class Solution(object):

    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return 0

        left = 0
        right = num

        while left <= right:

            mid = left + (right - left) // 2
            if mid ** 2 == num:
                return True

            elif mid ** 2 > num:
                right = mid - 1
            else:
                left = mid + 1

        return False

    # Same as LC-069 : Use Binary Search to find if sqaure of mid point is greater or less than given number

    def isPerfectSquare_(self, num):

        if num == 0:
            return 0

        l, h = 1, num
        while l < h:
            mid = (l + h) / 2
            if mid * mid == num:
                return True
            if mid * mid > num:
                h = mid - 1
            else:
                l = mid + 1

        return l * l == num
