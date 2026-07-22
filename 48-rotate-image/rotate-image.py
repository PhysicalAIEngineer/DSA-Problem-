# Brute Force Code & Optimal Code
class Solution:
    def rotate(self, matrix: List[List[int]]):
        # size of the square matrix
        n = len(matrix)
        # compute the transpose of the matrix swap matrix[i][j] with matrix[j][i] for all element on and above the main diagonal
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # reverse every row
        for i in range(n):
            matrix[i].reverse()

# Time Complexity : O(N^2)
# Space Complexity : O(N)