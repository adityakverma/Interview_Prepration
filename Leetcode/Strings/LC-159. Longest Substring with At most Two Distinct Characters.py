
# Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.
#
# Example 1:
#
# Input: "eceba"
# Output: 3
# Explanation: t is "ece" which its length is 3.
#
# Example 2:
#
# Input: "ccaabbb"
# Output: 5
# Explanation: t is "aabbb" which its length is 5.
#####################################################################################

# Approach 1: Sliding Window
# Intuition
# To solve the problem in one pass let's use here sliding window approach with two set pointers left and right serving as the window boundaries.
# The idea is to set both pointers in the position 0 and then move right pointer to the right while the window contains not more than two distinct characters. If at some point we've got 3 distinct characters, let's move left pointer to keep not more than 2 distinct characters in the window.

# See article saved

class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict

        n = len(s)
        if n < 3:
            return n

        # sliding window left and right pointers
        left, right = 0, 0
        # hashmap character -> its rightmost position
        # in the sliding window
        hashmap = defaultdict()

        max_len = 2

        while right < n:
            # slidewindow contains less than 3 characters
            if len(hashmap) < 3:
                hashmap[s[right]] = right
                right += 1

            # slidewindow contains 3 characters
            if len(hashmap) == 3:
                # delete the leftmost character
                del_idx = min(hashmap.values())
                del hashmap[s[del_idx]]
                # move left pointer of the slidewindow
                left = del_idx + 1

            max_len = max(max_len, right - left)

        return max_len

#

 #   Time complexity : O(N)\mathcal{O}(N)O(N) where N is a number of characters in the input string.

 #   Space complexity : O(1)\mathcal{O}(1)O(1) since additional space is used only for a hashmap with at most 3 elements.

#---------------------------------------------------------------------

class Solution_(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int

        Worst case time and space complexity:
        Time: O(N), Space: O(W) where N is size of string and W is size of max window
        """
        # Initialize sliding window and counts of chars in the window
        left = 0
        right = 0
        counts = collections.defaultdict(int)

        # Slide the window down the string until we reach the end
        #
        # Loop invariant:
        # (1) The previously seen window is s[left:right]
        # (2) The right index - left index of window is always the length
        #     of the longest substring with <= 2 distinct characters
        while right < len(s):
            # Slide the right end up and update counts such that the window is now s[left:right+1]
            counts[s[right]] += 1
            right += 1

            # If the window has more than 2 characters, slide the left end of
            # the window up and update counts such that the window is now s[left+1:right+1]
            if len(counts) > 2:
                counts[s[left]] -= 1
                if not counts[s[left]]:
                    del counts[s[left]]
                left += 1

        # The length of the window is the length of the longest valid substring
        return right - left


# --------------------------------------------------------------------

from collections import OrderedDict


class Solution(object):

    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int

        Runtime: O(n)
        Space: O(min(k, 26))

        """

        seen = OrderedDict()
        start = max_length = 0
        end = 1
        max_substring = ''

        for i, char in enumerate(s):

            # If the character is already in seen,
            # we want to move it to the end then
            # update its value to rightmost index.
            if char in seen:
                seen.move_to_end(char, last=True)
            seen[char] = i

            if len(seen) > k:
                # popitem() is O(1) because OrderedDicts
                # are doubly linked lists.
                _, start = seen.popitem(last=False)
                start += 1

            if max_length < (end - start):
                max_length, max_substring = end - start, s[start:end]
            end += 1

        return max_length

