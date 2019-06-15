
# Compare two version numbers version1 and version2.
# If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.
#
# You may assume that the version strings are non-empty and contain only digits and the . character.
# The . character does not represent a decimal point and is used to separate number sequences.
# For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.
#
# Example 1:
#
# Input: version1 = "0.1", version2 = "1.1"
# Output: -1
#
# Example 2:
#
# Input: version1 = "1.0.1", version2 = "1"
# Output: 1
#
# Example 3:
#
# Input: version1 = "7.5.2.4", version2 = "7.5.3"
# Output: -1

class Solution(object):

    ########################################################

    def compareVersion1(self, v1, v2): # Good
        versions1 = [int(v) for v in v1.split(".")] # [7, 5, 2, 4]
        versions2 = [int(v) for v in v2.split(".")]
        #versions3 = v1.split(".")
        #print versions1, versions2, versions3
        for i in range(max(len(versions1), len(versions2))):
            v1 = versions1[i] if i < len(versions1) else 0
            v2 = versions2[i] if i < len(versions2) else 0
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0

    def compareVersion11(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.') # ['7', '5', '2', '4']
        v2 = version2.split('.')
        l1, l2 = len(v1), len(v2)
        for i in xrange(max(l1, l2)):
            ver1 = int(v1[i]) if i < len(v1) else 0
            ver2 = int(v2[i]) if i < len(v2) else 0
            if ver1 > ver2:
                return 1
            elif ver1 < ver2:
                return -1
        return 0

    #######################################################
    # https://leetcode.com/problems/compare-version-numbers/discuss/50968/Share-my-AC-python-solution.
    def compareVersion2(self, version1, version2): # Nice trick using while loop
        num1 = version1.split('.')
        num2 = version2.split('.')
        while (len(num1) or len(num2)):
            if (len(num1) == 0):
                num1 = [0]
            elif (len(num2) == 0):
                num2 = [0]
            else:
                i1 = int(num1[0])
                i2 = int(num2[0])
                if (i1 < i2):
                    return -1
                elif (i1 > i2):
                    return 1
                else:
                    num1 = num1[1:]
                    num2 = num2[1:]
        return 0

    #######################################################
    def compareVersion(self, version1, version2):

        v1 = map(int,version1.split("."))
        v2 = map(int,version2.split("."))
        if len(v1) < len(v2):
            v1.extend([0]*(len(v2)-len(v1)))
        else:
            v2.extend([0]*(len(v1)-len(v2)))
        return cmp(v1,v2)

    #######################################################

    def compareVersion3(self, version1, version2): # Aditya: Runs but fails few tests
        i = j = 0
        v_1 = v_2 = " "
        for i in range(len(version1)):
            if not version1[i].isalnum():
                i += 1
            else:
                v_1 += version1[i]

        for j in range(len(version2)):
            if not version2[j].isalnum():
                j += 1
            else:
                v_2 += version2[j]

        if v_1 > v_2: return 1
        elif v_1 < v_2: return -1
        else: return 0

if  __name__ == '__main__':
    v1 = "7.5.2.4"
    v2 = "7.5.3"

    s = Solution()
    print "\nIs Version1 greater than Version2:",s.compareVersion1(v1,v2)
    print "\nIs Version1 greater than Version2:",s.compareVersion2(v1,v2)

