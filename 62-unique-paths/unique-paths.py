# Brute Force Code & Optimal Code
class Solution:
    def uniquePaths(self, m: int, n: int) -> int: 
        # create 2D memoization tables t with (m + 1) rows and (n + 1) columns, t[i][j] stores the total number of unique paths from the current cell (i, j) to the destination cell (m - 1, n -1) initiallt every cell contains -1 which means that its result has not been calculated yet memoization to avoid calculating the same cell number of paths multiple times 
        t = [[-1] * (n + 1) for _ in range(m + 1)]
        # define the recursive function
        # solve(i, j) returns the number of unique paths from the current cell (i, j) to the destination i = current row index & j = current column index so, can move only : right -> (i, j + 1) & down -> (i + 1, j) moving left or upward is nto allowed
        def solve(i, j):
            # base case 1: destination reached
            # destination is bottom right cell (m - 1, n -1) if the current position is the destination have sucessfully found one complete path therefore return 1
            if i == m - 1 and j == n - 1:
                return 1
            # outside the grid
            # check whether the current row & column index is outside the valid grid boundaries for valid row indices : 0 to m - 1 and valid column indices : 0 to n - 1 if any conditions below is true the current position is outside the grid such path cannot reach the destination so return 0
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            # check memoization
            # before exloring further movements check whether have already calculated the number of paths from the current cell (i, j) if t[i][j] is not -1 the result is already stored return it directly instend of making recursive calls
            if t[i][j] != -1:
                return t[i][j]
            # explore the two possible movements
            # 1. option 1 : move right
            # from the current cell (i, j) move one column to the right new position becomes (i, j + 1) recursive call return the number of valid paths that new position to the destination
            right = solve(i, j + 1)
            # 2. option 2 : move down
            # from the current cell (j, i) move one row downward new position becomes (i + 1, j) recursive call return the number of valid paths from that new position to the destination
            down = solve(i + 1, j)
            # calculated the total number of paths
            # every valid path from the current cell must begin by moving either right or down these two groups of paths are independents 1. right : number of paths starting with right move & 2. down : number of paths staring with down move so add result to get the total number of unique paths from the current cell store the answer in the memoization table so future calls this state can reuse it
            t[i][j] = right + down
            # return the total number of unique paths calculated for the current cell (i, j)
            return t[i][j]
        # start the recursion 
        # starting position is the top left corner : row = 0, column = 0, solve(0, 0) calculated the total number of unique paths from the top left corner to the bottom right corner
        return solve(0, 0)

# Time Complexity : O(N)
# Space Complexity : O(N)