"""
Here it's two sum but the input array is sorted. We just do a two pointer
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ## because of the o(1) additional space this makes it intresting.
        # I think what we can do is a two pointer solution and move pointers based off sum

        ans = []

        # edge case of no input
        if not numbers:
            return ans

        # establish pointers
        l, r = 0, len(numbers) - 1

        while l <= r:
            ssum = numbers[l] + numbers[r]

            # if sum is larger then target
            if ssum > target:
                r -= 1

            # if sum is smaller
            elif ssum < target:
                l += 1

            # what if we found it?
            elif ssum == target:
                ans = [l + 1, r + 1]
                return ans