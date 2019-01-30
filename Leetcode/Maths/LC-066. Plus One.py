
class Solution(object):

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        """ 
        s = ""
        for i in digits:
            s += str(i)     # concatenate each of the list element into string. Here 's' is sting

        s = int(s)          # now 's' is typecasted to integer so that we can add 1
        #print s
        return [int(i) for i in str(s + 1)] 
        """

        # Follow up - Do without typecasting

        num = 0
        for i in range(len(digits)):
            num += digits[i] * pow(10, (len(digits) - 1 - i))

        return [int(i) for i in str(num + 1)]

if __name__ == '__main__':
    A = [1,2,9]
    print A
    myobject = Solution()
    print myobject.plusOne(A)