"""
This is backtracking problem where we need to hit the exact number
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        if not candidates:
            return answer

        def dfs(i,curlist,total):
            if total == target:
                answer.append(curlist[:])
                return
            if i >= len(candidates) or total > target:
                return

            curlist.append(candidates[i])
            dfs(i,curlist,total+candidates[i])
            curlist.pop()
            dfs(i+1,curlist,total)
            return
        dfs(0,[],0)
        return answer
