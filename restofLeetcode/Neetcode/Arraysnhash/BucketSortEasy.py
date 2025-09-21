#This is just to iterate through an array and return the most common smallest even number there is

class Solution(object):
    def mostFrequentEven(self, nums):

        # init answer
        answer = -1

        hm = {}
        for n in nums:
            if n % 2 == 0:
                # even
                if n not in hm:
                    hm[n] = 1
                elif n in hm:
                    hm[n] += 1

        # now buckets
        bucket = []
        for buc in range(len(nums) + 1):
            # plus one to capture all evens
            bucket.append([])

        for num, freq in hm.items():
            bucket[freq].append(num)

        for potential in bucket[::-1]:
            if len(potential) == 1:
                return potential[0]
            # two or more
            elif len(potential) > 1:
                potential.sort()
                return potential[0]

        return answer