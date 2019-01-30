
# LC Numbers for BackTracking Problems
# 10 17 22 79  46 78 126 140 211 44 47 357 401 351 36 37 39 40 60
# 51 77 216 212 254 90 526 425 784 320 89 842 411 131 267

class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.children = {}
        self.isWord = False


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class BT_Revisit():

    def LC046_Permutation(self,s):  # CORRECT SOLUTION
        if s is None:    # Boundry condition
            return 0

        res =[]
        self.backtrack_LC046(s, 0, res)
        return res

    def backtrack_LC046(self, s, start, res):
        if start == len(s):
            print s[:]
            # res.append(s[:])
            return
        for x in range(start,len(s)):
            s[start], s[x] = s[x], s[start] # Choose
            self.backtrack_LC046(s, start+1, res)
            s[start], s[x] = s[x], s[start] # Un-choose

    # ------------------------------------------------
    # Somehow this method of append and pop doesn't work so follow above one.
    def LC046_Permutation_(self, s):
        if s is None:  # Boundry condition
            return 0

        res = []
        self.backtrack_LC046_(s, 0, [])
        return res

    def backtrack_LC046_(self, s, i, cur):
        if i == len(s):
            print cur
            # res.append(s[:])
            return
        for x in range(i, len(s)):
            cur.append(s[x])
            self.backtrack_LC046_(s, i + 1, cur) # change i+1 to x+1 and it gives LC 78
            cur.pop()

    ################################################################

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
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
            self.backtrack_LC017(digits, i + 1, cur, result)  # this will help with 2nd position - all possibilities (d,e,f) -  ad, ae, af
            cur.pop()

    ################################################################

    def Dice_rolling(self,num_of_dice):
        if num_of_dice == 0: return 0
        self.backtrack_dice(num_of_dice,0, [])

    def backtrack_dice(self,n,start, cur):
        options = [1,2,3,4,5,6]

        #print "CUR..",cur
        if start == n:   # n indicates max appends won't increase beyond this number. Once append reached to count n then it will return for back visit. Other combinations will available throught regular recusrive calls and back visits
            print (cur)
            return

        for c in options:
            cur.append(c)
            #print "Appending",c,cur
            self.backtrack_dice(n, start+1, cur)
            cur.pop()
            #print "Pop", c, cur

    ################################################################

    def Binary_Combinations(self, num_of_options):
        res = []
        if num_of_options < 1: return 0
        self.backtrack_BinaryCombo(num_of_options, 0, [],res)
        #retrun res

    def backtrack_BinaryCombo(self, n, i, cur,res):
        options = [0,1]
        if i == n:
            print cur
            #res.append(''.join(cur))
            return
        for c in options:
            cur.append(c)
            self.backtrack_BinaryCombo(n, i+1, cur,res)
            cur.pop()

    ################################################################

    def LC078_Subsets(self,nums):
        res = []
        if len(nums) < 1:
            return 0
        self.backtrack_LC078(nums,0, [])

    def backtrack_LC078(self, nums, i, cur):
        print cur[:],  # No if condition, since we need all possibilities  unlike LC-46
        for c in range(i,len(nums)):
            cur.append(nums[c])
            self.backtrack_LC078(nums, c+1, cur) # IMP: change i+1 to c+1 to get correct answer. Else you get re-arrangement with dups.
            cur.pop()

    ################################################################

    def LC022_GenerateParentheses(self,n): # Sounds like 2 dice problem. BTW we did LC20. Valid Parenthesis before
        res = []
        if n < 1:
            return 0
        self.backtrack_LC022(n,0,[])

    def backtrack_LC022(self,n,i,cur):
        options = ['(',')']
        if i == 2*n:
            if self.isvalidParenthesis(cur):
                print ''.join(cur),
            return

        for ch in options:
            cur.append(ch)
            self.backtrack_LC022(n,i+1,cur)
            cur.pop()

    def isvalidParenthesis(self, s): #LC-020
        stack = []         # Basically we are treating list as stack here and using list functions like append(), pop().
        match = {'(': ')'}

        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            elif not stack or match[stack.pop()] != c:
                return False
        return not stack

    ################################################################

    # Algorithm: Here we check each letter of word with letter on board.
    # If they keep matching and not visited ( ofcourse within boundary & not visited) ..
    # then keep checking other letters for match recursively using Backtracking
    # technique [ choose, recursion call, unchoose].
    # Eventually we are out of all letters of word and all have matched,
    # so return TRUE meaning word is present.

    # For matching technique: We shift word using word[1:] and try for matching
    # via check word[0] != board[i][j]. If both word[0] and board[i][j] match
    # keeping doing recusrive call (Backtracking) till you reach to end of word.

    class LC079_WordSearch(object):   # ACCEPTED

        def exist(self, board, word):
            """
            :type board: List[List[str]]
            :type word: str
            :rtype: bool
            """
            if not board:
                return False

            for i in xrange(len(board)):
                for j in xrange(len(board[0])):
                    if self.dfs(board, i, j, word):
                        return True
            return False

        # check whether can find word, start at (i,j) position
        # Note there only two places where this function can return.
        # 1. It can return TRUE if whole word is matched successfully
        # 2. Or it returns FALSE if meets boundary cond or mismatch or already visisted - In this case keep checking for other i and j's
        def dfs(self, board, i, j, word):

            if len(word) == 0:  # all the characters are checked
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
                return False

            tmp = board[i][j]  # first character is found, check the remaining part

            board[i][j] = "#"  # avoid visit agian
            # check whether can find "word" along one direction
            res = self.dfs(board, i + 1, j, word[1:]) or self.dfs(board, i - 1, j, word[1:]) \
                  or self.dfs(board, i, j + 1, word[1:]) or self.dfs(board, i, j - 1, word[1:])
            board[i][j] = tmp

            return res

    ########## Just keep below for reference - but above is good and got accepted ################

    def LC079_WordSearch(self, board, word):
        if not board:
            return False

        visited = [[False for i in range(len(board))] for j in range(len(board[0]))]  # this can avoid double visiting

        for i in range(len(board)):
            for j in xrange(len(board[0])):
                if self.dfs_079(board, word, visited, i, j): # If helper function returned False, then keep checking for other values of i & j.
                    return True
        return False

    # Note there only two places where this function can return.
    # 1. It can return TRUE if whole word is matched successfully
    # 2. Or it returns FALSE if meets boundary cond or mismatch or already visisted - In this case keep checking for other i and j's

    def dfs_079(self, board, word, visited, i, j):

        if not word:  # If done checking all letters of word (via word[1:]), then return true.
            return True # Only when complete word is matched then ONLY this function will return TRUE

        # Boundary check. NOTE:  In below, if visited[i][j] = true then we cannot consider it
        # again for matching (word[0] == board[i][j]). So retun False for that DFS call.
        if i < 0 or i == len(board) or j < 0 or j == len(board[0]) \
                or visited[i][j] \
                or word[0] != board[i][j]:  # This is important check.
            return False # If for above reason found, it returns FALSE then we check for other i and j values.

        visited[i][j] = True  # mark current position as visited. # this can avoid double visiting aka looping
        res = self.dfs_079(board, word[1:], visited, i + 1, j) or \
              self.dfs_079(board, word[1:], visited, i - 1, j) or \
              self.dfs_079(board, word[1:], visited, i, j - 1) or \
              self.dfs_079(board, word[1:], visited, i, j + 1)  # This checks in all neighbouring cells of board, if next letter of word is present or not.
        visited[i][j] = False  # backtrack

        return res

        # Note: word[1:] creates a new string from the 1st character in word to
        #  its end. For example, if you begin with word="hello", then calling
        # word[1:] will create a new string, "ello". As this process repeats
        # itself, you get a smaller and smaller string.

    ######################################################################

    def __init__(self):
        self.root = TrieNode()
        self.result = []

    def insert(self, word):
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.isWord = True

    # Algorithm: Create/Populate Trie DS with list of given words.
    # Pick letter from Board; and for each letter from board do
    # lookup in Trie recursively using Backtracking technique in
    # all directions.
    # Now, if letter from board matches, keep appending to empty string
    # and keep doing recursive calls ( following BT techniques ) until
    # isWord is true ( word completes as per Trie) - then append word to
    # result list. [Aditya]

    # Compared to LC-079 - This time we don't pass word or list of words,
    # instead we pass root of Trie, since we have populated a Trie from words.
    def LC212_WordSearchII(self, board, words): # Tries
        for w in words:
            self.insert(w)  # Make a Trie for each word in list.

        for j in range(len(board)):
            for i in range(len(board[0])):
                self.dfs_212(self.root, board, j, i)
        return self.result

        # [Aditya]: So basically in this dfs function, we pick the character from
        # board and seeing if it's in Trie's child (not none). If not none then look
        # for next char from board and see if that also matches with next child within
        # Trie and so on.
        # While doing this, keep checking if flag, is set for that word (created so
        # far via appending). If flag is set or true, that means word
        # from trie is present in board, so append that valid word to result list

    def dfs_212(self, node, board, j, i, word=''):

        if node.isWord: # 1st check if isWord is TRUE, then word is present in board, so append to result.
            self.result.append(word) # Appending word to 'result list' once flag isWord sets to True (meaning complete word is found).
            node.isWord = False

        if 0 <= j < len(board) and 0 <= i < len(board[0]): # 2nd check if within boundry condition

            char = board[j][i]  # Pick the char from board[][] AND check that char in Trie which we have build. If its non none , meaning char from board is present in board, then keep looking for other via DFS
            child = node.children.get(char)  # Using Get() method for dictionaries # So basically we picked the character from board and seeing if it's in Trie's child (not none). If not None ( meaning its present) then look for next char from board and see if that also matches with next child within Trie and so on.

            # print "child", char, child
            if child is not None:
                # print child, char
                word += char
                # print ".....",word

                # BACKTRACKING technique for searching - 1. choose option , 2. make recursice call with that option and check for solution 3. then unchoose ( if not found solution, so choose next option again in future).
                board[j][i] = None  # Since as per problem, letters may not be used more than once in a word.
                self.dfs_212(child, board, j + 1, i, word)
                self.dfs_212(child, board, j - 1, i, word)
                self.dfs_212(child, board, j, i + 1, word)
                self.dfs_212(child, board, j, i - 1, word)
                board[j][i] = char

    ################################################################

    def LC010_RegularExpressionMatching(self):
        pass

    ################################################################

    def LC044_WildcardMatching(self):
        pass

    ################################################################

    def LC140_WordBreakII(self):
        pass

    ################################################################

    def LC126_WordLadderII(self):  # GRAPH ; NOT BACKTCKING
        pass

    ################################################################

    #60. Permutation Sequence  https: // leetcode.com / problems / permutation - sequence /
    def getPermutation(self, n, k):
        nums = [str(i) for i in range(1, n + 1)]
        fact = [1] * n
        for i in range(1, n):
            fact[i] = i * fact[i - 1]
        k -= 1
        ans = []
        for i in range(n, 0, -1):
            id = k / fact[i - 1]
            k %= fact[i - 1]
            ans.append(nums[id])
            nums.pop(id)
        return ''.join(ans)

    ################################################################

    #131. Palindrome Partitioning  https: // leetcode.com / problems / palindrome - partitioning /
    def partition(self, s):
        def backtrack(start, end, tmp):
            if start == end:
                ans.append(tmp[:])
            for i in range(start, end):
                cur = s[start:i + 1]
                if cur == cur[::-1]:
                    tmp.append(cur)
                    backtrack(i + 1, end, tmp)
                    tmp.pop()

        ans = []
        backtrack(0, len(s), [])
        return ans

    ################################################################

    def LC089_GreyCode(self):
        pass

    ################################################################

    def LC051_nQueen(self):
        pass

    ################################################################

    # LC-077
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.backtrack(n, k, 1, [], res)
        return res

    def backtrack(self, n, k, start, cur, res):

        if k == len(cur):
            res.append(copy.deepcopy(cur))  # Deep copy, else its all empty
            return  # backtracking

        for i in range(start,
                       n + 1):  # Note here we are not starting from 1 everytime, instead we are using 'start', which is actually i+1
            cur.append(i)  # Choose
            self.backtrack(n, k, i + 1, cur, res)
            cur.pop()  # Un-choose

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class Solutions2():

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.isWord = True

    def search(self, word):
        node = self.root
        for i in word:
            if i not in node.children:
                return False
            node = node.children[i]
        return node.isWord

    # We first check whether current prefix is in dictionary. Then we
    # recursively check for remaining string s[i:len(s)] which is suffix
    # of length size-i. This is not BT, but simple recursion.

    def LC139_WordBreak(self, s):  # TRIE

        if len(s) == 0:
            return True

        for i in range(1, len(s) + 1):  # Reason you need to do till len(s)+1 because in slicing we consider till one letter before in s[0:i]. So we'll never get last word. eg: google will always be googl if its s[0:i]
            if self.search(s[0:i]) and self.LC139_WordBreak(s[i:len(s)]):
                return True
        return False

    ################################################################



