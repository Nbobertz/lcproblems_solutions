"""
Here we simply just removed nodes from a linked list using a montomic stack
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #use a monotomic stack to append and then pop to increasing
        stack = [] #strictly increasing

        cur = head
        while cur:
            if len(stack) == 0:
                stack.append(cur.val)
            elif stack and cur.val > stack[-1]:
                while stack and cur.val > stack[-1]:
                    stack.pop()
                stack.append(cur.val)
            elif stack and cur.val <= stack[-1]:
                stack.append(cur.val)
            cur = cur.next


        answer = ListNode()
        dummy = answer
        for n in range(len(stack)-1):
            answer.val = stack[n]
            answer.next = ListNode()
            answer = answer.next
        answer.val = stack[-1]
        return dummy