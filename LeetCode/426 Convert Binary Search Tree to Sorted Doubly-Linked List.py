# Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

# You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

# We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.


"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # time:O(n) bcz we need to traverse through entire tree
        # space: balanced tree = O(log(n)) bcz binary , but worst case is O(n) bcz call-stack for every single node

        if not root: return

        first, last = [None], [None]

        #in-order traversal
        def dfs(head,first,last):
            if not head:
                return

            dfs(head.left,first,last)

            if not first[0] and not last[0]:
                first[0] = last[0] = head
            else:
                head.left = last[0]
                last[0].right = head
                last[0] = head

            dfs(head.right,first,last)

        dfs(root,first,last)

        first[0].left = last[0]
        last[0].right=first[0]

        return first[0]



#         if not root: return
#         # set head and tail to smallest and largest element
#         res, tail = Node(0), Node(0)
#         smallest, largest = self.smallest(root) , self.largest(root)
#         res.right, tail.left = smallest, largest
#         smallest.left, largest.right = largest, smallest
#         if smallest == largest: return smallest

#         # turn tree into 2d list
#         def dfs(head):
#             if not head.left or not head.left.right:
#                 return
#             if head.left.right != head:
#                 next_largest = self.largest(head.left)
#                 # print("next_largest=",next_largest.val)
#                 if not next_largest.left:
#                     next_largest.left = head.left
#                     next_largest.right = head
#                     head.left = next_largest
#             dfs2(head.left)
#         dfs2(root)

#         # complete pointers
#         seen = set()
#         def dfs(head):
#             if not head or head in seen: return
#             if head.right and not head.right.left: head.right.left = head
#             if head.left and not head.left.right: head.left.right = head
#             seen.add(head)
#             left = dfs(head.left)
#             right = dfs(head.right)

#         dfs(root)
#         return res.right


#     def smallest(self,head):      # logn
#         if not head.left:
#             return head
#         return self.smallest(head.left)


#     def largest(self,head):
#         if not head.right:
#             return head
#         return self.largest(head.right)
