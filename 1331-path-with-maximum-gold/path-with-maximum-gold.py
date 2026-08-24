# Brute Force Code & Optimal Code
class Solution:
    def __init__ (self):
        # store the number of rows in the grid
        self.m = 0
        # store the number of column in the grid
        self.n = 0
        # four possible direction
        self.directions = [
            [-1, 0], # move up
            [1, 0], # move down
            [0, 1], # move right
            [0, -1], # move left
        ]
    def DFS(self, grid, i, j):
        # base case : stop DFS if:
        # 1. i goes outside the grid
        # 2. j goes outside the grid
        # 3. current cell outside 0 gold
        # in all these cases cannot collect any move gold
        if ( i >= self.m or i < 0 or j >= self.n or j < 0 or grid[i][j] == 0):
            return 0
        # store the original amount of gold present in the current cell need this values because temporarily chage the cell to 0
        originalgoldvalue = grid[i][j]
        # mark current cell as visited set the current cell to 0 so that the same cell cannot be visited again during the current DFS path
        grid[i][j] = 0
        # store the maximum amount of gold that can be collected from neighboring cells
        maxgold = 0
        # try all four directions
        for direction in self.directions:
            # calculate the row of the next cell
            new_i = i + direction[0]
            # calculate the column of the next cell
            new_j = j + direction[1]
            # recursively explore the next cell take the maximum result among all four direction possibles
            maxgold = max(maxgold, self.DFS(grid, new_i, new_j))
        # backtracking restore the original amounf of gold this is important because another DFS starting from diffrent cell should be allowed to use this cell again
        grid[i][j] = originalgoldvalue
        # total grid collected from this path = gold in the current cell + maximum gold collected from neighbours
        return originalgoldvalue + maxgold
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        # number of rows in grid
        self.m = len(grid)
        # number of column in grid
        self.n = len(grid[0])
        # store the maximum amount of gold found amoung all possible paths
        maxgold = 0
        # try every cell as starting point 
        for i in range(self.m):
            for j in range(self.n):
                # only start from cell that contains gold
                if grid[i][j] != 0:
                    # start DFS from this cell and updates the maximum numbers
                    maxgold = max(maxgold, self.DFS(grid, i, j))
        # return the maximum gold that can be collected
        return maxgold

# Time Complexity : O(N)
# Space Complexity : O(N)