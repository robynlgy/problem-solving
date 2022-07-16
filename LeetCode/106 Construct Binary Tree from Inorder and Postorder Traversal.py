# Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # inorder = [9,3,15,20,7]
        # postorder = [9,15,7,20,3]

        inorder_map = {}

        for i,val in enumerate(inorder):
            inorder_map[val] = i

        def helper(left,right):
            while postorder:
                curr = postorder.pop()
                root = TreeNode(curr)
                curr_idx = inorder_map[curr]

                if curr_idx != right:
                    root.right = helper(curr_idx+1,right)
                if curr_idx != left:
                    root.left = helper(left,curr_idx-1)

                return root

        return helper(0,len(postorder)-1)