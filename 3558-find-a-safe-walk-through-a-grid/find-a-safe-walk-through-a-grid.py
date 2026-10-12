# Brute Force Code & Optimal Code
from collections import deque
class Solution:
    def findSafeWalk(self, grid, health):
        # define the four possible movement directions
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # get the number of rows and columns
        m = len(grid)
        n = len(grid[0])
        # store the minimum health cost required to reach each cell initialize all cells with infinity
        result = [[float('inf')] * n for _ in range(m)]
        # create a deque for 0-1 BFS
        queue = deque()
        # set the starting cell's health cost
        result[0][0] = grid[0][0]
        queue.appendleft((0, 0))
        # process cells until the deque becomes empty
        while queue:
            # remove the front cell from the deque
            r, c = queue.popleft()
            # explore all four neighboring cells
            for direction in directions:
                nr = r + direction[0]
                nc = c + direction[1]
                # skip the neighbor if it is outside the grid
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue
                # check whether moving to this neighbor gives a lower health cost
                if result[r][c] + grid[nr][nc] < result[nr][nc]:
                    # update the minimum health cost for the neighbor
                    result[nr][nc] = result[r][c] + grid[nr][nc]
                    # If the neighbor has cost 0, add it to the front
                    if grid[nr][nc] == 0:
                        queue.appendleft((nr, nc))
                    else:
                        # If the neighbor has cost 1, add it to the back
                        queue.append((nr, nc))
        # return True if at least 1 health remains after reaching the destination
        return health - result[m - 1][n - 1] >= 1

# Time Complexity : O(N)
# Space Complexity : O(N)