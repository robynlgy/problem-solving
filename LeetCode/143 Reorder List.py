# You are given the head of a singly linked-list. The list can be represented as
# L0 → L1 → … → Ln - 1 → Ln

# Reorder the list to be on the following form:
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# Example 1 :
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]

# Example 2 :
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
# ================ O(n) time O(1) space ================

## 1) find middle point of list
        slow, fast = head, head.next
    # doing head.next for fast instead of head bcz we want to be able to set slow.next to be None to signify that the first half is ended
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None

## 2) reverse second half of list
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        # prev is the head of the second list and the last node of orig list

## 3) merge the two lists, taking one from each

        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2


# ================ O(n) time O(n) space ================
#         curr = head
#         nodes_list = []

#         while curr:
#             nodes_list.append(curr)
#             curr = curr.next

#         l,r = 0 , len(nodes_list)-1
#         last = head

#         while l<r:
#             nodes_list[l].next = nodes_list[r]
#             l += 1

#             if l == r:
#                 last = nodes_list[r]
#                 break

#             nodes_list[r].next = nodes_list[l]
#             r -= 1

#             last = nodes_list[l]
#         if last:
#             last.next = None

   #        ========
        # alt second part after list is setup
        # curr = head
        # while curr:
        #     last = nodes_list.pop()
        #     if curr == last:
        #         curr.next = None
        #         break
        #     if curr.next == last:
        #         curr.next.next = None
        #         break
        #     last.next = curr.next
        #     curr.next = last
        #     curr = last.next


# ======== O(n^2) ================================================================

        # works but too slow - finding the last node is n so n^2?
        # curr = head

#         def findLast(head) -> ListNode:
#             curr = head
#             if not curr.next: return curr

#             while curr.next:
#                 prev = curr
#                 curr = curr.next
#             prev.next = None
#             return curr

#         while curr and curr.next:
#             last = findLast(curr)
#             last.next = curr.next
#             curr.next = last
#             curr = last.next

#         return head




