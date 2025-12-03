"""
return the middle of a linked list
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #we can do this with fast and slow pointer

        prev = ListNode(0,head)
        slow = prev
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        #now we are at middle, grab the next one over
        return slow.next