#standard two sum. Here is the answer using a hashmap to keep track of where we have been.
class Solution:
    def twoSum(nums: list[int], target: int) -> list[int]:
        hashm = {}

        for x in range(0,len(nums)):
            tt = target - nums[x]
            if tt in hashm:
                return [hashm[tt],x]

            #put in hashm
            if nums[x] not in hashm:
                hashm[nums[x]] = x

nums = [2,7,11,15]
target = 9

print(Solution.twoSum(nums=nums,target=target))