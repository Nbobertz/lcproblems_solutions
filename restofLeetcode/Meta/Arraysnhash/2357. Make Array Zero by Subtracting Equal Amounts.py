class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = set()

        for num in nums:
            if num not in count and num != 0 :
                count.add(num)
        return len(count)