"""
Did the subsets problme
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        if not nums:
            return answer #returns empty array

        def dfs(i,arr):
            if i>= len(nums):
                answer.append(arr[:]) #o(n) copy
                return

            arr.append(nums[i])
            dfs(i+1,arr)
            arr.pop()
            dfs(i+1,arr)
            return

        dfs(0,[])
        return answer