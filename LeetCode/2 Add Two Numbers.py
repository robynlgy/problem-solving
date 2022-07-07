# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
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

        return dummy.next if dummy.next else dummy