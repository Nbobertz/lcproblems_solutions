#did bucket sort top k frequent elements again

class Solution(object):
    def topKFrequent(self, nums, k):
        # do bucket sort
        # the idea here is that we will iterate through the array and then store the number and frequency. The idea is that we then const an array of bucketts [[]] where each [] corespondes to the maximumum len of nums. We then count off from the backend of k to get the correct answer

        hm = {}

        # first pass to capture all numbers and their frequencies
        for n in nums:
            if n not in hm:
                hm[n] = 1
            elif n in hm:
                hm[n] += 1

        # now we build a subarray of buckets
        buckets = []
        for _ in range(0, len(nums) + 1):
            buckets.append([])

        # now we have a bucket array where we can drop in the frequency of integers into each bucket
        for freq, number in hm.items():
            buckets[number].append(freq)

        # now we iterate backwards over array until the len of answer array is == k. The idea here is we are capturing all the elements at sub-bucket frequency.
        answer = []
        for buc in buckets[::-1]:
            if len(buc) != 0:
                # we have a number in the bucket
                for x in buc:
                    answer.append(x)

            if len(answer) >= k:
                return answer