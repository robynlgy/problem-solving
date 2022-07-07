# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # O(n) * 3 => O(n) where n is the longer of two lists/result
        sum = 0
        dig1, dig2 = 0, 0
        curr, curr2 = l1, l2

        while curr:
            sum += curr.val * 10 ** dig1
            dig1 += 1
            curr = curr.next
        while curr2:
            sum += curr2.val * 10 ** dig2
            dig2 += 1
            curr2 = curr2.next

        dummy = curr = ListNode()

        while sum:
            value = sum % 10
            sum = sum // 10
            curr.next = ListNode(value)
            curr = curr.next

        return dummy.next if dummy.next else dummy #edge case where l1 and l2 is [0]

        ## alternative - add two nodes from both lists together and maintain a carry
        # O(n) where n is the longer of two lists, +1 if carry

#         dummy = curr = ListNode()

#         carry = 0
#         while l1 or l2 or carry:
#             v1 = l1.val if l1 else 0
#             v2 = l2.val if l2 else 0

#             val = v1 + v2 + carry
#             carry = val // 10
#             val = val % 10
#             curr.next = ListNode(val)

#             curr = curr.next
#             l1 = l1.next if l1 else None
#             l2 = l2.next if l2 else None

#         return dummy.next







