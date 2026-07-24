# Optimal Code
class Solution:
    # check whether the given matrix is a Toeplitz matrix toeplitz matrix has the property that every top-left to bottom-right diagonal contains the same value.
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        # number of rows and columns
        m = len(matrix)
        n = len(matrix[0])
        # traverse the matrix starting from the second row and second column
        for i in range(1, m):
            for j in range(1, n):
                # compare the current element with its top-left diagonal neighbor if they are different the matrix is not Toeplitz
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False
        # every element matches its top-left diagonal neighbor so the matrix is Toeplitz
        return True

# Time Complexity : O(N)
# Space Complexity : O(1)