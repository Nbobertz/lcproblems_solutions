"""
This is for an intersection of two arrays

"""


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # create a frequency map

        hm = {}
        answer = []

        if len(nums1) >= len(nums2):

            # build map
            for n in nums1:
                if n not in hm:
                    hm[n] = 1
                elif n in hm:
                    hm[n] += 1

            # now go through and see if nums2 n is in hm
            for x in nums2:
                if x in hm:
                    answer.append(x)
                    hm[x] -= 1
                    if hm[x] == 0:
                        del hm[x]

        elif len(nums1) < len(nums2):
            for n in nums2:
                if n not in hm:
                    hm[n] = 1
                elif n in hm:
                    hm[n] += 1

            for x in nums1:
                if x in hm:
                    answer.append(x)
                    hm[x] -= 1
                    if hm[x] == 0:
                        del hm[x]

        return answer