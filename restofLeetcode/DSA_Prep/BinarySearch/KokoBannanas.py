"""
I don't really get this logic but here is Koko Eating Bannaans
"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        #ok so we have to take the min which is 1 bannaa per hour and the max which is the max(piles)
        #we then go downwards until we eat all the bannanas
        l,r = 1, max(piles)
        res = r

        while l<=r:
            k = (l+r)//2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p)/k)
            if totalTime <= h:
                res = k
                r = k-1
            else:
                l = k + 1
        return res