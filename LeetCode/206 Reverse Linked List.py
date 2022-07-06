# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# ============ iterative ver. ============
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

# ========= recursive ver.1 =========
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        newHead = head                                  # 1                 # 2
        if head.next:                                   # if 2              # 2.next = None
            newHead = self.reverseList(head.next)       # newHead = 2
            head.next.next = head                       # 2.next = 1
        head.next = None                                # 1.next = None     # 2.next = None

        return newHead                                  # 2                 # 2

        #[ # -> 1 -> 2 -> # ]

# ========= recursive ver.2 ========= (think this is cleaner)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(cur, prev):
            if cur is None:
                return prev
            else:
                next = cur.next
                cur.next = prev
                return reverse(next, cur)

        return reverse(head, None)