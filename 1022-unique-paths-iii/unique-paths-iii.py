# Brute Force Code & Optimal Code
class Solution:
    def __init__(self):
        # store the number of rows in the grid
        self.m = 0
        # store the number of column in the grid
        self.n = 0
        # store the total number of non obstables cells that must be visited this includes all empty cells(0) and starting cell(1) at ending cell(2) is checked seperately
        self.emptyCells = 0
        # store the total number of valid paths that visit every requied cell exactly onces 
        self.result = 0
        # four possible movement from the current cells
        self.directions = [
            [1, 0], # move down
            [-1, 0], # move up
            [0, 1], # move right
            [0, -1], # move left
        ]
    def dfs(self, grid, curr_count, i, j):
        # check whether the current cell is valid stop the current path if:
        # 1. row is outside the grid
        # 2. column is outside the grid
        # 3. cell is an obstacles
        # 4. cell was already visited
        # use -1 to represent both obstacles and temporarily visited cells
        if (i < 0 or i >= self.m or j < 0 or j >= self.n or grid[i][j] == -1):
            return
        # check whether reached the ending cell once reach the ending square cannot continue walking so pathn is valid only if every required non obstacles cell has been visited exactly onces
        if grid[i][j] == 2:
            # if curr_count equals emptycell all required cells have been visited
            if curr_count == self.emptyCells:
                # found once valid path
                self.result += 1
            # whether valid or invalid stop this path because the ending cell has been reached
            return
        # mark the current cell as visited set the current cell to -1 so that do not visit the same cell again during this path
        grid[i][j] = -1
        # try all four direction possible
        for direction in self.directions:
            # calculate the coorinates of the next cell
            new_i = i + direction[0]
            new_j = j + direction[1]
            # recursively explore the next cell so curr_count + 1 means that the current cell has now been visited so increase the count before moving to the next cell
            self.dfs(grid, curr_count + 1, new_i, new_j)
        # backtracking restore the current cell after exploring all possible paths from it this allow the cell to be used again when exploring diffrent path
        grid[i][j] = 0
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        # number of row
        self.m = len(grid)
        # number of column
        self.n = len(grid[0])
        # reset the numnber of required cells and the number of valid paths
        self.emptyCells = 0
        self.result = 0
        # variables to store the starting cell
        start_x = 0
        start_y = 0
        # find the starting cell and cound all empty cells
        for i in range(self.m):
            for j in range(self.n):
                # if the cell is 0 it is an empy cell that must be visited
                if grid[i][j] == 0:
                    self.emptyCells += 1
                # if the cell is 1 store its coorinates becasue DFS must start from here
                if grid[i][j] == 1:
                    start_x = i
                    start_y = j
        # include the starting cell in the number of cells that must be visited need to visit every non obstacles cell exactly once before reaching the ending cell
        self.emptyCells += 1
        # start DFS curr_count = 0 because no cell has been counted as visited before DFS starts
        curr_count = 0
        # start exploring from the starting cell
        self.dfs(grid, curr_count, start_x, start_y)
        # return the total number of valid paths
        return self.result

# Time Complexity : O(N)
# Space Complexity : O(N)