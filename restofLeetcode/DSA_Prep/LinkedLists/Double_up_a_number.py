"""
here we are going to read a linked list and return the integer as a linked list. YOu need to understand how to read a linked list and then return the integer as another linked list


"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def doubleIt(self, head):
        num1 = []

        cur = head
        while cur:
            num1.append(cur.val)
            cur = cur.next

        #turn to int
        num2 = ''
        for x in num1:
            num2 = num2+str(x)
        num2 = int(num2)
        num = num2*2
        num = str(num)

        dummy = ListNode(0)
        cur = dummy
        for ch in num:
            cur.next = ListNode(int(ch))
            cur = cur.next

        return dummy.next