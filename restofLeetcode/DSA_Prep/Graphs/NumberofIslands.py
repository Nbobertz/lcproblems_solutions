#This is the famous number of islands problem. It's just a graph and finding out how many number of islands there are in the graph
class Solution(object):
    def numIslands(self, grid):
        # assumption: from collections import deque

        # this is a bfs solution,
        islands = 0
        visited = set()  # add as tuples

        if len(grid) == 0:
            return answer  # no grid

        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            # run a bfs algorithm

            # add to set to ensure we do not double up
            visited.add((r, c))

            q = deque()

            q.append((r, c))

            while q:
                R, C = q.popleft()
                directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # left,right,down,up
                for dr, dc in directions:
                    row, col = dr + R, dc + C
                    print(row, col)
                    if (row in range(rows) and
                            col in range(cols) and
                            grid[row][col] == 1):
                        q.append((row, col))
                        visited.add((row, col))
                        print(visited)

        # at this point we have a grid
        for r in range(0, len(grid)):
            for c in range(0, len(grid[0])):
                # print(grid[r][c])
                if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == '1' and
                        (r, c) not in visited):
                    print('here')
                    islands += 1
                    bfs(r, c)

        return islands
