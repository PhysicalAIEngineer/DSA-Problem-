# Brute Force Code & Optimal Code
class Solution:
    def restoreMatrix(self, rowsum: List[int], colsum: List[int]):
        # number of rows
        m = len(rowsum)
        # number of column
        n = len(colsum)
        # create an m * n matrix intially filled with 0
        matrix = [[0] * n for _ in range(m)]
        # i point to the current row
        i = 0
        # j point to the current column
        j = 0
        # continue unitl have processed all rows or all columns
        while i < m and j < n:
            # put the largest possible values into the current cell value cannot be greater than : remaining sum required by this row and remaining sum required by this column
            matrix[i][j] = min(rowsum[i], colsum[j])
            # substract the values placed in the cell from the remaining row sum
            rowsum[i] -= matrix[i][j]
            # subtract the same value from the remaining column sum
            colsum[j] -= matrix[i][j]
            # if the current row has reached its required sum move to the next row
            if rowsum[i] == 0:
                i += 1
            # if the current column has reached its required sum move ot the next column
            if colsum[j] == 0:
                j += 1
        # return the restored matrix
        return matrix

# Time Complexity : O(N)
# Space Complexity : O(N)        