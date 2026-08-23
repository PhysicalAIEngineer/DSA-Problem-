# Brute Force Code & Optimal Code
class Solution:
    # count the total number of negative values present in the matrix
    def countNegatives(self, grid: list[list[int]]) -> int:
        # number of rows in the matrix
        m = len(grid)
        # number of columns in the matrix
        n = len(grid[0])
        # store the total count of negative numbers
        result = 0
        # traverse every row
        for i in range(m):
            # traverse every column of the current row
            for j in range(n):
                # check whether the current element is negative
                if grid[i][j] < 0:
                    result += 1
        # return the total number of negative elements
        return result

# Time Complexity : O(N^2)
# Space Complexity : O(N)