#This is a very brute force approach to the problem of next greater number

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        #brute force

        answer = []

        for n1 in range(0,len(nums1)):
            for n2 in range(0,len(nums2)):
                if nums1[n1] == nums2[n2]:
                    tmp = -1
                    r = n2 + 1
                    while r <= len(nums2):
                        if r == len(nums2):
                            answer.append(tmp)
                            break
                        if nums2[n2]<nums2[r]:
                            tmp = nums2[r]
                            answer.append(tmp)
                            break
                        r+=1
        return answer

#This is the efficent o(n) way
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        hm = {n:i for i,n in enumerate(nums1)}
        res = [-1] * len(nums1)

        stack = []
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                idx = hm[val]
                res[idx] = cur
            if cur in hm:
                stack.append(cur)
        return res