"""
Here we want to find the missing integers in the grid. Simply iterate through it and keep a map of what is going on
"""


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        #this is just an extension of hte previous problem. Read to array, then simply do the previous problem
        tmp = []
        ans = []

        if not grid:
            return ans

        for b in range(len(grid)):
            for c in range(len(grid[0])):
                tmp.append(grid[b][c])

        #now build a map and see what number is doubled up
        hm = {}
        for x in tmp:
            if x not in hm:
                hm[x] = 1
            elif x in hm:
                ans.append(x)

        #now go through and see what number is not there
        for x in range(1,len(tmp)+1):
            if x not in hm:
                ans.append(x)
                return ans