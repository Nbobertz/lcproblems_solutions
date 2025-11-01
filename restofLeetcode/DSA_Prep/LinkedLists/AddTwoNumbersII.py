"""
Not sure how this problem and the first one are simliar but all we have to do is read from two linked lists and add up the numbers. After that cast it to a new linked list.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):

        s1 = ''
        s2 = ''

        while l1:
            s1 += str(l1.val)
            l1 = l1.next
        while l2:
            s2 += str(l2.val)
            l2 = l2.next

        # convert to integers
        n1, n2 = int(s1), int(s2)

        n3 = n1 + n2
        n3s = str(n3)

        # now we cast to new linked list
        head = ListNode(int(n3s[0]))
        cur = head

        # idea here is to then go through and put each integer where it is supposed to go
        for x in range(1, len(n3s)):
            cur.next = ListNode(int(n3s[x]))
            cur = cur.next
        return head