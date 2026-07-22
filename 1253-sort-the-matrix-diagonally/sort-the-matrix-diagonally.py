# Brute Force Code 
class Solution:
    # sort every diagonal of the matrix in ascending order
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        # number of rows and columns
        rows = len(mat)
        cols = len(mat[0])
        # function to sort a single diagonal starting from (start_row, start_col)
        def sortdiagonal(start_row, start_col):
            # store all element of the current diagonal
            diagonal = []
            row = start_row
            col = start_col
            # collect the diagonal element
            while row < rows and col < cols:
                diagonal.append(mat[row][col])
                row += 1
                col += 1
            # sort the collected elements
            diagonal.sort()
            # sorted element back into same diagonal
            row = start_row
            col = start_col
            index = 0
            while row < rows and col < cols:
                mat[row][col] = diagonal[index]
                index += 1
                row += 1
                col += 1
        # sort all diagonal that start from the first row
        for col in range(cols):
            sortdiagonal(0, col)
        # sort all diagonal that start from the first column skip the top left cell because its diagonal is already processed
        for row in range(1, rows):
            sortdiagonal(row, 0)
        # return the matrix with all diagonal sorted
        return mat 

# Time Complexity : O(N)
# Space Complexity : O(N)