"""
Get all possible subsets for an array
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        if not nums:
            return answer

        sub = []

        def dfs(i):
            """
            recursion algorithm that will move through the array from left to right appending unique subarrays
            """

            # handle base case
            # i = index
            if i >= len(nums):
                # return
                answer.append(sub.copy())
                return

            # append to sub, builds the array
            sub.append(nums[i])

            # now we recursion for all of i
            dfs(i + 1)
            sub.pop()
            dfs(i + 1)

        dfs(0)
        return answer