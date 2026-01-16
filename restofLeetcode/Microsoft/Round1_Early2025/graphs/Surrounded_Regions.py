#here we are given a graph and have to find all o's that have a sounrded region of x's and convert that.

def solution():
    # so for this we are going to keep two sets. The first will keep track of everywhere we have been
    # the second is going to keep track of the current island. When we bfs from there we will hit edge; if we are still within the range on that the we can pop from the set and turn that to x

    ROWS, COLS = len(board), len(board[0])

    # const set and array
    visited = set()
    tmpar = set()  # put the land we find

    # def bfs
    def bfs(r, c):

        # call deque
        q = deque()

        # add (r,c) to visited
        # visited.add((r,c))

        # now append (r,c)
        q.append((r, c))

        while q:
            row, col = q.popleft()
            directions = [1, 0], [-1, 0], [0, 1], [0, -1]

            # capture multiple
            for dr, dc in directions:
                r, c = dr + row, dc + col
                if (r in range(1, ROWS - 1) and
                        c in range(1, COLS - 1) and
                        board[r][c] == 'O' and
                        (r, c) not in visited):
                    q.append((r, c))
                    tmpar.add((r, c))
                    visited.add((r, c))

        # capture singular
        if (r + 1 in range(1, ROWS - 1) and
                r - 1 in range(1, ROWS - 1) and
                c + 1 in range(1, COLS - 1) and
                c - 1 in range(1, COLS - 1) and
                board[r + 1][c] == 'X' and
                board[r - 1][c] == 'X' and
                board[r][c + 1] == 'X' and
                board[r][c - 1] == 'X'):
            # visited.add((r,c))
            print(board[r][c])
            board[r][c] = 'X'

        # fill in land
        for x in tmpar:
            r, c = x
            board[r][c] = 'X'
        tmpar.clear()

    # now we will call all spots in grid
    for r in range(ROWS):
        for c in range(COLS):
            bfs(r, c)