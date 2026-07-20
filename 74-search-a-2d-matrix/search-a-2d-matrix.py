# Brute Force Code
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # traverse each row of the matrix
        for row in matrix:
            # traverse every element in the current row
            for num in row:
                # if the target element is found return true immediately
                if num == target:
                    return True
        # target is not present in the entire matrix
        return False

# Time Complexity : O(N^2)
# Space Complexity : O(1) 
        