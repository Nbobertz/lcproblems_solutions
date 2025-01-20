#here we want to find the maximum area of an island and return it as an integer

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

def solution():
    # call the rows and columns
    ROWS, COLS = len(grid), len(grid[0])  # len of grid and columns
    visit = set()  # set of tuples

    # dfs()
    def dfs(r, c):
        # recursive operations
        if (r < 0 or r == ROWS or
                c < 0 or c == COLS or
                grid[r][c] == 0 or (r, c) in visit):
            return 0

        # now add to visit
        visit.add((r, c))

        # now add up all recursive calls in each direction
        return (1 + dfs(r + 1, c) +
                dfs(r - 1, c) +
                dfs(r, c + 1) +
                dfs(r, c - 1))

    # nested for loops to go over everything in the grid
    area = 0
    for r in range(ROWS):
        for c in range(COLS):
            # ensures we go over everything
            if grid[r][c] == 1 and (r, c) not in visit:
                area = max(area, dfs(r, c))  # call dfs and return the max value of all dfs possiblities

    return area

print(solution())