"""
This is just finding what elements exist in either array
"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #step 1, read problem and ask clarrifying questions
        # arr1 = [1,3,4,7,19]
        # arr2 = [0,3,7,20]
        # answer = [3,7]

        #step 2 captuere edge cases
        # what if no input?
        # return empty array

        answer = []
        if not nums1:
            return answer

        ss1 = set(nums1)
        ss2 = set(nums2)

        for n in ss1:
            if n in ss2:
                answer.append(n)
        return answer