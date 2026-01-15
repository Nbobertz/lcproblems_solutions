"""
This is teh kth largest stone problem
"""


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # two inputs, one is array of nums, the other is a integer k.
        # k we will come back to
        self.k = k
        import heapq
        self.nums = nums[:]
        heapq.heapify(self.nums)

        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)

        if len(self.nums) > self.k:
            heapq.heappop(self.nums)

        return self.nums[0]


