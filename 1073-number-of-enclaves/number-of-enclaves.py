# Brute Force & Optimal Code
class Solution:
    # return the number of land cells that cannot reach the boundary
    def numEnclaves(self, grid: list[list[int]]) -> int:
        # number of rows
        m = len(grid)
        # number of columns
        n = len(grid[0])
        # DFS function to explore one connected land component
        def dfs(row, col, visited):
            # DFS moves outside the grid,
            # this land component can reach
            # the boundary
            if (row < 0 or row >= m or col < 0 or col >= n):
                return True
            # if the current cell is water there is no land to explore
            return_value = False
            if grid[row][col] == 0:
                return return_value
            # if this cell was already visited do not process it again
            if (row, col) in visited:
                return False
            # mark the current land cell as visited
            visited.add((row, col))
            # explore all four directions
            up = dfs(row - 1, col, visited)
            down = dfs(row + 1, col,visited)
            left = dfs(row,col - 1,visited)
            right = dfs(row,col + 1,visited)
            # if any direction can reach outside the grid, this component is connected to the boundary
            return (up or down or left or right)
        # store the total number of enclosed land cells
        total_enclaves = 0
        # try every cell as a possible starting point
        for row in range(m):
            for col in range(n):
                # start DFS only from an unprocessed land cell
                if grid[row][col] == 1:
                    # create a fresh visited set for the current component
                    visited = set()
                    # check whether this land component can escape
                    can_escape = dfs(row,col,visited)
                    # if the component cannot reach the boundary all its cells are enclaves
                    if not can_escape:
                        total_enclaves += len(visited)
                    # mark every cell in this component as processed
                    for r, c in visited:
                        grid[r][c] = 0
        # return the total number of enclave cells
        return total_enclaves

# Time Complexity : O(N)
# Space Complexity : O(N)
