"""
This is the classic 3sum problem
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #we can have a pointer at 0 and then another two at l,r where l = 1, r = len(nums)-1
        #we move them in and capture all possible solutions

        answer = []

        if not nums or len(nums) < 3:
            return answer

        nums = sorted(nums)

        ll = 0
        while ll <= len(nums)-3:
            l,r = ll+1,len(nums)-1

            #handles duplicates
            if ll > 0 and nums[ll] == nums[ll-1]:
                ll+=1
                continue

            while l<r:
                ssum = nums[ll]+nums[l]+nums[r]
                if ssum <0:
                    l+=1
                elif ssum >0:
                    r-=1
                elif ssum == 0:
                    answer.append([nums[ll],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
            ll+=1


        return answer