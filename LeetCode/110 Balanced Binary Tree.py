# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as:

# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        res = [True]

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left) #1
            right = dfs(root.right) #1

            if abs(left - right) >  1:
                res[0] = False

            return 1+max(left,right)

        dfs(root)

        return res[0]

