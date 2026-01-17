"""
Here is the famous permutations 2 problem
"""


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        answer = []
        if not nums:
            return answer

        # we sort to handle dupclicates
        nums.sort()
        used = [False] * len(nums)

        def dfs(cur):
            if len(cur) == len(nums):
                answer.append(cur[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                # skip duplicates
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                cur.append(nums[i])
                dfs(cur)
                cur.pop()
                used[i] = False

        dfs([])
        return answer