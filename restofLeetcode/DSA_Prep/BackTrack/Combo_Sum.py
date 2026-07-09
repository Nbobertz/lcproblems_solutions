"""
Here is combo sum problem
"""

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []

        def dfs(i, sub, total):
            if total == target:
                answer.append(sub[:])
                return

            if total > target or i >= len(nums):
                return

            sub.append(nums[i])
            dfs(i, sub, total + nums[i])
            sub.pop()

            # Skip nums[i]
            dfs(i + 1, sub, total)

        dfs(0, [], 0)
        return answer