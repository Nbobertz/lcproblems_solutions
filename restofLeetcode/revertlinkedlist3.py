#here we are going to be given a linked list and the idea is that we need to invert it. The easiest way to do this is to simply perform encapsulation on the next value in the linked list. We store it and then change the current nodes .next to the previous value. After this we simply go to the next node and establish the previous one as previous

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
#
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         cur = head
#         prev = None
#
#         #loop through each node and set the next to prev
#         while cur:
#             nxt = cur.next
#             cur.next = prev
#             prev = cur
#             cur = nxt
#         return prev