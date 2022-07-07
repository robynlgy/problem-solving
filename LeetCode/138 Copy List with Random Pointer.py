# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

# Return the head of the copied linked list.

# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
# Your code will only be given the head of the original linked list.


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = { None : None }      # O(n) space

        curr = head
        while curr:                     #O(n)
            copy = Node(curr.val)
            oldToNew[curr] = copy
            curr = curr.next

        curr = head
        while curr:                     #O(n)
            copy = oldToNew[curr]
            copy.next = oldToNew[curr.next]
            copy.random = oldToNew[curr.random]
            curr = curr.next

        return oldToNew[head]



#         #O(n^2) sol bcz finding index
#         if not head: return None
#         # initialize list1 with each node of orig list
#         # initialize list2 with each node with just the value
#         list1, list2 = [], []
#         curr = head
#         while curr:                                 #O(n)
#             list1.append(curr)
#             list2.append(Node(curr.val))
#             curr = curr.next

#         # get index of where random node is stored in orig list
#         rand_idx = []
#         for i in range(len(list1)):                 #O(n^2)
#             rand_node = list1[i].random
#             rand_idx.append(list1.index(rand_node) if rand_node else None)

#         # populate .next to point to next node in list and .rand to point to the right index
#         for i in range(len(list2)):                     #O(n)
#             # update .next for all except last node
#             if i < len(list2)-1:
#                 list2[i].next = list2[i+1]
#             list2[i].random = list2[rand_idx[i]] if (rand_idx[i]!=None) else None

#         return list2[0]
