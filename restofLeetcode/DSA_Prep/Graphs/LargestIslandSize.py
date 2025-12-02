"""
This is just number of islands while keeping track of the largest island you can see
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #this is just number of islands plus total land size

        answer = 0
        if not grid:
            return answer

        #we are going to use DFS to solve this
        from collections import deque

        visited = set() #store tuples (r,c)

        def bfs(r,c):
            q = deque()
            #first add to visited
            visited.add((r,c))

            q.append((r,c))

            #finds the total island
            land = 1
            while q:
                for n in range(0,len(q)):
                    R,C = q.popleft()

                    #call directions
                    direc = [[1,0],[-1,0],[0,1],[0,-1]]
                    for d in direc:
                        row,col = d[0]+R,d[1]+C

                        #logic to check
                        if (row in range(len(grid)) and
                            col in range(len(grid[0])) and
                            grid[row][col] == 1 and
                            (row,col) not in visited):
                            land+=1
                            q.append((row,col))
                            visited.add((row,col))

            return land




        for r in range(0,len(grid)):
            for c in range(0,len(grid[0])):
                if grid[r][c] == 1 and (r,c) not in visited:
                    land = bfs(r,c)
                    print(land)
                    answer = max(land,answer)
        return answer