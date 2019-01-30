
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.sqrt((2 * n) + 0.25)-0.5)



# Logic is
# n < = (x(x+1))/2 : Example if there are 8 coins then there are only 3 full rows possible 1,2,3.
# Remianing is 2 in 4th row which can be discarded

# 2n <= x(x+1)
# Add 1/4 both sides
# 2n + 1/4 <= x(x+1) + 1/4
# 2n +0.25 <= (x + 1/2)sq


########## Balaji #################

class Solution_(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        size = 1
        while ((n - size) >= 0):
            n = n - size
            count += 1
            size += 1

        return count
########################################
