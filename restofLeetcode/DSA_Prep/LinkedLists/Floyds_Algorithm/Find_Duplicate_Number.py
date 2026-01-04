"""
This one is more of a check with how numbers are pointing around in an array. The idea is at sometpoint we can point two pointers around and they will hit eachother.
After that simply move the pointers until they converge
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow2 = nums[0]
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow