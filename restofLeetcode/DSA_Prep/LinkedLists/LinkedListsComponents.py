"""
The logic for this problem is weird. Just scan for linked list components
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        answer = 0

        if not head or not nums:
            return answer

        nums = set(nums)

        while head:
            if head.val in nums and (head.next == None or head.next.val not in nums):
                answer += 1
            head = head.next

        return answer