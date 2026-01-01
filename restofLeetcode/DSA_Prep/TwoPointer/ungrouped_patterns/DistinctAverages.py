"""
Here we need to return teh number of distinct averages we see in the input array. This is an easy problem


"""


class Solution(object):
    def distinctAverages(self, nums):
        #ok we use a set, calculate numbers and then return the number of distinct

        ss = set()

        nums = sorted(nums)
        #o(logn)

        while len(nums) != 0:
            n1 = float(nums[0])
            n2 = float(nums[-1])

            #remove numbers
            nums.pop(0)
            nums.pop()

            #calc average
            ave = float((n1+n2)/2)
            ss.add(ave)

        return len(ss)