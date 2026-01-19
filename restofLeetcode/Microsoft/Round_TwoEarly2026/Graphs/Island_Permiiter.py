"""
This checks the permiter of the one island we are given on the map
"""


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        answer = 0
        if not grid:
            return answer

        from collections import deque
        q = deque()
        visited = set()  # stores tuples of places we have seen so far, prevents max recursion depth (r,c)

        def bfs(r, c):
            nonlocal answer
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # up, down, right, left
            tup = (r, c)
            visited.add(tup)

            q.append(tup)

            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in directions:
                        rr, cc = r + dr, c + dc

                        # check to see if out of bounds or water then incrment answer by 1
                        if (rr not in range(len(grid)) or
                                cc not in range(len(grid[0])) or
                                grid[rr][cc] == 0):
                            answer += 1

                        # see if we need to add to q
                        if (rr in range(len(grid)) and
                                cc in range(len(grid[0])) and
                                grid[rr][cc] == 1 and
                                (rr, cc) not in visited):
                            tup2 = (rr, cc)
                            q.append(tup2)
                            visited.add(tup2)

        for R in range(len(grid)):
            for C in range(len(grid[0])):
                tuptup = (R, C)
                if grid[R][C] == 1 and tuple(tuptup) not in visited:
                    bfs(R, C)
        return answer
