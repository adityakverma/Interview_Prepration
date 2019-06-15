
# S and T are strings composed of lowercase letters. In S, no letter occurs more than once.
#
# S was sorted in some custom order previously. We want to permute the characters of T so
# that they match the order that S was sorted. More specifically, if x occurs before y in S,
# then x should occur before y in the returned string.
#
# Return any permutation (order matters) of T (as a string) that satisfies this property.
# Example :
# Input:  S = "cba", T = "abcd"
# Output: "cbad"
# Explanation:
# "a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a".
# Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda"
# are also valid outputs.
# -------------------------------------------------------------------------------------------

class Solution():

    def customSortString(self,S, T):
        d = dict()
        res = ''

        for letter in T:
            if letter in d:
                d[letter] += 1
            else:
                d[letter] = 1
        for letter in S:
            if letter in d:
                res += letter * d.pop(letter)
        for key in d:
            res += key * d[key]
        return res

    def customSortString2(self, S, T):
        ans = []
        while S:
            ele = S[0]
            ind = T.find(ele)
            while ind!=-1:
                ans.append(T[ind])
                T = T[:ind]+T[ind+1:]
                ind = T.find(ele)
            S = S[1:]
        ans.extend(list(T))
        return ''.join(ans)


if __name__ == '__main__':
    s = Solution()
    source = "cba"
    target = "abcd"
    print "\nCustom Sort:",s.customSortString(source,target)