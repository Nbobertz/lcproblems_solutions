"""
This is for a rotated sorted array
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        n = len(nums)
        l, r = 0, n - 1

        # Step 1: find pivot (index of smallest element)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        pivot = l

        # Step 2: binary search with index mapping
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            real_mid = (mid + pivot) % n

            if nums[real_mid] == target:
                return real_mid
            elif nums[real_mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1
