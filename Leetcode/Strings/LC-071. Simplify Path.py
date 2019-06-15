
# Tags: Strings, Stack, FB, MS

# Given an absolute path for a file (Unix-style), simplify it.
# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
# Corner Cases:
#
#     Did you consider the case where path = "/../"?
#     In this case, you should return "/".
#     Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
#     In this case, you should ignore redundant slashes and return "/home/foo".
import collections

class Solution():  # Aditya
    def simplifyPath(self, path):
        stack = []
        path = path.split('/')
        for token in path:
            # print "Cuurent Stack:", stack
            if token in ('', '.'):
                pass # or continue
            elif token == '..':
                if stack: stack.pop()
            else:
                stack.append(token)
                # print "Appended",stack
        return '/' + '/'.join(stack)

    #----------------------------------------------
    # https://leetcode.com/problems/simplify-path/discuss/25794/Python-easy-to-understand-solutions-with-stack-and-deque.

    # with stack
    def simplifyPath1(self, path):
        stack = []
        for item in path.split("/"):
            if item not in [".", "..", ""]:
                stack.append(item)
            if item == ".." and stack:
                stack.pop()
        return "/" + "/".join(stack)

    # with deque
    def simplifyPath2(self, path):
        deque = collections.deque()
        for item in path.split("/"):
            if item not in [".", "..", ""]:
                deque.append(item)
            if item == ".." and deque:
                deque.pop()
        return "/" + "/".join(deque)
    #-------------------------------------------------

if __name__ == '__main__':
    s = Solution()
    path = "/a/./b/../../c/d"
    print "\nFinal path:",s.simplifyPath(path)



