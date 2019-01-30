
###############################################################
# Python union find solution

# Similar to idea provided in : https://www.youtube.com/watch?v=0jNmHPfA_yE
# Or ideas given by Mapara.

class UnionFind(object):
    def __init__(self, grid):
        self.n = len(grid)
        self.parent = [-1] * self.n  # Giving original IDs. Like Mapara's idea.
        for idx in xrange(self.n):
            self.parent[idx] = idx

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            self.parent[rooty] = rootx

    def diff_groups(self):
        diff_groups = set()
        for i in xrange(self.n):
            diff_groups.add(self.find(i))  # Adding unique IDs from Parent. Remeber Mapara's Idea.
        return len(diff_groups)

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        uf = UnionFind(M)

        for i in xrange(n):
            for j in xrange(n):
                if M[i][j] == 1:
                    uf.union(i, j)

        return uf.diff_groups()


###############################################################

class Solution1(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """

        def dfs(M,i,visited):
            visited[i] = True
            for j in range(len(M[0])):
                if(M[i][j] == 1 and not visited[j]):
                    dfs(M,j,visited)

        visited = [False]*len(M)
        res = 0

        for i in range(len(M)):
            if(not visited[i]):
                dfs(M,i,visited)
                res +=1

        return res

###################################################################

