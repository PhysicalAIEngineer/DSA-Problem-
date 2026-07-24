# Brute Force Code
class Solution:
    # check whether the given matrix is a Toeplitz matrix in a Toeplitz matrix, every top-left to bottom-right diagonal contains the same value.
    def isToeplitzMatrix(self, matrix):
        # number of rows and columns
        rows = len(matrix)
        cols = len(matrix[0])
        # check all diagonals that start from the first row
        for start_col in range(cols):
            # first value of the current diagonal
            diagonal_value = matrix[0][start_col]
            row = 0
            col = start_col
            # traverse the current diagonal
            while row < rows and col < cols:
                # if any value differs the matrix is not Toeplitz
                if matrix[row][col] != diagonal_value:
                    return False
                # move to the next cell on the diagonal
                row += 1
                col += 1
        # check all diagonals that start from the first column skip the first row because those diagonals were already checked.
        for start_row in range(1, rows):
            # first value of the current diagonal
            diagonal_value = matrix[start_row][0]
            row = start_row
            col = 0
            # traverse the current diagonal
            while row < rows and col < cols:
                # if any value differs the matrix is not Toeplitz
                if matrix[row][col] != diagonal_value:
                    return False
                # move to the next cell on the diagonal
                row += 1
                col += 1
        # every diagonal contains identical values
        return True

# Time Complexity : O(N^2)
# Space Complexity : O(N)