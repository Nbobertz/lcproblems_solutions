"""
Easy LC done at mindight. Just find the intersection of two arrays
"""


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hm = {}
        answer = []

        ns1 = set(nums1)
        ns2 = set(nums2)

        for n in ns1:
            hm[n] = 1

        for n in ns2:
            if n in hm:
                answer.append(n)

        return answer