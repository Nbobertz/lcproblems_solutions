"""
This problem is literally just return a montomic increasing stack. Pretty simple but I guess you could do it with greedy
"""


class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        # ok so this is a monotomic stack problem since we are going to use a stack and it is goin to be strictly increasing in size as we go across. The question however is will we double up.

        # capture edge case
        if not nums:
            return 0

        stack = []

        for i, n in enumerate(nums):
            if not stack:
                # prime this bad boi
                stack.append(n)
            else:
                # if number is larger go ahead and append
                if n >= stack[-1]:
                    stack.append(n)  # larger goes on top

                # what if the number is less though? We should be able to append the [-1] since it's the largest
                elif n < stack[-1]:
                    # just replace
                    pass  # ? can we just pass

        return len(stack)
