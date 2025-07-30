#Here we are given an array of integers. We need to return true if there is at least two sets of the same integer
#return False if the entire array is unique

class Solution(object):
    def containsDuplicate(self, nums):
        #we can use a hashset for this. Iterate through once and see if it exists in the set
        hs = set()

        for num in nums:
            if num not in hs:
                hs.add(num)
            elif num in hs:
                return True
        return False