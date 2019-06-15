
# Tags: String, Backtracking, Google, FB, AWS, Uber

# Given a string containing digits from 2-9 inclusive, return all possible letter
# combinations that the number could represent.
# A mapping of digit to letters (just like on the telephone buttons) is given below.
# Note that 1 does not map to any letters.
#
# Example:
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        numletter = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
        }

        letters = [numletter[i] for i in digits] # list comprehension
        if digits:
            if len(digits) == 1:
                return letters
            else:
                return reduce((lambda x, y: [i + j for i in x for j in y]), letters)# Note i+j is concatenation
        else:
            return []

    def letter_Combinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        numletter = { 2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz' }
        if digits is None: return 0

        for i in range(len(digits)):
            for j in range(len(numletter[i])):
                pass



if __name__ == '__main__':

    digits = [2,3,5]
    s = Solution()
    print "\nLetter Combintion:\n", s.letterCombinations(digits)
