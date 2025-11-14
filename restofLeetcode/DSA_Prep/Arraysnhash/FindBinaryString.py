"""
Convert binary to number and the njust search through range
"""


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:

        ss = set()

        for binary in nums:
            ss.add(int(binary,2))

        #now we have set of tru numbers

        for i in range(len(nums)+1):
            if i not in ss:
                return bin(i)[2:].zfill(len(nums[0]))