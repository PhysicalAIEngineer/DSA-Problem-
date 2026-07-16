# Optimal Code
class Solution:
    def __init__(self):
        # list to store all valid board configurations
        self.result = []
    # backtracking function to place queens row by row
    def solve(self, board: list[list[str]], row: int, columns: set[int], diagonals: set[int], anti_diagonals: set[int]) -> None:
        # if queens have been placed in all rows, store the current board configuration
        if row == len(board):
            self.result.append(["".join(r) for r in board])
            return
        # try placing a queen in every column of the current row
        for col in range(len(board)):
            # compute the current diagonal identifiers
            diagonal_id = row - col
            anti_diagonal_id = row + col
            # skip this position if it is already under attack
            if (col in columns or diagonal_id in diagonals or anti_diagonal_id in anti_diagonals):
                continue
            # mark the current column and diagonals as occupied
            columns.add(col)
            diagonals.add(diagonal_id)
            anti_diagonals.add(anti_diagonal_id)
            # place the queen
            board[row][col] = 'Q'
            # recur for the next row
            self.solve(board, row + 1, columns, diagonals,anti_diagonals)
            # remove the queen and free the column and diagonals
            columns.remove(col)
            diagonals.remove(diagonal_id)
            anti_diagonals.remove(anti_diagonal_id)
            board[row][col] = '.'
    # return all valid N-Queens configurations
    def solveNQueens(self,n: int) -> list[list[str]]:
        # if the board size is zero, return an empty list
        if n == 0:
            return []
        # clear any previous stored solutions
        self.result = []
        # create an empty n x n chessboard
        board = [['.' for _ in range(n)] for _ in range(n)]
        # sets to keep track of occupied columns main diagonals and anti-diagonals
        columns = set()
        diagonals = set()
        anti_diagonals = set()
        # start placing queens from the first row
        self.solve(board,0,columns,diagonals,anti_diagonals)
        # return all valid board configurations
        return self.result

# Time Complexity : O(N)
# Space Complexity : O(N^2)