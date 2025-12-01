"""
Here I did the number of islands problem again. Got it first try after not doing it forever
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        answer = 0

        #this is the classic bfs problem
        if not grid:
            return answer

        from collections import deque

        def bfs(r,c):
            visited.add((r,c))

            q = deque()

            q.append((r,c))

            while q:
                for n in range(0,len(q)):
                    node = q.popleft()
                    R,C = node[0],node[1]

                    directions = [[0,1],[0,-1],[1,0],[-1,0]] #up,down,left,right
                    for direc in directions:
                        r2,c2 = direc[0]+R,direc[1]+C

                        #logic to see if it's 1 and in bounds and not in visited
                        if (r2 in range(0,len(grid)) and
                            c2 in range(0,len(grid[0])) and
                            grid[r2][c2] == '1' and
                            (r2,c2) not in visited):
                            q.append((r2,c2))
                            visited.add((r2,c2))





        visited = set()

        for r in range(0,len(grid)):
            for c in range(0,len(grid[0])):

                #check to see if grid is 1
                if grid[r][c] == '1' and (r,c) not in visited:
                    bfs(r,c)
                    answer+=1

        return answer