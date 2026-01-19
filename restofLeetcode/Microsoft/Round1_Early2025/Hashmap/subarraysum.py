#here we are given an integer array and asked if we can find all continous subarray's that add up to the k target.


nums = [1,2,3,4,5]

k = 6

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sub_num = {0: 1}
        total = count = 0

        for n in nums:
            total += n

            if total - k in sub_num:
                count += sub_num[total - k]

            sub_num[total] = 1 + sub_num.get(total, 0)

        return count

print(Solution.subarraySum())