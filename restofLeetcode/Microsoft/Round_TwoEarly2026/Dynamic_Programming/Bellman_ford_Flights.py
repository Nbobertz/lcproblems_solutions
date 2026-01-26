"""
This is an insane problem, that will TLE if you use the bfs approach
"""


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float('inf')

        # dp[v] = cheapest cost to reach v with current number of flights
        dp = [INF] * n
        dp[src] = 0

        # We can take at most k+1 flights
        for _ in range(k + 1):
            tmp = dp[:]  # copy previous state

            for u, v, price in flights:
                if dp[u] != INF:
                    tmp[v] = min(tmp[v], dp[u] + price)

            dp = tmp

        return dp[dst] if dp[dst] != INF else -1