# All above problesm + Review that document which is Summary of Backtracking; though most of these already here.
if __name__ == '__main__':
    s = BT_Revisit()

    #--------------------------------------------------
    str1 = "ABC"
    LC46 = list(str1) # OR say    str = ['A', 'B', 'C']
    #print s.LC046_Permutation(LC46)
    #print s.LC046_Permutation_(LC46) # Doesn't work as expected. We need to use SWAP method
    #--------------------------------------------------
    LC017 = [2,3]
    #print s.LC017_letterCombinations(LC017)
    #--------------------------------------------------
    #print s.Dice_rolling(2)
    #--------------------------------------------------
    print s.Binary_Combinations(2)
    #--------------------------------------------------
    LC078 = [1,2,3]
    #print s.LC078_Subsets(LC078) # Gives all re-arrangement with dups - Not correct
    #--------------------------------------------------
    #print s.LC022_GenerateParentheses(3)
    #--------------------------------------------------
    board = [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]

    word = "ABCCEDA"
    #print "\nWord Search: ", s.LC079_WordSearch(board,word)
    #--------------------------------------------------

    words_ = ["oath","pea","eat","rain"]
    board_ = [
                ['o','a','a','n'],
                ['e','t','a','e'],
                ['i','h','k','r'],
                ['i','f','l','v']
            ]
    #print "\nSolution : ", s.LC212_WordSearchII(board_, words_)
    #--------------------------------------------------

    s2 = Solutions2()
    arr = ["I", "work","at","Google","California"]

    for i in range(len(arr)):
        s2.insert(arr[i])
    print "\n I work at google: ",s2.LC139_WordBreak("IworkatGoogle")
    print "\n I work at Oracle: ",s2.LC139_WordBreak("IworkatOracle")

    #--------------------------------------------------
