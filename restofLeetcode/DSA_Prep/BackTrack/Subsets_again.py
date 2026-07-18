"""
Here we are going to add all subsets of integers to an answer array
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #this is a backtracking algorithm because it needs to return all possible subsets

        answer = []
        if not nums:
            return answer

        def dfs(i,sub):
            nonlocal answer

            if i >= len(nums):
                answer.append(sub[::])
                return

            #now we increase
            sub.append(nums[i])

            dfs(i+1,sub)
            sub.pop()
            dfs(i+1,sub)
            return

        dfs(0,[])
        return answer