"""
This is the multi-bfs solution for walls and gates

"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        answer = 0
        if not grid:
            return answer

        ROWS,COLS = len(grid),len(grid[0])
        visited = set() #store visited places so we don't double up (r,c) as tuple

        from collections import deque

        def dfs(r,c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))

            directions = [[1,0],[-1,0],[0,-1],[0,1]] #up down and left/right

            while q:
                for _ in range(len(q)):
                    node = q.popleft()
                    r,c = node[0],node[1]

                    for d in directions:
                        R,C = d[0]+r,d[1]+c

                        if (R in range(ROWS) and
                            C in range(COLS) and
                            grid[R][C] == '1' and
                            (R,C) not in visited):
                            dfs(R,C)



        #iterate over the grid spot by spot
        for r in range(ROWS):
            for c in range(COLS):
                if (r in range(ROWS) and
                    c in range(COLS) and
                    (r,c) not in visited and
                    grid[r][c] == '1'):
                    dfs(r,c)
                    answer+=1

        return answer