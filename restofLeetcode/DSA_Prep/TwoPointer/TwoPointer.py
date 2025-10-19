"""
The idea here is that we need to find an a target in an array in o(1) space complexity.
This can be done with a two pointer approach


"""

class Solution(object):
    def twoSum(self, numbers, target):
        l,r = 0,len(numbers) -1

        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1,r+1]
            elif s < target:
                l += 1
            else:
                r -= 1