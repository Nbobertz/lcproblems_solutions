"""
This is leetcode count bowls problem. It is a monotomic stack which means I need to practice this. For some reason my brain can't comprehend this


"""

class Solution:
    def bowlSubarrays(self, nums: List[int]) -> int:
        #edge case
        answer = 0
        if not nums or len(nums)<3:
            return answer

        stack = []

        for num in nums:
            while stack and stack[-1] < num:
                stack.pop()
                if len(stack) >= 1:
                    answer += 1
            stack.append(num)
        return answer
