"""Classic problem. Recomend that everyone does it at least once."""


class Solution(object):
    def maxArea(self, height):
        # so we can do a two pointer for this and keep track of the distance. Not efficent but easiy demonstrates what we are trying to do
        # water = 0
        # for p1 in range(0,len(height)):
        #     for p2 in range(p1+1,len(height)):
        #         tmp = min(height[p1],height[p2])*(p2-p1)
        #         water = max(water,tmp)

        # o n solution
        # we can do a sliding window soloution, the idea is the keep track of the maximum and miminm. Keep track of maximum line, move l pointer as we hit another max, calculte at each diffrence point
        water = 0
        if len(height) == 1:
            return water
        # we have a container of some kind if we hit this part

        l, r = 0, len(height) - 1

        while l <= r:
            if height[r] < height[l]:
                # move r pointer to the left and calc distance
                tmp = min(height[l], height[r]) * (r - l)
                water = max(tmp, water)
                r -= 1
            elif height[r] >= height[l]:
                tmp = min(height[l], height[r]) * (r - l)
                water = max(tmp, water)
                l += 1

        return water