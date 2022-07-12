# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # have a queue of each node and their level
        # have a hashmap of each level
        # while queue isn't empty:
        #   pop from beg,  add to corres hashmap levle arr
        #   then add left/right to queue, level is curr + 1
        # O(n) time:every node O(n) space:hm

        if not root: return

        levels = defaultdict(list)
        queue = deque([(root,0)]) #linkedlist for eff

        while queue:
            curr, lv = queue.popleft()  # Node 3 , 0
            levels[lv].append(curr.val) #levels[0].append(3)

            if curr.left:
                queue.append((curr.left,lv+1))
            if curr.right:
                queue.append((curr.right,lv+1))

        return levels.values()