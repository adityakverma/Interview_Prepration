
class Solution(object):
    UPBOUND = 2147483647

    def splitIntoFibonacci(self, st):
        res = []
        if not st:
            return res
        self.util(st, res, [], 0)
        if res:
            return map(int, res[0])
        return res


    def util(self, st, res, sf, start):
        if start == len(st):
            if self.isFib(sf):
                res.append(sf[:])
                return
        for i in range(start, len(st)):
            if i - start > 10:
                return
            piece = st[start: i+1]
            if int(piece) > Solution.UPBOUND:
                return
            if piece.startswith("0") and start != i:
                return
            if len(sf) < 3 or self.isFib(sf):
                sf.append(piece)
                self.util(st, res, sf, i+1)#next start
                sf.pop()

    def isFib(self, arr):
        if len(arr) < 3:
            return False
        size = len(arr)
        return int(arr[size-1]) == int(arr[size-2]) + int(arr[size-3])


