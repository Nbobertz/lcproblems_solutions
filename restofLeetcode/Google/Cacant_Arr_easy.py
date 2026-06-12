"""
This is just to cacatonate an array, the idea here is that we are goign to add onto the end of an array
This is o(n)
"""

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #cant we just add double the array? So, ans = arr1 + arr2? and return?
        nums+=nums
        return nums