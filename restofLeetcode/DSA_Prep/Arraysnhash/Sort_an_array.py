"""
Here we are going to manually sort the array.
Got this first try in under 10 minutes
"""


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        hm = {}  # keep numbers and frequency
        import math
        minn, maxx = min(nums), max(nums)
        for i, n in enumerate(nums):
            if n not in hm:
                hm[n] = 1

            elif n in hm:
                hm[n] += 1

        answer = []
        # now we are going to append to the array in order
        while minn <= maxx:
            # append all inastances of minn if you find it in hm to answer
            if minn in hm:
                for x in range(hm[minn]):
                    answer.append(minn)
            minn += 1
        return answer