#got this one after about 15 minutes. Just sum the index points to binary and count the 1's in teh resulting string

class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        answer = 0
        for i,n in enumerate(nums):
            count = 0
            binary = bin(i)
            for x in binary:
                if x == '1':
                    count+=1
            if count == k:
                answer+=int(n)

        return answer