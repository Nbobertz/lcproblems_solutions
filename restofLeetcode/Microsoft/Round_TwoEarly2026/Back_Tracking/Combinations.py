"""
This was my 400th problem. It is backtaracking over all possible combinations of size k
"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []

        def dfs(start: int, cur: List[int]):
            # base case: picked k numbers
            if len(cur) == k:
                answer.append(cur[:])
                return

            # choose next numbers
            for x in range(start, n + 1):
                cur.append(x)
                dfs(x + 1, cur)  # move forward
                cur.pop()

        dfs(1, [])
        return answer