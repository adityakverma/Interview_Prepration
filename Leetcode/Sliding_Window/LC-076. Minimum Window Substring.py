

# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

# Example:
#
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
#
# Note:
#
#     If there is no such window in S that covers all characters in T, return the empty string "".
#     If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
# ==============================================================================================================

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        i, j = 0, 0  # i and j are like start and end pointers. both moving in same directions from start
        n = len(s)
        res, = "#"

        miss = len(set(t))
        freq = collections.Counter(t)  # Tells freq of each element in target string. As we keep finding them in window, we reduce count
        # Note: Througout freq is just for reference for comparing w/ sofar. This counter doesn't change.

        sofar = collections.defaultdict(int)  # Tell the elements found so far in targrt which are match in window. If sofar[s[j]] equals
        # freq[s[j]], that means we can reduce miss count. sofar will change unlike freq (counter)

        # STEP-01: Iterate from start till end of string - to find suitable window.
        while j < n:

            # STEP-02: If we still have elements from taget to be found and current ele is in freq, so increment sofar.
            # AND if sofar count for that element is equal to count in freq, then reduce miss.

            if miss and s[j] in freq:  # miss tells how many characters of target are still missing in S. Id miss=0 window found.
                sofar[s[j]] += 1
                if sofar[s[j]] == freq[s[j]]:
                    miss -= 1
            j += 1  # Move the right pointer. Widening the window.
            # print "Miss", miss, "freq: ", freq, "sofar: ", sofar


            # STEP-03: Once some window is found which has all elements from t in s, then only we enter this while loop
            # and try to reduce window size.

            while i <= j and not miss:  # If miss=0 from above 'if' block that whole target has been found in some window

                # Step-3A: Try updating result to minimum window where miss==0
                if res == "#" or len(res) > len(s[i:j]):
                    res = s[i:j]  # Update res, ensuring we have minimum window, which contains all elements of target.

                # Step-3B: Basically if start element s[i] is part of freq, and nothing is missing, try reducing sofar - in the
                # hope we don't anything from target. Its basically an attempt to reduce window. But if  if
                # sofar[s[i]] == freq[s[i]] - 1  that means we are loosing elements so we increment miss.

                if s[i] in freq:
                    sofar[s[i]] -= 1  # This is like moving the window
                    if sofar[s[i]] == freq[
                        s[i]] - 1:  # But if while reducing window, we loose target element , then increment miss
                        miss += 1
                i += 1

        return "" if res == "#" else res


# # https://leetcode.com/problems/minimum-size-subarray-sum/discuss/59110/O(N)-template-for-Minimum-Size-Subarray-Sum-and-Minimum-Window-Substring-and-Longest-Substring-Without-Repeating-Characters

'''
    For example

e.g. S = "ADOBECODEBANC", T = "ABC"
          ADOBEC 
	         BECODEBA 
               CODEBA
                   BANC
The substrings above are candidates for the result. So the answer is BANC which is minimum in size.


#  The algorithm has two major phases.
#     Find the first window that contains all letters in t;
#     Keep expanding the window to the right by 1 char at a time, reducing left side if possible.

#     The best part is to make sure that THE ACTIVE WINDOW ALWAYS CONTAINS ALL LETTERS IN t.
#     In this case, every time the window is expanded, only the new char need to be checked.
'''



