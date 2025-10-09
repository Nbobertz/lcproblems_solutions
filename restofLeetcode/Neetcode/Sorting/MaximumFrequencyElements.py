"""
Did this one bymyself in under 10 minutes. Simple bucket sort on stuff and then see what we have as the maximum frequency

"""


class Solution(object):
    def maxFrequencyElements(self, nums):
        # we can do this with bucket sort in o(n) assuming what we are doing is simply taking the maximum bucket and adding up the frequencies
        answer = 0
        if not nums:
            return answer

        # so now we have nums
        hm = {}  # number, frequency
        for n in nums:
            if n not in hm:
                hm[n] = 1
            elif n in hm:
                hm[n] += 1

        # now we have frequency map; 1 occurs 3 times for example
        # now we simply create our bucket array
        buckets = []
        for _ in range(0, len(nums) + 1):
            # we do +1 to capture maximum possible buckets
            buckets.append([])

        # now we simply pull from the hashmap and assign to each frequency the bucket
        for num, freq in hm.items():
            buckets[freq].append(num)

        # now we simply need to pull from the last bucket and add up all the frequencies
        counter = 0
        for buc in buckets[::-1]:
            counter += 1
            if len(buc) != 0:
                spot = len(buckets) - counter
                for num in buc:
                    answer += spot
                break
        return answer
