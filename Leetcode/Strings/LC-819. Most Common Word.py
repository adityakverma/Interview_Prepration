
# Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.
#
# Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.
#
# Example:
# Input:
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
# Output: "ball"
# Explanation:
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"),
# and that "hit" isn't the answer even though it occurs more because it is banned.
# --------------------------------------------------------------------------------

# [Algorithm]: Basically sentence needs to be :
# 1.converted to list via of space separated - .paragraph.split(" ")
# 2.converted to lowercase - paragraph.lower(),
# 3.all special char stripped - strip("!?',:.")
# 4.removed all banned words - words not in banned list
# 5.Count each kind of word using counter(), since its a list of words
# 6.and return most_common()

import collections
import re


class Solution(object):

    def mostCommonWord1(self, paragraph, banned): # My Solution
        word_list = []
        words = paragraph.lower().split(" ")  # Lower case & space separated list
        for word in words:
            word = word.strip("!?',;.")
            if word not in banned:      # if word after all cleansing is not from banned word, then add to new list
                word_list.append(word)
        return collections.Counter(word_list).most_common(1)[0][0]

    #-----------------------------------------------------------------------
    def mostCommonWord2(self, paragraph, banned): # Leetcode Official Solution
        banset = set(banned)
        count = collections.Counter(
            word.strip("!?',;.") for word in paragraph.lower().split())

        ans, best = '', 0
        for word in count:
            if count[word] > best and word not in banset:
                best = count[word] # Update best, or you can also use max function
                ans = word
        return ans

    # -----------------------------------------------------------------------
    # READ Notes of regular expressions - important topic
    def mostCommonWord3(self, p, banned):
        ban = set(banned)
        words = re.findall(r'\w+', p.lower()) # 'w' means only alphanumeric [a-zA-Z_0-9]. 'W' is non-alphanumeric
        print words
        return collections.Counter(w for w in words if w not in ban).most_common(1)[0][0]

    # -----------------------------------------------------------------------
    def mostCommonWord4(self, paragraph, banned):
        counts = collections.Counter(word.strip("!?',;.") for word in paragraph.lower().split())
        for ban in banned:
            del counts[ban]
        counts = counts.most_common()
        return counts[0][0]

    # -----------------------------------------------------------------------
    def mostCommonWord5(self, paragraph, banned):  # Good Solution. without collection.counter
        paragraph = paragraph.lower()
        banned = set(banned)

        lis = paragraph.split(' ')
        dic = {}
        for word in lis:
            word = word.strip("!?',;.")
            if word not in banned:
                if word not in dic:
                    dic[word] = 1
                else:
                    dic[word] += 1
        maximum = 0
        char = ""
        for key, val in dic.items():
            if val > maximum:
                maximum = val
                char = key
        return char


if __name__ == '__main__':
    s = Solution()
    sentence = "Bob hit a ball, the hit BALL flew far after it was hit." # string
    ban = ["hit"] # List[str]
    print "\nMost Common Word:",s.mostCommonWord1(sentence,ban)


# Test case:
# "Bob. hIt, baLl"
# ["bob", "hit"]
