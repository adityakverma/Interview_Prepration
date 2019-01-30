
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/8070/One-line-python-solution

class Solution(object):

    def letterCombinations(self, digits):

        result = []
        if len(digits) < 1:  # Base case
            return []

        self.backtrack_LC017(digits, 0, [], result)
        return result

    def backtrack_LC017(self, digits, i, cur, result):
        map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if i == len(digits):

            if len(cur) > 0:
                print ''.join(cur)
                result.append(''.join(cur))
            return  # Very Important, else it takes higher values of i and we get IndexError: list index out of range

        for ch in map[digits[i]]:
            cur.append(ch)  # this chooses first position example 'a' .. and then b,c later
            self.backtrack_LC017(digits, i + 1, cur,
                                 result)  # this will help with 2nd position - all possibilities (d,e,f) -  ad, ae, af
            cur.pop()

    # -------------------------------------------------------------------------------------------
    '''
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
        # for i in digits:
        #     print i, numletter[i],

        letters = [numletter[i] for i in digits] # list comprehension
        print letters
        if digits:
            if len(digits) == 1:
                return letters
            else:
                return reduce((lambda x, y: [i + j for i in x for j in y]), letters)# Note i+j is concatenation
        else:
            return []

    # -------------------------------------------------------------------------------------------
    def backtracking_letterCombinations(self, digits):
        dic = {
            1: '*', 2: 'abc', 3: 'def',
            4: 'ghi', 5: 'jkl', 6: 'mno',
            7: 'qprs', 8: 'tuv', 9: 'wxyz',
            0: ' '
        }

        def generate(segment, digits, letter=[]):
            #print digits
            #print "segment",segment
            if not digits:
                #print digits
                letter.append(segment)
                return []

            for i in dic[digits[0]]:
                #print "..",i
                generate(segment + i, digits[1:])
            return letter

        return generate('', digits)

    # -------------------------------------------------------------------------------------------
    # https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/8063/Python-solution

    def letterCombinations_BT(self, digits):
        map = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz' }
        result = []

        def make_combinations(i, cur):
            if i == len(digits):
                if len(cur) > 0:
                    result.append(''.join(cur))
                return
            for ch in map[digits[i]]:
                cur.append(ch)
                make_combinations(i + 1, cur)
                cur.pop()

        make_combinations(0, [])
        return result
    # -------------------------------------------------------------------------------------------

    '''

if __name__ == '__main__':

    digits = [2,3]
    s = Solution()
    print "\nLetter Combintion:\n", s.LC017_letterCombinations(digits)

    #print "\nLetter Combintion:\n", s.letterCombinations(digits)
    #print "\nBacktracking Letter Combintion:\n", s.backtracking_letterCombinations(digits)
    #print "\nBacktracking Letter Combintion:\n", s.letterCombinations_BT(digits)



































# https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/8067/Python-easy-to-understand-backtracking-solution.

# def letterCombinations(self, digits):
#     if not digits:
#         return []
#     dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
#     res = []
#     self.dfs(digits, dic, 0, "", res)
#     return res
#
#
# def dfs(self, digits, dic, index, path, res):
#     if len(path) == len(digits):
#         res.append(path)
#         return
#     for i in xrange(index, len(digits)):
#         for j in dic[digits[i]]:
#             self.dfs(digits, dic, i + 1, path + j, res)

#-----------

# https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/8063/Python-solution

# def letterCombinations(self, digits):
#         """
#         :type digits: str
#         :rtype: List[str]
#         """
#         interpret_digit = {
#             '1': '',
#             '2': 'abc',
#             '3': 'def',
#             '4': 'ghi',
#             '5': 'jkl',
#             '6': 'mno',
#             '7': 'pqrs',
#             '8': 'tuv',
#             '9': 'wxyz',
#             '0': ' '}
#         all_combinations = [''] if digits else []
#         for digit in digits:
#             current_combinations = list()
#             for letter in interpret_digit[digit]:
#                 for combination in all_combinations:
#                     current_combinations.append(combination + letter)
#             all_combinations = current_combinations
#         return all_combinations

