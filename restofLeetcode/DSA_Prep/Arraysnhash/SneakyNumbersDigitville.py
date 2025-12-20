"""
Here we simply are going to see if two numbers made a doulble apperance in an array
"""

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        answer = []

        if not nums:
            return answer

        #o(n) pass add to hashmap
        hm = {}

        for n in nums:
            if n not in hm:
                hm[n] = 1
            elif n in hm:
                answer.append(n)

        return answer


