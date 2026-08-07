# Brute Force Code & Optimal Code
class Solution:
    def __init__(self):
        # four possible movement directions:
        # 1. [-1, 0] -> up
        # 2. [1, 0]  -> down
        # 3. [0, -1] -> left
        # 4. [0, 1]  -> right
        self.directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        # number of rows and columns these will be initialized in minDays().
        self.m = 0
        self.n = 0
    def DFS(self, grid, i, j, visited):
        # stop DFS if the current cell is invalid.
        # stop when:
        # 1. go outside the grid.
        # 2. cell was already visited.
        # 3. cell is water (0).
        if (i < 0 or i >= self.m or j < 0 or j >= self.n or visited[i][j] or grid[i][j] == 0):
            return
        # mark the current land cell as visited this prevents visiting the same cell again.
        visited[i][j] = True
        # explore all four neighboring cells.
        for direction in self.directions:
            # calculate the neighboring row.
            new_i = i + direction[0]
            # calculate the neighboring column.
            new_j = j + direction[1]
            # recursively explore the neighboring cell.
            self.DFS(grid, new_i, new_j, visited)
    def numberOfIslandsDFS(self, grid):
        # create a visited matrix visited[i][j] = False means the cell has not been visited yet.
        visited = [[False] * self.n for _ in range(self.m)]
        # store the total number of islands.
        islands = 0
        # visit every cell in the grid.
        for i in range(self.m):
            for j in range(self.n):
                # if find an unvisited land cell it is the starting point of a new island.
                if (not visited[i][j] and grid[i][j] == 1):
                    # DFS visits every connected land cell belonging to this island.
                    self.DFS(grid, i, j, visited)
                    # one complete DFS traversal represents one island.
                    islands += 1
        # return the total number of islands.
        return islands
    def minDays(self, grid):
        # number of rows.
        self.m = len(grid)
        # number of columns.
        self.n = len(grid[0])
        # Count how many islands currently exist.
        islands = self.numberOfIslandsDFS(grid)
        # Case 1:
        # 1. if there are already multiple islands the grid is already disconnected.
        # 2. if there are no islands at all it is also already disconnected.
        # 3. therefore, no removal is required.
        # --------------------------------------------------
        if islands > 1 or islands == 0:
            return 0
        # Case 2:
        # 1. try removing every land cell one at a time.
        # 2. if removing one cell causes:
        #     a. More than one island OR
        #     b. No islands
        # then one day/removal is enough.
        for i in range(self.m):
            for j in range(self.n):
                # only land cells can be removed.
                if grid[i][j] == 1:
                    # temporarily remove this land cell.
                    grid[i][j] = 0
                    # count the islands after removing it.
                    islands = self.numberOfIslandsDFS(grid)
                    # restore the cell because want to test other cells as well.
                    grid[i][j] = 1
                    # if the grid becomes disconnected or completely loses its island only one removal was necessary.
                    if islands > 1 or islands == 0:
                        return 1
        # Case 3:
        # 1. grid originally had exactly one island and removing any single land cell did not disconnect it.
        # 2. according to the problem constraints, at most two removals are always sufficient.
        return 2

# Time Complexity : O(N)
# Space Complexity : O(N)