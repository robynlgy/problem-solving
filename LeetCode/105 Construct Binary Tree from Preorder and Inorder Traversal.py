# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder = [ 3, 9, 20, 15, 7 ]
        # inorder = [ 9, 3, 15, 20, 7]
        inorder_map = {}
        # {9: 0, 3: 1, 15: 2, 20: 3, 7: 4}
        preorder = deque(preorder)

        for i,val in enumerate(inorder):
            inorder_map[val] = i

        def helper(left,right):
            while preorder:
                node_val = preorder.popleft()
                root = TreeNode(node_val)
                root_idx = inorder_map[node_val]
                if root_idx != left:
                    root.left = helper(left,root_idx-1)
                if root_idx != right:
                    root.right = helper(root_idx+1,right)

                return root

        return helper(0,len(preorder)-1)





        # slicing O(n^2) time n space
#         while inorder:
#             root = TreeNode(preorder.pop(0))
#             curr_index = inorder.index(root.val)
#             root.left = self.buildTree(preorder,inorder[:curr_index])
#             root.right = self.buildTree(preorder,inorder[curr_index+1:])

#             return root






#         # preorder = [3,9,90,91,20,15,7]
#         # inorder  = [90,9,91,3,15,20,7]

#         if inorder:
#             currIdx = inorder.index(preorder.pop(0))
#             root = TreeNode(inorder[currIdx])
#             root.left = self.buildTree(preorder,inorder[:currIdx])
#             root.right = self.buildTree(preorder,inorder[currIdx+1:])

#             return root

