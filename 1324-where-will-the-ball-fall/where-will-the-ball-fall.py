# Brute Force Code
class Solution:
    # simulate the movement of each ball through the grid and return the column where each ball exits
    def findBall(self, grid):
        # number of rows and columns
        rows = len(grid)
        cols = len(grid[0])
        # store the final position of every ball
        answer = []
        # drop one ball from every column
        for start_col in range(cols):
            # current position of the ball
            row = 0
            col = start_col
            # track whether the ball gets stuck
            stuck = False
            # move the ball through each row
            while row < rows:
                # board redirects the ball to the right
                if grid[row][col] == 1:
                    # ball hits the right boundary
                    if col == cols - 1:
                        stuck = True
                        break
                    # ball gets trapped in a V-shaped pattern: 1, -1
                    if grid[row][col + 1] == -1:
                        stuck = True
                        break
                    # move the ball one column right
                    col += 1
                # board redirects the ball to the left
                else:
                    # ball hits the left boundary
                    if col == 0:
                        stuck = True
                        break
                    # ball gets trapped in a V-shaped pattern: 1, -1
                    if grid[row][col - 1] == 1:
                        stuck = True
                        break
                    # move the ball one column left
                    col -= 1
                # move the ball to the next row
                row += 1
            # store the result for the current ball
            if stuck:
                answer.append(-1)
            else:
                answer.append(col)
        # return the exit column for every ball
        return answer

# Time Complexity : O(N^2)
# Space Complexity : O(N)