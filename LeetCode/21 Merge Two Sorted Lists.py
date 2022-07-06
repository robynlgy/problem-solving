# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Example 1 :
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        curr = head = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                curr, list1 = list1, list1.next

            else:
                curr.next = list2
                curr, list2 = list2, list2.next

        if list1 or list2:
            curr.next = list2 if list2 else list1

        return head.next




# prev tries

#         cur = dummy = ListNode()
#         while list1 and list2:
#             if list1.val < list2.val:
#                 # print("first",list1.val,"==",cur.next.val, cur.val)
#                 cur.next = list1
#                 list1, cur = list1.next, list1 #for cur = list1 here, list1 is still before it became list1.next
#                 # print("second",list1.val,"==",cur.next.val, cur.val)
#             else:
#                 cur.next = list2
#                 list2, cur = list2.next, list2

#         if list1 or list2:
#             cur.next = list1 if list1 else list2

#         return dummy.next



#         if not list1 and not list2:
#             return None
#         if not list1 and list2:
#             return list2
#         if not list2 and list1:
#             return list1
#         #if both empty, return null?
#         # if one empty, return head of one

#         # two pointer, one on each list, whichever is smaller goes to new list

#         head = None
#         curr = None;

#         while list1 and list2:
#             # start w head
#             if not head:
#                 if list1.val <= list2.val:
#                     head = list1;
#                     list1 = list1.next;
#                     curr = head
#                 else:
#                     head = list2;
#                     list2=list2.next;
#                     curr = head;
#             else:
#                 if list1.val<= list2.val:
#                     temp = list1.next
#                     curr.next = list1;
#                     curr = list1
#                     list1 = temp;
#                 else:
#                     temp = list2.next;
#                     curr.next = list2;
#                     curr = list2;
#                     list2 = temp


#         if list1:
#             curr.next = list1
#         elif list2:
#             curr.next = list2

#         return head
