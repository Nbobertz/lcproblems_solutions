"""
Here we are going to count partitions in an array
"""

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        answer = 0

        if not nums:
            return answer

        for i in range(0,len(nums)-1):
            ss = sum(nums[:i])+sum(nums[i:])
            if ss % 2 == 0:
                #is even
                answer+=1

        return answer