"""
Here we just want to find the index points of stable mountains based off logic
"""


class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        answer = []

        # capture edge case
        if len(height) == 0 or threshold == None:
            return answer

        # if len 1
        if len(height) == 0:
            return answer

        # just do one o(n) pass
        for i in range(1, len(height)):
            prev = height[i - 1]
            if prev > threshold:
                answer.append(i)

        return answer