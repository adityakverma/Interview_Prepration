# ==========================
# Tags: Array, Two Pointers
# ==========================
# https://leetcode.com/problems/container-with-most-water/discuss/6126/C++-O(n)-solution-with-thought-process-applying-simple-bucket-theory
# https://leetcode.com/problems/container-with-most-water/discuss/6131/O(N)-7-line-Python-solution-72ms
# Two pointer approach

class Solution():
    # Approach  (Two Pointer Approach)
    def maximumArea(self,height):
        i,j,result = 0, len(height)-1, 0
        while (i<j):
            result = max(result, min(height[i],height[j]) * (j-i))
            if(height[i]< height[j]):
                i +=1
            else:
                j -=1
        return result

    def maxArea(self, height):
        L, R, width, res = 0, len(height) - 1, len(height) - 1, 0
        for w in range(width, 0, -1):
            # We notice that to calculate the area, the height is really identified by the smaller number / shorter end between the two ends
            if height[L] < height[R]:
                res, L = max(res, height[L] * w), L + 1
                # So, as to find the next potential maximum area, we disregard the shorter end by moving it to the next position
            else:
                res, R = max(res, height[R] * w), R - 1
        return res


# driver function
if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    s = Solution()
    #print s. maxArea(height)
    print s. maximumArea(height)  # my solution

# Complexity Analysis
    # Time complexity : O(n). Single pass.
    # Space complexity : O(1). Constant space is used.