# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:
# Input: head = [1], n = 1
# Output: []

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next: return None
        dummy = ListNode(next=head)
        # starting the pointer at one before so that we dont have to save temp variables when updating the .next arrows
        slow, fast = dummy, head

        #whenever you're setting a dummy = slow, then updating slow:
        # when you first update slow.next, ure updating what dummy is pointing to next as well bcz at this point slow == dummy
        # however whne you're updating what slow is, thats when the link between the two breaks
        for i in range(n):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next




