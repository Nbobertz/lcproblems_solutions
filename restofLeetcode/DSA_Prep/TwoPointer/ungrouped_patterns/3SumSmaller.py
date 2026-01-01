#here we are given an input array of integers and asked to find the total number of triplets whose sum is less then the target number

class Solution(object):
    def threeSumSmaller(self, nums, target):
        nums.sort()
        count = 0

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < target:
                    # All elements from left to right-1 with nums[i] and nums[left] are valid
                    count += (right - left)
                    left += 1
                else:
                    right -= 1

        return count