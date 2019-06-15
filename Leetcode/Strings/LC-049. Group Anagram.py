
# Tags: Strings, Hash Table, FB, AWS, Uber

# Given an array of strings, group anagrams together.
# Note: An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.  for example, the word binary can be rearranged into "brainy".

# Example:
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

# Other Similar questions:
#   49	Group Anagrams
# 	242	Valid Anagram
# 	438	Find All Anagrams in a String
# 	760	Find Anagram Mappings
# 	839	Similar String Groups

# -------------------------------------------------------------------------------



class Solution(object):

    # The idea is to use the sorted string as the key. by the way, it is shorter to rewrite if-else in one statement.
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for str in strs:
            print "str", str, sorted(str) # Understand how sorted works. It works on both list and string and output is list form: https://www.programiz.com/python-programming/methods/built-in/sorted

            key = ''.join(sorted(str))
            print key
            if key in dic:
                dic.get(key).append(str)
            else:
                dic[key] = [str]
        return dic.values()


    def groupAnagrams_Balaji(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash_table = {}
        if not strs:
            return []
        for val in strs:
            temp = "".join(sorted([v for v in val]))
            # print "temp", temp
            if temp in hash_table:               # OR hash_table.keys()
                hash_table[temp].append(val)
            else:
                hash_table[temp] = [val]

        ans = hash_table.values()
        return ans



if __name__ == '__main__':
    input = ["eat", "tea", "tan", "ate", "nat", "bat"]
    s = Solution()
    print "\nGrouping Anagrams: \n",s.groupAnagrams_Balaji(input)
    print "\nGrouping Anagrams: \n",s.groupAnagrams(input)

# Time Complexity:
# is it O(n*mlogm)?
# n = len(strs), m = len(strs[0])


