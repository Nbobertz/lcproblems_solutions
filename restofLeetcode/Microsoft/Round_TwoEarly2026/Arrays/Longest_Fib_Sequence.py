"""
The trick here is to grab a map of all numbers mapped to their index and then 'count down' from there as you see numbers
o(n2)

"""


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        if len(arr) <= 2:
            return 0

        index_map = {}

        for i, n in enumerate(arr):
            index_map[n] = i

        maxi = 0

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                prev, prevv = arr[j], arr[i]
                length = 2
                while prev + prevv in index_map:
                    length += 1
                    maxi = max(maxi, length)
                    prev, prevv = prev + prevv, prev

        return maxi if maxi > 2 else 0