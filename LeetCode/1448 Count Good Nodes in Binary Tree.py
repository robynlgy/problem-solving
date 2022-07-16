# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

# Return the number of good nodes in the binary tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0

        count = [0]

        def dfs(root,max_val,count):
            if not root:
                return
            if root.val >= max_val:
                count[0] += 1

            dfs(root.left,max(max_val,root.val),count)
            dfs(root.right,max(max_val,root.val),count)


        dfs(root,root.val,count)
        return count[0]