# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val

            cur = cur.right



#         #time with heap -> O(n) + O(n) + k log n -> O(n) + k log n
#         nodes = []

#         def dfs(root,nodes):
#             if not root: return

#             nodes.append(root.val)
#             dfs(root.left,nodes)
#             dfs(root.right,nodes)

#         dfs(root,nodes)
#         heapq.heapify(nodes)
#         for i in range(1,k):
#             heapq.heappop(nodes)

#         return heapq.heappop(nodes)

