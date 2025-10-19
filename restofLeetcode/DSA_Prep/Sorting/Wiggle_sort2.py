class Solution(object):
    def wiggleSort(self, nums):

        #sort nums
        nums.sort()

        mid = (len(nums)+1) // 2 #int division
        l,r = nums[:mid][::-1],nums[mid:][::-1]
        nums[::2], nums[1::2] = l,r

