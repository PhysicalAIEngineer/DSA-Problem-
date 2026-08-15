# Brute Force Code & Optimal Code
class Solution:
    def __init__ (self):
        # list to store the all valid board configuration
        self.result = []
    # backtracking function to place queens row by rows
    def solve(self, board: list[list[str]], row: int, columns: set[int], diagonals: set[int], anti_diagonals: set[int]):
        # if queens have been placed in all rows store the current board configurations
        if row == len(board):
            self.result.append(["".join(r) for r in board])
            return 
        # try placing a queen in every column of the current rows
        for col in range(len(board)):
            # compute the current diagonal identifiers
            diagonal_id = row - col
            antidiagonal_id = row + col
            # skip this position if it is already under attack
            if (col in columns or diagonal_id in diagonals or antidiagonal_id in anti_diagonals):
                continue
            # mark the current column and diagonal as occupieds
            columns.add(col)
            diagonals.add(diagonal_id)
            anti_diagonals.add(antidiagonal_id)
            # place the queens
            board[row][col] = "Q"
            # recursively for the next rows
            self.solve(board, row + 1, columns, diagonals, anti_diagonals)
            # remove the queens and free the columns and diagonals
            columns.remove(col)
            diagonals.remove(diagonal_id)
            anti_diagonals.remove(antidiagonal_id)
            board[row][col] = "."
    # return all valid N-Queens configurations 
    def solveNQueens(self, n: int) -> List[List[str]]:
        # if the boards size is zeros, return any empty list
        if n == 0:
            return []
        # clear any previous stored solutions
        self.result = []
        # create an empty n * n solutions
        board = [["." for _ in range(n)] for _ in range(n)]
        # sets to keep track of occupied columns main diagonals and anti-diagonals
        columns = set()
        diagonals = set()
        anti_diagonals = set()
        # start placing queens from first rows
        self.solve(board, 0, columns, diagonals, anti_diagonals)
        # return all valid board configurations
        return self.result

# Time Complexity : O(N)
# Space Complexity : O(N)