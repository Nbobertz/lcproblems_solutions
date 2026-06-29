"""
3Sum but the trick here is to skip duplicates and it's two sum inside of a loop
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []

        if len(nums) < 3:
            return ans

        nums.sort()

        for i1 in range(len(nums) - 2):

            if i1 > 0 and nums[i1] == nums[i1 - 1]:
                continue

            l, r = i1 + 1, len(nums) - 1

            while l < r:
                ssum = nums[i1] + nums[l] + nums[r]

                if ssum < 0:
                    l += 1

                elif ssum > 0:
                    r -= 1

                else:
                    ans.append([nums[i1], nums[l], nums[r]])

                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return ans