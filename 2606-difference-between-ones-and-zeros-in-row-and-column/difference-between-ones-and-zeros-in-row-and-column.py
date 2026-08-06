# Brute Force Code & Optimal Code
class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        # number of rows in the grid
        m = len(grid)
        # number of columns in the grid
        n = len(grid[0])
        # store the number of 1s in every row rowOnes[i] = number of 1s in row i
        rowOnes = [0] * m
        # store the number of 1s in every column colOnes[j] = number of 1s in column j
        colOnes = [0] * n
        # traverse every cell of the grid
        for i in range(m):
            for j in range(n):
                # if the current cell contains 1 increase the count for its row and column.
                if grid[i][j] == 1:
                    rowOnes[i] += 1
                    colOnes[j] += 1
        # create the answer matrix diff[i][j] will store the difference value for cell (i, j).
        diff = [[0] * n for _ in range(m)]
        # calculate the answer for every cell
        for i in range(m):
            for j in range(n):
                # number of 1s in row i
                onesRowi = rowOnes[i]
                # number of 1s in column j
                onesColj = colOnes[j]
                # total elements in row i are n therefore zeros in row = total elements - ones
                zerosRowi = n - onesRowi
                # total elements in column j are m therefore zeros in column = total elements - ones
                zerosColj = m - onesColj
                # calculate the required difference formula: diff[i][j] = ones in row + ones in column - zeros in row - zeros in column
                diff[i][j] = (onesRowi + onesColj - zerosRowi - zerosColj)
        # return the completed difference matrix
        return diff

# Time Complexity : O(N^2)
# Space Complexity : O(N)