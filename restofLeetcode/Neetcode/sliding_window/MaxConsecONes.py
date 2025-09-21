#The idea here is that you have an array of 1's and 0's and the idea is that you need ot return the max len within the array of 1's where you can only change one 0 to a 1

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        l = 0
        max_len = 0
        zero_count = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[l] == 0:
                    zero_count -= 1
                l += 1  # shrink window from left

            max_len = max(max_len, r - l + 1)

        return max_len