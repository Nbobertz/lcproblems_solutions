"""
Got stuck on this problem for some reason, whatever

"""

class Solution(object):
    def checkIfExist(self, arr):
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i != j:
                    if arr[i] == 2*arr[j]:
                        return True
        return False