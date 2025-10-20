"""
Here we are just searching a 2d array to see if we can find a number. Just add it all together and see

"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        arr = []

        n = len(matrix)
        for x in range(0,n):
            arr.extend(matrix[x])

        #now just binary search
        l,r = 0,len(arr)-1

        while l <= r:
            half = (l+r)//2
            #if we are higher
            if arr[half]>target:
                r = half -1
            elif arr[half]<target:
                l = half + 1
            elif arr[half]==target:
                return True
        return False
