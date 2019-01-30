
# Given a binary tree, find the length of the longest path where each
# node in the path has the same value. This path may or may not pass through the root.
#
# Note: The length of path between two nodes is represented by the
# number of edges between them.
#
# Example 1:
#
# Input:
#
#               5
#              / \
#             4   5
#            / \   \
#           1   1   5
#
# Output: 2
# -----------------------------------
# Example 2:
# Input:
#
#               1
#              / \
#             4   5
#            / \   \
#           4   4   5
#
# Output:2


# https://leetcode.com/problems/longest-univalue-path/discuss/108142/Python-Simple-to-Understand

# The approach is similar to the Diameter of Binary Tree question except that we reset the left/right to 0 whenever the current node does not match the children node value.

class Solution(object):

    def longestUnivaluePath(self, root):

        self.ans = 0

        def arrow_length(node):

            if not node: return 0

            left_length = arrow_length(node.left) # This goes all the wat to bottom of tree (leaf) and then it return recursively.
            right_length = arrow_length(node.right)

            if node.left and node.left.val == node.val:
                left_arrow = left_length + 1
            else:
                left_arrow = 0 # Reset value if its not continous

            if node.right and node.right.val == node.val:
                right_arrow = right_length + 1
            else:
                right_arrow = 0

            self.ans = max(self.ans, left_arrow + right_arrow)

            return max(left_arrow, right_arrow)

        arrow_length(root)
        return self.ans

# --------------------------------------------------------------------------
    # Time Complexity: O(N), where N is the number of nodes in the tree.
    # We process every node once.
    #
    # Space Complexity: O(H), where H is the height of the tree. Our
    # recursive call stack could be up to HHH layers deep.
# --------------------------------------------------------------------------
