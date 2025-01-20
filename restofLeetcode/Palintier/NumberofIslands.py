#here we are given a matrix graph of 1's and 0's and it is our job to figure out how to find out how many islands are in the graph
grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]

def solution():
    # you can either do this with a bfs solution or a dfs solution. The idea is that you capture the rows,cols and then append those to a deque. From here we then iterate through them and make sure they all hit the required permissions.
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0

    def bfs(r, c):
        q = deque()
        visited.add((r, c))
        q.append((r, c))
        while q:
            row, col = q.popleft()
            # call the directions
            directions = [1, 0], [-1, 0], [0, 1], [0, -1]
            for dr, dc in directions:
                r, c = dr + row, dc + col
                if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == '1' and
                        (r, c) not in visited):
                    q.append((r, c))
                    visited.add((r, c))

    # for loop on rows and cols. If we hit an 'island' 1 then we see if its in visited. If it is not we bfs it.
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                bfs(r, c)
                islands += 1

    return islands

