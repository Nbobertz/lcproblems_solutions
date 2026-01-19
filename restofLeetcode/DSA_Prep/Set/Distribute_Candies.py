"""
Here we have to distirbute candies to overweight alice. The idea is that alice can only eat a set portion of candies
"""


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        ss = set(candyType)

        n = len(candyType)
        sn = len(ss)

        if (n // 2) <= sn:
            return (n // 2)

        elif (n // 2) > sn:
            return sn