
# Given an array of characters, compress it in-place.
# The length after compression must always be smaller than or equal to the original array.
# Every element of the array should be a character (not int) of length 1.

# After you are done modifying the input array in-place, return the new length of the array.
# Follow up: Could you solve it using only O(1) extra space?
#
# Example 1:
# Input: ["a","a","b","b","c","c","c"]
# Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
#
# Explanation:
# "aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".

# Example 3:
#
# Input:
# ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
#
# Output:
# Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
#
# Explanation:
# Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
# Notice each digit has it's own entry in the array.

class Solution(object):

    # https://leetcode.com/problems/string-compression/discuss/122241/Python-solution-with-detailed-explanation
    # Algorithm :
    #     Maintain a rptr and wptr to write in-place.
    #     Use 2 while loops - outer loop rptr < len(chars) and inner loops counts the streak of common characters.
    #     Always write the character, but only write the frequency when it is more than 1. Note that when f = 12, we need to write two characters: "1" and "2".

    def compress2(self, chars):  # Other's solution
        """
        :type chars: List[str]
        :rtype: int
        """
        rptr, wptr = 0, 0
        while rptr < len(chars):
            ch, f = chars[rptr], 0
            while rptr < len(chars) and chars[rptr] == ch:
                rptr, f = rptr+1, f+1
            chars[wptr], wptr = ch, wptr + 1
            if f > 1:
                for c in str(f):
                    chars[wptr], wptr = c, wptr + 1
        return wptr

    def compress(self, chars):  # Leetcode Official
        anchor = write = 0
        for read, c in enumerate(chars):
            if read + 1 == len(chars) or chars[read + 1] != c:
                chars[write] = chars[anchor]
                write += 1
                if read > anchor:
                    for digit in str(read - anchor + 1):
                        chars[write] = digit
                        write += 1
                anchor = read + 1
        return write


    def compress1(self, chars): # Mine: Works buts its not in-place. Also fails few testcases
        dict = {}
        s = ""
        for i in chars:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1

        for i,j in dict.items():
            if j == 1:
                s += str(i)
            else:
                s += str(i)+ str(j) #+ dict.values()
        print s
        return len(s)

if __name__ == '__main__':
    s = Solution()
    input = ["a","a","b","b","c","c","c"] #["a","b","b","b","b","b","b","b","b","b","b","b","b"] # ["a","a","b","b","c","c","c"]
    print "\nCompressed length:",s.compress(input)


# ------------------------------------------------------------------
# https://leetcode.com/articles/string-compression/#

# Approach #1: Read and Write Heads [Accepted]
#
# Intuition
#
# We will use separate pointers read and write to mark where we are reading and
# writing from. Both operations will be done left to right alternately: we will
# read a contiguous group of characters, then write the compressed version to the
# array. At the end, the position of the write head will be the length of the
# answer that was written.
#
# Algorithm
#
# Let's maintain anchor, the start position of the contiguous group of characters
# we are currently reading.
#
# Now, let's read from left to right. We know that we must be at the end of the block
# when we are at the last character, or when the next character is different from the
# current character.
#
# When we are at the end of a group, we will write the result of that group down using
# our write head. chars[anchor] will be the correct character, and the length
# (if greater than 1) will be read - anchor + 1. We will write the digits of that number
#  to the array.
#
# Python
#
# class Solution(object):
#     def compress(self, chars):
#         anchor = write = 0
#         for read, c in enumerate(chars):
#             if read + 1 == len(chars) or chars[read + 1] != c:
#                 chars[write] = chars[anchor]
#                 write += 1
#                 if read > anchor:
#                     for digit in str(read - anchor + 1):
#                         chars[write] = digit
#                         write += 1
#                 anchor = read + 1
#         return write

# Complexity Analysis
#
#     Time Complexity: O(N), where NNN is the length of chars.
#     Space Complexity: O(1), the space used by read, write, and anchor.

# ------------------------------------------------------------------




