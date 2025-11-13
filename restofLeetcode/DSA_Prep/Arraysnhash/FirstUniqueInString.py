"""
Just find the first unique letter in a string and return it's index
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hm = {}

        for i,char in enumerate(s):
            if char not in hm:
                hm[char] = [i,1]
            elif char in hm:
                hm[char][1]+=1

        #now call the map and return all 1's

        lowest = None #init to len s to capture the max letter
        for i,arr in hm.items():
            if arr[1] == 1:
                if lowest == None:
                    lowest = arr[0]
                else:
                    lowest = min(arr[0],lowest)
        if lowest == None:
            return -1
        else:
            return lowest
