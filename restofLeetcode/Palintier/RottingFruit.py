#here we are given a graph and 3 possible integers in each spot. 1 = fresh fruit, 2 = rotten fruit, 3 = nothing

#the idea is that every revolution (minute) rotten fruit will spoil all fresh fruit near it. Our goal is to figure out how many minutes it will take to spoil all rotten fruit

grid = [[2,1,1],[1,1,0],[0,1,1]]

def solution():
    class Solution:
        def orangesRotting(self, grid: List[List[int]]) -> int:
            q = collections.deque()
            fresh = 0
            time = 0

            for r in range(len(grid)):
                for c in range(len(grid[0])):
                    if grid[r][c] == 1:
                        fresh += 1
                    if grid[r][c] == 2:
                        q.append((r, c))

            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            while fresh > 0 and q:
                length = len(q)
                for i in range(length):
                    r, c = q.popleft()

                    for dr, dc in directions:
                        row, col = r + dr, c + dc
                        if (row in range(len(grid))
                                and col in range(len(grid[0]))
                                and grid[row][col] == 1
                        ):
                            grid[row][col] = 2
                            q.append((row, col))
                            fresh -= 1
                time += 1
            return time if fresh == 0 else -1