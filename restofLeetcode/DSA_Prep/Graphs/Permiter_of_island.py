"""
Here we want to find the permiter of islands on the graph
"""


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perm = 0
        if not grid:
            return perm


        visited = set()


        from collections import deque

        def bfs(r,c):
            visited.add((r,c))

            q = deque()

            q.append((r,c))
            pp = 0
            while q:
                for n in range(len(q)):
                    r,c = q.popleft()

                    directions = [[1,0],[-1,0],[0,-1],[0,1]]
                    for d in directions:
                        R,C = d[0]+r,d[1]+c

                        #if we find another peice of land
                        if (R in range(len(grid)) and
                            C in range(len(grid[0])) and
                            grid[R][C] == 1 and
                            (R,C) not in visited):
                            q.append((R,C))
                            visited.add((R,C))

                        elif (R not in range(len(grid)) or
                            C not in range(len(grid[0])) or
                            grid[R][C] == 0):
                            pp+=1

            return pp

        for R in range(len(grid)):
            for C in range(len(grid[0])):
                if grid[R][C] == 1 and (R,C) not in visited:
                    perm = bfs(R,C)
                    return perm