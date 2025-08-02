#return the top k most frequent elements in an array




class Solution(object):
    def topKFrequent(self, nums, k):

        # so iterate throug the array, store to hashmap, then see if it hits k

        hm = {}
        answer = []

        if len(nums) <= k:
            return nums
        for num in nums:
            if num not in hm:
                hm[num] = 1
            elif num in hm:
                hm[num] += 1

        # look for k most frequent elements
        hm2 = {}
        arr = []

        for key, value in hm.items():
            if value not in arr:
                arr.append(value)
            if value not in hm2:
                hm2[value] = [key]
            elif value in hm2:
                tmp = hm2[value]
                tmp.append(key)
                hm2[value] = tmp

        arr.sort()
        for i in range(0, k):
            check = arr.pop()
            num = hm2[check]
            for n in num:
                answer.append(n)
                if len(answer) >= k:
                    return answer

        return answer