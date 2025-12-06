"""
This is a leetcode hard

"""


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        answer = []
        if not board or not words:
            return []

        seen = set()

        def dfs(r, c, i, w):
            # i is index of word we are on
            # w = word we are on

            # base case of if we found word
            if i == len(w):
                if w not in seen:
                    answer.append(w)
                    seen.add(w)
                return

            # if we off board or cahr is #
            if (r not in range(rows) or
                    c not in range(cols) or
                    board[r][c] == '#' or
                    board[r][c] != w[i]):
                return

            temp = board[r][c]

            board[r][c] = '#'
            dfs(r + 1, c, i + 1, w)
            dfs(r - 1, c, i + 1, w)
            dfs(r, c + 1, i + 1, w)
            dfs(r, c - 1, i + 1, w)
            board[r][c] = temp

        for r in range(rows):
            for c in range(cols):
                for w in words:
                    if board[r][c] == w[0]:
                        dfs(r, c, 0, w)

        return answer