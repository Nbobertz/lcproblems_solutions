"""
This is one of my favorite problems as it is easy to type, and complext to understand
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        answer = 0

        #if not given area
        if not grid:
            return answer

        rows = len(grid)
        cols = len(grid[0])

        ss = set()
        def bfs(r, c):
            from collections import deque

            q = deque([(r, c)])
            ss.add((r, c))

            directions = [(0,1), (0,-1), (1,0), (-1,0)]

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    R = row + dr
                    C = col + dc

                    if (0 <= R < rows and
                        0 <= C < cols and
                        (R, C) not in ss and
                        grid[R][C] == '1'):

                        ss.add((R, C))
                        q.append((R, C))

        for R in range(len(grid)):
            for C in range(len(grid[0])):
                if grid[R][C] == '1' and (R,C) not in ss:
                    answer+=1
                    bfs(R,C)

        return answer