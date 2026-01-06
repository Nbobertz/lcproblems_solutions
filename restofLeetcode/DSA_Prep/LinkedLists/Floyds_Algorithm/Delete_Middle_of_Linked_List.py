"""
Here we are deleting hte middle part of a linked list. I am sure my method is not the most efficent but it works
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head2 = head
        prev = ListNode(0, head)
        slow = prev
        fast = head

        # the idea is that we are going to use a fast and slow pointer to hit the end of the list
        if fast.next == None:
            # we only have one pointer
            head = None
            return head

        prev2 = None
        while fast != None and fast.next != None:
            prev2 = slow
            slow = slow.next
            fast = fast.next.next

        # step one over
        prev2 = slow
        slow = slow.next

        # now delete middle point and return head
        tmp = slow.next
        slow = prev2
        prev2.next = tmp

        return head2

