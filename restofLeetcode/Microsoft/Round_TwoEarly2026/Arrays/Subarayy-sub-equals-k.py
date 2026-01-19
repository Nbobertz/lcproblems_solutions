"""
This is subarray sum ==k whic his prefix sum. YOu need to calculate the sum of the current total minus k
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        curr_sum = 0

        count_map  = {0:1}

        for num in nums:
            curr_sum = num + curr_sum
            target = curr_sum - k
            if target in count_map:
                count +=  count_map[target]
            if curr_sum in count_map:
                count_map[curr_sum] += 1
            else:
                count_map[curr_sum] = 1
        return count