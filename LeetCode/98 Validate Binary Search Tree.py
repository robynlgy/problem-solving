# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Q: can node values be the same? no
        # simplest tree: left is less than root, right is larger than root
        # recursion : return itself, and max & min at itself,
        #if comparing left, look for max, right look for min

        res = [True]

        def dfs(root,res):
            if not root or res[0]==False:
                return (float('inf'), float('-inf'))

            l_min, l_max = dfs(root.left,res)
            r_min, r_max = dfs(root.right,res)

            if (l_max >= root.val or
                r_min <= root.val):
                res[0] = False
                return (float('inf'), float('-inf'))

            return (min(l_min,r_min,root.val), max(l_max,r_max,root.val))


        dfs(root,res)

        return res[0]

    # dfs = depth first search --> stack --> LIFO [ a, b, c] -> c -> b -> a
    # bfs = breadth first search --> queue --> FIFO [ a, ,b, c] -> a -> b -> c

#     def a():
#         print('hi')
#         b()
#         print('!!')


#     def b():
#         print('world')

#     a()

    # call stack:
    #
    #   b()
    #   a()
    # ---------



    #             3
    #         /      \
    #       1          5
    #     /   \      /   \
    #    0     2    4     6
    #           \
    #            3

    # false
    #
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #passes down condition instead of up
        def dfs(root,left_lim,right_lim):
            if not root:
                return True

            if not (root.val > left_lim and root.val < right_lim):
                return False

            return dfs(root.left,left_lim,root.val) and dfs(root.right,root.val,right_lim)
                # right =
                # if left and right:
                #     return True

            # return False

        return dfs(root,float('-inf'),float('inf'))

