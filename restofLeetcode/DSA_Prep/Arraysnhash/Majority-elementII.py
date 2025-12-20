"""
Here we want to find the majority element in an array. My solution did not use the o(1) space complexity
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hm = {}
        #freq map
        count = len(nums)//3
        print(count)
        answer = set()
        for n in nums:
            if n not in hm:
                hm[n] = 1
                #just in case it's less then n
                if hm[n] > count:
                    answer.add(n)
            elif n in hm:
                hm[n] += 1
                if hm[n] > count:
                    answer.add(n)
        answer = list(answer)
        return answer