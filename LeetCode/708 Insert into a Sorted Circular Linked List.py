# Given a Circular Linked List node, which is sorted in ascending order, write a function to insert a value insertVal into the list such that it remains a sorted circular list. The given node can be a reference to any single node in the list and may not necessarily be the smallest value in the circular list.

# If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the circular list should remain sorted.

# If the list is empty (i.e., the given node is null), you should create a new single circular list and return the reference to that single node. Otherwise, you should return the originally given node.

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        ## Alt: instead of tracking a largest node, we know that it is the largest node when prev > curr as you're going through a loop. alternative solution is to loop until one of the base cases it met, return the prev and curr pointers and update the link outside of the loop to minimize code within the loop :( see code at bottom

        new_node = Node(insertVal)
        if not head:
        #edge: null node
            new_node.next = new_node
            return new_node

        seen = set()
        def search(head,last = None, largest = None):
            if head.next == head:
            #edge: 1 node
                head.next, new_node.next = new_node, head
                return
            if last and head.val >= insertVal and last.val <= insertVal:
            # this should be before the next if stmt because some insertVals arent' larger/smaller than all but needs to be inserted right before head
                last.next = new_node
                new_node.next = head
                return
            if head in seen:
            #edge: insertVal is larger/smaller than all nodes, stop infinite loop and insert after the largest node
                largest.next, new_node.next = new_node, largest.next
                return

            seen.add(head)
            if not largest or head.val >= largest.val:
                largest = head

            search(head.next, head,largest)

        search(head)

        return head


    # from discussions:
# class Solution:
#     def insert(self, head, val):
#         node = Node(val, head)
#         if not head:
#             node.next = node
#             return node
#         prev, cur = head, head.next
#         while 1:
#             if prev.val <= val <= cur.val:
#                 break
#             elif prev.val > cur.val and (val<cur.val or val>prev.val):
#                 break
#             prev, cur = prev.next, cur.next
#             if prev == head:
#             #RL: this takes care of the [3,3,3], 0 case -> we know that it went over a loop, and since they're all the same numbers, 0 can be inserted wherever the pointers are (which also is where we started). This also takes care of when there's only one element in the cycle
#                 break
#         prev.next = node
#         node.next = cur
#         return head