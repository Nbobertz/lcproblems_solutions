"""
just add all arrays together with extend and then do binary search
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        marr = []

        #o(n) pass to combine into master array
        for m in matrix:
            marr.extend(m)

        #do binary
        l,r = 0,len(marr)-1

        while l<=r:
            half = int((l+r)/2)

            #logic
            if marr[half] < target:
                l = half+1
            elif marr[half] > target:
                r = half-1
            elif marr[half] == target:
                return True

        return False
