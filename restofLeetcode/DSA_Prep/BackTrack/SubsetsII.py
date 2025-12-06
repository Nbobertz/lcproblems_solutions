"""
Not really sure what this problem wanted exactly but it was just subsets with more steps
"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        answer = []

        sub = []

        nums = sorted(nums)

        seen = set()

        def dfs(i):
            #handle base case
            if i >= len(nums):
                #found full subarray
                tmp = tuple(sub)
                if tmp not in seen:
                    answer.append(sub.copy())
                    seen.add(tmp)
                return

            #handle logic of adding to working sub
            sub.append(nums[i])

            dfs(i+1) #do all the first index
            sub.pop() #moves to next index point
            dfs(i+1) #does next index point

        dfs(0)
        return answer[::-1]