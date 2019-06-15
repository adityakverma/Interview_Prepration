

class Solution(object):

    def addBinary(self, a, b):
        return bin(int(a,2)+int(b,2))[2:] # #convert int to binary string, Eg : bin(5)->'0b101'


    # https://leetcode.com/problems/add-binary/discuss/24622/Python-solution-bit-manipulation-(58-ms-not-the-best-though)
    def addBinary1(self, a, b):

        temp_b = temp_a = 0
        x = int(a, 2)
        y = int(b, 2)
        loop = True

        while loop:
            temp_a = x & y  # carry
            temp_b = x ^ y  # sum
            x = temp_a << 1  # shifting the carry for each bit
            y = temp_b
            if (not temp_a):
                loop = False

        return bin(temp_b)[2:]

if __name__ == '__main__':
    a = "0110"
    b = "1000"
    s = Solution()
    print "\nAdding binary",s.addBinary(a,b)
    print "\nAdding binary",s.addBinary1(a,b)