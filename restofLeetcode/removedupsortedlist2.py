#here we are going to be given a sorted list and we have to remove all duplicates from it and return unique integers only.

#run in lc as they have test cases. LC 82
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         ss = set()
#
#         cur = head
#         prv = None
#
#         while cur:
#             #catch if number is/is not in hm
#             if cur.val not in ss:
#                 ss.add(cur.val)
#                 prev = cur
#                 cur = cur.next
#             elif cur.val in ss:
#                 tmp = cur
#                 prev.next = cur.next
#                 prev = cur.next
#                 cur = cur.next
#         return head