#here we are given a bunch of arrays and the idea is that we will have to iterate through them to figure out if a word exists within the arrays. The best way to do this is with bfs
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

def solution():
    ROWS, COLS = len(board), len(board[0])

    path = set()

    def dfs(r, c, i):
        # handle base case
        if i == len(word):
            return True
        if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                (r, c) in path):
            return False

        # add path, call DFS
        path.add((r, c))
        res = (dfs(r + 1, c, i + 1) or
               dfs(r - 1, c, i + 1) or
               dfs(r, c + 1, i + 1) or
               dfs(r, c - 1, i + 1))
        path.remove((r, c))
        return res

    for r in range(ROWS):
        for c in range(COLS):
            if dfs(r, c, 0) == True:
                return True
    return False

print(solution())