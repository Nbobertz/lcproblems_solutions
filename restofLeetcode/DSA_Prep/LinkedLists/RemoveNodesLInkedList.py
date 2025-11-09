"""
Here we had to remove nodes from a linked list. This problem is a great one to determine how to build a linked list
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        #so this a stack problem
        cur = head
        tmp = []

        if not head:
            return stack

        while cur:
            tmp.append(cur.val)
            cur = cur.next

        answer = []
        #loop backwards
        largest = None
        for n in tmp[::-1]:
            if largest == None:
                largest = n
                answer.append(n)
            else:
                if n < largest:
                    continue
                elif n >= largest:
                    largest = n
                    answer.insert(0,n)


        #creat linked list
        head2 = ListNode()
        cur = head2

        for x in range(0,len(answer)):
            cur.val = answer[x]
            if x == len(answer)-1:
                return head2
            cur.next = ListNode()
            cur = cur.next