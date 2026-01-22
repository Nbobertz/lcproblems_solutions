"""
This is combination sum problme
"""


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []
        if not nums:
            return answer

        def dfs(i, arr, total):
            if total == target:
                answer.append(arr[:])
                return

            elif i >= len(nums) or total > target:
                # i is out of bounds and we are above target
                return

            arr.append(nums[i])
            dfs(i, arr, total + nums[i])
            arr.pop()
            dfs(i + 1, arr, total)
            return

        dfs(0, [], 0)
        return answer