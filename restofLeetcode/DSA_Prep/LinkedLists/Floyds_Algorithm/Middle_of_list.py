"""
Here we want to return the middle of a linked list
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #build the linked list first
        prev = ListNode(0,head)
        slow = prev #starting at -1 point
        fast = head #true point

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        return slow.next