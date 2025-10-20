"""
The idea here is to return the middle of the linked list


"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        #First pass is to capture len, then we count on the second pass

        n = 0

        curr = head
        while curr:
            n+=1
            curr = curr.next

        n = n/2

        print(n)

        #now go through list and return the node
        cur2 = head
        while cur2:
            if n == 0:
                print('here')
                return cur2
            n-=1
            cur2 = cur2.next