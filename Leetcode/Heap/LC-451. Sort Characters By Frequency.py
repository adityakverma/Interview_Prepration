
from heapq import *
from collections import Counter

class Solution:

    # This is good solution, but in interview counter might not be accepted.
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        chars = Counter(s)
        #print chars.items()
        heap = []

        for c in chars:
            heappush(heap, (chars[c], c)) # This will help to maintain heap with least freq on top.

        output = ""
        while len(heap):
            c = heappop(heap)
            output += c[1] * c[0]
        return output[::-1] # Since minimum freq was popped before and we need more freq to lesser.

    # ---------------------------------------------------------------------------------------
    def frequencySort_(self, s):
        lst = list(s)  # Important - Converting Word to list so we can iterate on it.
        dct = {}
        newLst = []
        s1 = ''

        for i in lst:
            dct[i] = dct.get(i, 0) + 1

        for key, value in list(dct.items()):  # converting Dict to list, so we can apply sort
            newLst.append((value, key))

        newLst.sort(reverse=True)  # Note this is sort based on value, else we would have specified which key=newLst[1] not [0]

        for value, key in newLst:
            s1 = s1 + key * value

        return s1

if __name__ == '__main__':
    s = Solution()
    Input = "tree"
    print "\nSorted char by frequency: ", s.frequencySort(Input)
    print "\nSorted char by frequency: ", s.frequencySort_(Input)



############################################################################

'''
# Alternate Solution without using Counter

def frequencySort(self, s):
    
    lst = list(s) # Important - Converting Word to list so we can iterate on it. 
    dct = {}
    newLst = []
    s1 = ''
    
    for i in lst:
        dct[i] = dct.get(i,0)+1
    
    for key,value in list(dct.items()): # converting Dict to list, so we can apply sort
        newLst.append((value,key))
    
    newLst.sort(reverse=True) # Note this is sort based on value, else we would have specified which key=newLst[1] not [0]
    
    for value,key in newLst:
        s1 = s1 + key*value
        
    return s1

'''