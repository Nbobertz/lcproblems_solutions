"""
This is for adding two numbers from a linked list
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #3 steps, first read number
        if not l1 or not l2:
            return None

        head1,head2 = l1,l2

        arr1 = []
        arr2 = []

        #o(n)
        while head1:
            arr1.append(head1.val)
            head1 = head1.next

        #o(n)
        while head2:
            arr2.append(head2.val)
            head2 = head2.next

        #add both numbers
        s1,s2 = '',''

        #o(n)
        s1 = ''.join(str(x) for x in reversed(arr1))
        s2 = ''.join(str(x) for x in reversed(arr2))

        s1,s2 = int(s1),int(s2)

        #o(n)
        s3 = s1+s2
        s3 = str(s3)
        s3 = list(s3)
        s3 = s3[::-1]

        head = ListNode()
        cur = head
        #o(n)
        for x in range(len(s3)):
            cur.val = int(s3[x])
            if x != len(s3)-1:
                cur.next = ListNode()
                cur = cur.next

        return head