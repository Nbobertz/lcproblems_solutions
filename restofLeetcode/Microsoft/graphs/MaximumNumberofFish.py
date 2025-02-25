#here we are given a graph of 0's and integers. Anything that is not a 0 is a total amount of fish for that spot.
#a fisherman can do one of two things; first fish his waterhing hole and then move to the next one to fish
# Write an algorithm that will return the total amount of fish he could possibly return if he choses his watering hole properly
from collections import deque


#Hint: this is just largest island with another step

grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]

def solution():
    # so this is a game about fish. At any point a fisherman can look to the left, up, down, or right and see if there is more fish. This is just largest island I think but with fish values.

    ROWS, COLS = len(grid), len(grid[0])
    visited = set()  # store as tuples
    mfish = 0  # return max number of fish on fishing trip

    def bfs(r, c):

        # use deque for bfs
        q = deque()

        # add to visited so we don't double up
        visited.add((r, c))
        fish = grid[r][c]

        q.append((r, c))
        while q:
            row, col = q.popleft()
            directions = [0, 1], [0, -1], [1, 0], [-1, 0]
            for dr, dc in directions:
                r, c = dr + row, dc + col
                if (r in range(ROWS) and
                        c in range(COLS) and
                        grid[r][c] > 0 and
                        (r, c) not in visited):
                    fish = grid[r][c] + fish
                    q.append((r, c))
                    visited.add((r, c))
        return fish

    for r in range(ROWS):
        for c in range(COLS):
            if (grid[r][c] > 0 and
                    (r, c) not in visited):
                fishy = bfs(r, c)
                mfish = max(mfish, fishy)

    return mfish


print(solution())