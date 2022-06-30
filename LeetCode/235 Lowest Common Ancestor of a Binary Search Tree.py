# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #time O(log(n)) bcz u either go left/right/return
        #space O(1)
#         if p.val == root.val:
#             return p
#         if q.val == root.val:
#             return q
#         if p.val<root.val and q.val < root.val:
#             return self.lowestCommonAncestor(root.left,p,q)
#         if p.val>root.val and q.val>root.val:
#             return self.lowestCommonAncestor(root.right,p,q)
#         else:
#             return root

        #even cleaner, same approach without recursion:
        cur = root

        while cur:  # will always run
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right
            else:
                return cur


# think this might be O(n) * 3? but doesnt make use of fact that tree is a BST,
# this records the path for p and q nodes and find the latest point that they intersect
#         p_path, q_path = [],[]

#         def dfs(root,seen,target):
#             if not root:
#                 return False
#             if root.val == target:
#                 seen.append(root)
#                 return True
#             left,right = dfs(root.left,seen,target),dfs(root.right,seen,target)
#             if left or right:
#                 seen.append(root)
#                 return True

#             return False

#         dfs(root,p_path,p.val)
#         dfs(root,q_path,q.val)

#         for num in p_path:
#             if num in q_path:
#                 return num