# Brute Force Code & Optimal Code
class Solution:
    # perform DFS to determine whether the current island is completely surrounded by water
    def dfs(self, grid: list[list[int]], row: int, col: int) -> bool:
        # if move outside the grid the island touches the boundary so it is not a closed island
        if (row < 0 or row >= self.m or col < 0 or col >= self.n):
            return False
        # if the current cell is water or has already been visited this direction is considered closed
        if grid[row][col] == 1:
            return True
        # mark the current land cell as visited by converting it to water
        grid[row][col] = 1
        # explore all four neighboring cells
        left = self.dfs(grid, row, col - 1)
        right = self.dfs(grid, row, col + 1)
        up = self.dfs(grid, row - 1, col)
        down = self.dfs(grid, row + 1, col)
        # island is closed only if every direction remains closed
        return (left and right and up and down)
    # return the total number of closed islands
    def closedIsland(self, grid: list[list[int]]) -> int:
        # number of rows
        self.m = len(grid)
        # number of columns
        self.n = len(grid[0])
        # store the number of closed islands
        count = 0
        # traverse every cell in the grid
        for i in range(self.m):
            for j in range(self.n):
                # start DFS from every unvisited land cell
                if grid[i][j] == 0:
                    count += self.dfs(grid, i,j)
        # return the total number of closed islands
        return count

# Time Complexity : O(N)
# Space Complexity : O(N)