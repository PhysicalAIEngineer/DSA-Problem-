# Brute Force Code & Optimal Code
from collections import deque 
class Solution: 
    def shortestPathBinaryMatrix(self, grid): 
        # number of rows
        m = len(grid) 
        # number of columns
        n = len(grid[0]) 
        # if grid is empty or starting cell is blocked there is no possible path
        if m == 0 or n == 0 or grid[0][0] != 0: 
            return -1 
        # 8 possible direction : up, down, left, right, up left, up right, down left, down right
        directions = [(1, 1), (0, 1), (1, 0), (0, -1),(-1, 0), (-1, -1), (1, -1), (-1, 1)] 
        # result[x][y] stores the shortest distance from (0,0) to cell (x,y)
        result = [[float('inf')] * n for _ in range(m)] 
        # queue stores: (distance, (row, column))
        queue_stores = deque() 
        # start from the top-left cell distance is 0 initially
        queue_stores.append((0, (0, 0))) 
        result[0][0] = 0 
        # BFS
        while queue_stores: 
            # get the current cell and its distance
            distance, node = queue_stores.popleft() 
            x, y = node 
            # check all 8 possible directions
            for direction in directions: 
                x_ = x + direction[0] 
                y_ = y + direction[1] 
                # moving to any neighbouring cell costs 1
                moving_neighbouring = 1 
                # check: cell is inside the grid & cell is open (0) & found a shorter distance
                if (0 <= x_ < m and 0 <= y_ < n and grid[x_][y_] == 0 and  distance + moving_neighbouring < result[x_][y_]): 
                    # Add the new cell to the queue
                    queue_stores.append((distance + moving_neighbouring, (x_, y_)))  
                    # Mark the cell as visited
                    grid[x_][y_] = 1 
                    # store the shortest distance
                    result[x_][y_] = distance + moving_neighbouring 
        # if destination is still unreachable
        if result[m - 1][n - 1] == float('inf'): 
            return -1 
        # result stores number of moves/edges add 1 because answer counts cells
        return result[m - 1][n - 1] + 1

# Time Complexity : O(N)
# Space Complexity : O(N)