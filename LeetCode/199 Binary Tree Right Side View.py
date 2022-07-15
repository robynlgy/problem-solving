# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ## have a levels list, but instead of keeping all levels, keep only the right-most one
        ## we can have the right-most one for each level if we did dfs from left to right

        levels = []

        def dfs(root,level):
            if not root:
                return
            if len(levels) == level:
                levels.append(root.val)
            else:
                levels[level] = root.val

            dfs(root.left,level+1)
            dfs(root.right,level+1)



        dfs(root,0)
        return levels



# [1,3,4,5]
#                   1
#               /       \
#            2           3
#         /    \
#       1       4
#      /
#     5