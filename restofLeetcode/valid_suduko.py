#Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
import collections

#Each row must contain the digits 1-9 without repetition.
#Each column must contain the digits 1-9 without repetition.
#Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
#Note:

#A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#Only the filled cells need to be validated according to the mentioned rules.

#example
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

#contraints
#the board will always be a length of 9 with column length of 9. Will there be any negative numbers? No. Only positive 1-9 numbers and the string '.' representing null are allowed.

#how I would do it. So this is going to be a hashmap problem because we have integers and values needing to be checked. We are going to create a hashmap, add the row, box, and column to it. Then we are going to add condintioanl statements to check to see if the board is valid.

#I had to use Neetcodes solution. Essentially he just created three hashmaps for rows, columns, and squares. Then he added to them as he looped through the arrays and if there was a duplicate he returned false:

def solution():
    cols= collections.defaultdict(set)
    rows=collections.defaultdict(set)
    squares=collections.defaultdict(set)

    for r in range(9):
        for c in range(9):
            if board[r][c]=='.':
                continue
            if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3,c//3)]):
                return False
            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            squares[(r//3,c//3)].add(board[r][c])
    return True
print(solution())