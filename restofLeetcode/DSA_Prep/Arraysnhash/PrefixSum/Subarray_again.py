"""Again"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #ok so this is a prefix sum problem, we are going to move the index and calculate the current sum at each point. If we find the current sum -k in a prefix map we will then add all counts and continue.
        #this works because we can pre calculate everything as we move across the array. Essentially meaning we are going to store the solution before we need it.

        ans = 0
        cursum = 0
        if not nums or k == None:
            return ans

        #pre map
        pre = {0:1} #there is always a 0 array at the front of the array

        for n in nums:
            cursum += n
            res = cursum - k

            #check in map and add to count if you see prefix count
            if res in pre:
                ans += pre[res]

            ##add current sum that we have to map or inc if it exists
            if cursum in pre:
                pre[cursum]+=1
            elif cursum not in pre:
                pre[cursum] = 1

        return ans