

def reverseBits(self, n):
    ans = 0
    for i in xrange(32):
        ans = (ans << 1) + (n & 1)
        n >>= 1
    return ans

# Just generate the answer bit by bit, do not use things like "% 2" or "2 ** k" or "bin". Bit manipulation is a lot faster. One small thing is the plus operator can be replaced by "bitwise or", aka "|". However i found plus is more readable and fast in python.
