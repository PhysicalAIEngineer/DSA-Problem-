# Optimal Code
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # store the number of rows and columns
        rows = len(matrix)
        cols = len(matrix[0])
        # treat the matrix as virtual 1D sorted array intialize the binary search boundaries
        left = 0
        right = rows * cols - 1
        # perfrom binary search
        while left <= right:
            # find the middle index
            mid = left + (right - left) // 2
            # convert the virtual 1D index into the corresponding 2D coorfinates
            row = mid // cols
            col = mid % cols
            # if the middle element is greater than the target search the left half
            if matrix[row][col] > target:
                right = mid - 1
            # if the middle element is smaller than the target search the right half
            elif matrix[row][col] < target:
                left = mid + 1
            # target found
            else:
                return True
        # target does not exists in the matrix
        return False

# Time Complexity : O(Nlog)
# Space Complexity : O(1)
        