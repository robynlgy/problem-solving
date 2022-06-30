#Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

#A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return False
        if not subRoot: return True

        if self.sameTree(root,subRoot):
            return True
        else:
            return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))



    def sameTree(self,root,subRoot):
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return self.sameTree(root.left,subRoot.left) and self.sameTree(root.right,subRoot.right)
        else:
            return False

    # prev had this return the node in the main tree to pass into sameTree as the `root`, but this does not account for if tree has same value nodes
        # def dfs(root):
        #     if not root:
        #         return None
        #     if root.val == subRoot.val:
        #         return root
        #     return dfs(root.left) or dfs(root.right)

