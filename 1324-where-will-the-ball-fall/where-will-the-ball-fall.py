# Optimal Code
class Solution:
    # simulate the path of every ball through the grid and return the column where each ball exists
    def findBall(self, grid: List[List[int]]) -> List[int]:
        # number of rows and columns
        m = len(grid)
        n = len(grid[0])
        # store the final position of every ball
        result = []
        # drop one ball from each column
        for ball in range(n):
            # current position of the ball 
            row = 0
            col = ball
            # track whether the ball successfully exists
            reached = True
            # move the ball until it reaches the bottom or gets stuck
            while row < m and col < n:
                # current board slopes to the right
                if grid[row][col] == 1:
                    # ball gets stuck if it hits the right wall or it form v shape with the next board
                    if col == n - 1 or grid[row][col + 1] == -1:
                        reached = False
                        break
                    # move one column right
                    col += 1
                # current board slopes to the left
                elif grid[row][col] == -1:
                    # ball gets stuck if it hits the left wall or it forms v shape with  the previous board
                    if col == 0 or grid[row][col - 1] == 1:
                        reached = False
                        break
                    # move one column left
                    col -= 1
                # move down to the next row
                row += 1
            # if the ball reaches the bottom store its exits column otherwise store -1
            if reached:
                result.append(col)
            else:
                result.append(-1)
        # return the result for every starting column
        return result 

# Time Complexity : O(N)
# Space Complexity : O(N)