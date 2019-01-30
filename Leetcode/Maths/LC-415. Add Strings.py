

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        n1 = n2 = 0
        num1 = list(num1)  # Convert string to list
        num2 = list(num2)

        for i in range(len(num1)):
            n1 += num1[i] * pow(10, (len(num1) - 1 - i))  # Convert list to proper number - same as LC-66

        for i in range(len(num2)):
            n2 += num2[i] * pow(10, (len(num2) - 1 - i))

        return str(n1 + n2)
