# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # time: def O(n) this time
        # space: hm O(n)
        if not node: return

        origMap = defaultdict()

        def dfs(node):
            copy = Node(node.val)
            origMap[node] = copy

            for neighbor in node.neighbors:
                if neighbor in origMap:
                    copy.neighbors.append(origMap[neighbor])
                else:
                    copy.neighbors.append(dfs(neighbor))

            return copy


        return dfs(node)







#         #create a orig to clone hm
#         #then for each node, append the corresponding clone node to neighbors list
#         # space => hm => O(n) --> is there a way to do this using constant space
#         # time => O(2n) to make hm and append neighbors maybe O(n*m) where m is the num of neighbors for second nested loop
#         if not node: return

#         origMap = defaultdict()
#         stack = [node]

#         while stack:
#             curr = stack.pop()
#             copy = Node(curr.val)
#             origMap[curr] = copy

#             for neighbor in curr.neighbors:
#                 if neighbor not in origMap:
#                     stack.append(neighbor)


#         for orig in origMap:
#             for neighbor in orig.neighbors:
#                 origMap[orig].neighbors.append(origMap[neighbor])

#         return origMap[node]