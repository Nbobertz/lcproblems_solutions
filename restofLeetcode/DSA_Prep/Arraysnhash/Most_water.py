"""
This is literally one of the classic two pointer problems. Container with most water.
Just move the smaller pointer and calc. You don't have to worry about if both are the same.
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        #ok, so this is a classic. What you do is move the smaller integer pointer and continue to capture the most water
        ans = 0
        if not height:
            return 0 #cant hold water

        l,r = 0,len(height)-1

        while l<=r:
            ssum = min(height[l],height[r])*(r-l)
            ans = max(ssum,ans)

            #move pointers
            if height[l]<height[r]:
                l+=1
            else:
                r-=1

        return ans