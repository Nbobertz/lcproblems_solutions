"""
Here I am doing combination sum, this is important because we are including all possible integers
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def dfs(i, cur, total):
            # cur == []
            # handle base case

            # what if it equals to target
            if total == target:
                answer.append(cur.copy())
                return

            if i >= len(candidates) or total > target:
                return

            # cur == current array of numbers
            cur.append(candidates[i])

            # dfs down this number ex. 0th index
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return answer