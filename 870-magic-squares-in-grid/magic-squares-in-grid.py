# Brute Force Code & Optimal Code
class Solution:
    def is_magic_grid(self, grid: list[list[int]], r: int, c: int) -> bool:
        # check whether the 3x3 subgrid contains all numbers from 1 to 9 exactly once so, set is used to keep track of numbers that have already appeared.
        seen = set()
        # visit all 9 cells of the 3x3 subgrid.
        for i in range(3):
            for j in range(3):
                # get the current number.
                num = grid[r + i][c + j]
                # valid magic square can only contain numbers from 1 to 9.if the number is outside this range the subgrid is invalid.if the number already exists in 'seen' there is a duplicate number.
                if num < 1 or num > 9 or num in seen:
                    return False
                # add the number to the set.
                seen.add(num)
        # calculate the required magic sum every row, column, and diagonal must have the same sum so use the first row as the reference sum
        magic_sum = (grid[r][c] + grid[r][c + 1] + grid[r][c + 2])
        # check all 3 rows and all 3 columns.
        for i in range(3):
            # calculate the sum of the current row.
            row_sum = (grid[r + i][c] + grid[r + i][c + 1] + grid[r + i][c + 2])
            # every row must have the same sum as the first row.
            if row_sum != magic_sum:
                return False
            # calculate the sum of the current column.
            col_sum = (grid[r][c + i] + grid[r + 1][c + i] + grid[r + 2][c + i])
            # every column must also have the same sum.
            if col_sum != magic_sum:
                return False
        # check the main diagonal.
        # main diagonal: (r, c), (r+1, c+1), (r+2, c+2)
        diagonal_sum = (grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2])
        # main diagonal must have the magic sum.
        if diagonal_sum != magic_sum:
            return False
        # check the anti-diagonal.
        # anti-diagonal: (r, c+2), (r+1, c+1), (r+2, c)
        anti_diagonal_sum = (grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c])
        # anti-diagonal must also have the same magic sum.
        if anti_diagonal_sum != magic_sum:
            return False
        # all conditions are satisfied so this 3x3 subgrid is a magic square.
        return True
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        # number of rows in the entire grid.
        rows = len(grid)
        # number of columns in the entire grid.
        cols = len(grid[0])
        # store the total number of magic squares.
        count = 0
        # try every possible top-left corner of a 3x3 subgrid rows - 2 and cols - 2 ensure that the complete 3x3 subgrid stays inside the original grid.
        for i in range(rows - 2):
            for j in range(cols - 2):
                # check whether the 3x3 subgrid starting at (i, j) is a magic square.
                if self.is_magic_grid(grid, i, j):
                    # found one valid magic square.
                    count += 1
        # return the total number of magic squares.
        return count

# Time Complexity : O(N)
# Space Complexity : O(1)