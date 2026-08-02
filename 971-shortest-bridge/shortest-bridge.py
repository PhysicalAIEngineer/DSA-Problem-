# Brute Force Code & Optimal Code
from collections import deque
class Solution:
    def __init__(self):
        # number of rows and columns
        self.m = 0
        self.n = 0
        # four possible movement directions: up, left, right, down
        self.directions = [
            (-1, 0),  # up
            (0, -1),  # left
            (0, 1),   # right
            (1, 0)    # down
        ]
    # check whether a cell (i, j) is inside the grid
    def isSafe(self, i: int, j: int) -> bool:
        return 0 <= i < self.m and 0 <= j < self.n
    # DFS is used to find and mark every cell belonging to the first island
    def dfs(self, grid: list[list[int]], i: int, j: int, visitedcell: set[tuple[int, int]]) -> None:
        # stop DFS if: cell is outside the grid & cell is water & cell has already been visited
        if (not self.isSafe(i, j) or grid[i][j] == 0 or (i, j) in visitedcell):
            return
        # mark the current land cell as part of the first island
        visitedcell.add((i, j))
        # explore all four neighboring cells
        for di, dj in self.directions:
            new_i = i + di
            new_j = j + dj
            # continue DFS from the neighboring cell
            self.dfs(grid, new_i, new_j, visitedcell)
    # BFS is used to expand outward from the first island until the second island is reached
    def bfs(self,grid: list[list[int]], visitedcell: set[tuple[int, int]]
    ) -> int:
        # queue stores cells that can currently reach from the first island
        queue = deque()
        # add every cell of the first island to the BFS queue
        for cell in visitedcell:
            queue.append(cell)
        # number of layers of water crossed
        level = 0
        # perform multi-source BFS
        while queue:
            # number of cells in the current BFS layer
            level_size = len(queue)
            # process every cell in this layer
            for _ in range(level_size):
                i, j = queue.popleft()
                # explore all four directions
                for di, dj in self.directions:
                    new_i = i + di
                    new_j = j + dj
                    # ignore cells outside the grid
                    if not self.isSafe(new_i, new_j):
                        continue
                    # ignore cells that have already been visited
                    if (new_i, new_j) in visitedcell:
                        continue
                    # if reach land have reached the second island
                    if grid[new_i][new_j] == 1:
                        return level
                    # otherwise, this is water add it to the visited set and queue
                    visitedcell.add((new_i, new_j))
                    queue.append((new_i, new_j))
            # move to the next BFS layer
            level += 1
        # return level if no bridge was found
        return level
    # find the minimum number of water cells that need to be flipped to connect the two islands
    def shortestBridge(self, grid: list[list[int]]) -> int:
        # store the number of rows and columns
        self.m = len(grid)
        self.n = len(grid[0])
        # store all cells belonging to the first island
        visitedcell = set()
        # search for the first land cell
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    # use DFS to mark the complete first island
                    self.dfs(grid, i, j, visitedcell)
                    # start BFS from all cells of the first island
                    return self.bfs(grid, visitedcell)
        # no island was found
        return -1

# Time Complexity : O(N^2)
# Space Complexity : O(N)