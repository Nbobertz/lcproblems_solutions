"""
Here I did wordearch problem
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r, c, i):
            # base case
            if i == len(word):
                # the word is here
                return True
            if (r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or word[i] != board[r][c]
                    or board[r][c] == '#'):
                # out of bound, character is not in word, or charcter is nonchar
                return False

            board[r][c] = '#'  # instaed of keeping a set to keep track of visited
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            board[r][c] = word[i]
            return res

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    # found possible first letter of word
                    answer = dfs(r, c, 0)
                    if answer == True:
                        return True
        return False