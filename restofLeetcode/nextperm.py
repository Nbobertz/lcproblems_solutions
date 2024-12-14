#here we are given an array and we have to find the next possible permutation in the array that is the next largest.

#this one is a very hard one that you need to know the trick for. This is because the intuitive approach that is brute force to generate all permutations would result in a timeout as that is O(!). The trick here is to simply iterate from right to left taking the lowest integer and replacing the largest at the furthest point to the left.

def solution():
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            self.swap(nums, i, j)
        self.reverse(nums, i + 1)

    def reverse(self, nums, start):
        i, j = start, len(nums) - 1
        while i < j:
            self.swap(nums, i, j)
            i += 1
            j -= 1

    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp