# Brute Force Code & Optimal Code
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        # step 1: calculate the grid dimensions
        # calculate the total number of rows in the obstacle grid len(obstacleGrid) gives the number of rows store this value in 'm'.
        m = len(obstacleGrid)
        # calculate the total number of columns in the obstacle grid obstacleGrid[0] represents the first row len(obstacleGrid[0]) gives the number of columns store this value in 'n'.
        n = len(obstacleGrid[0])
        # step 2: create the memoization tables 
        # create a 2D memoization table 't' with: - m rows & - n columns initially, every cell contains -1. meaning of values:
        # -1 -> The answer for this cell has not been calculated.
        #  0 -> There are no valid paths from this cell.
        # >0 -> The number of valid paths from this cell
        #       to the destination.
        # t[i][j] stores the number of valid paths from cell (i, j) to the destination cell (m - 1, n - 1) use memoization to avoid calculating the same subproblem multiple times.
        t = [[-1] * n for _ in range(m)]
        # step 3: define the recursive function 
        # solve(i, j) calculates the number of valid paths from the current cell (i, j) to the destination.
        # 'i' represents the current row index.
        # 'j' represents the current column index.
        # from the current cell, we can make only two movements:
        # 1. right -> (i, j + 1)
        # 2. down  -> (i + 1, j)
        def solve(i, j):
            # base case 1: outside the grid 
            # check whether the current position is outside the boundaries of the grid.
            # i >= m -> We have moved below the last row.
            # j >= n -> We have moved beyond the last column.
            # since these positions do not exist in the grid they cannot contribute to a valid path therefore, return 0.
            if i >= m or j >= n:
                return 0
            # base case 2: obstacle cell 
            # Check whether the current cell contains an obstacle obstacleGrid[i][j] == 1 means that this cell contains an obstacle cannot move through an obstacle therefore, reaching this cell means that the current path is invalid return 0 because no valid path can continue through this cell.
            if obstacleGrid[i][j] == 1:
                return 0
            # base case 3: destination reached 
            # check whether the current position is the bottom-right destination cell the destination coordinates are: (m - 1, n - 1) if reach the destination and it is not an obstacle, we have successfully completed one valid path therefore, return 1.
            if i == m - 1 and j == n - 1:
                return 1
            # step 4: check the memoization tables 
            # check whether we have already calculated the number of valid paths from the current cell (i, j) if t[i][j] is not equal to -1, the answer has already been calculated and stored return the stored result instead of exploring the same cell again this prevents repeated calculations and improves the efficiency of the recursive solution.
            if t[i][j] != -1:
                return t[i][j]
            # step 5: explore the two possible movements 
            # option 1: move right
            # to move right:
            # - row index 'i' remains unchanged.
            # - column index 'j' increases by 1.
            # next cell becomes (i, j + 1) recursively calculate the number of valid path from that next cell to the destination if the next cell is an obstacle or outside the grid the recursive function will return 0 store the result in the variable 'right'.
            right = solve(i, j + 1)
            # option 2: move down 
            # to move down:
            # - row index 'i' increases by 1.
            # - column index 'j' remains unchanged.
            # the next cell becomes (i + 1, j) recursively calculate the number of valid paths from that next cell to the destination if the next cell is an obstacle or outside the grid the recursive function will return 0 store the result in the variable 'down'.
            down = solve(i + 1, j)
            # step 6: calculate and store the total paths
            # there are two possible ways to continue from the current cell:
            # 1. move right and count all valid paths from there.
            # 2. move down and count all valid paths from there.
            # total valid paths = paths moving right + paths moving down & add both results and store the answer in t[i][j]. if both directions are blocked, both values will be 0, and the current cell will have 0 valid paths.
            t[i][j] = right + down
            # return the calculated number of valid paths from the current cell (i, j) to the destination.
            return t[i][j]
        # step 7: start the recursion 
        # start calculating the number of valid paths from the top-left corner of the grid, which is (0, 0) solve(0, 0) explores all possible right and down movements while avoiding obstacles finally, return the total number of valid paths from the starting cell to the destination.
        return solve(0, 0)

# Time Complexity : O(N)
# Space Complexity : O(N)