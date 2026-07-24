# Optimal Code
from collections import deque
class Solution:
    # find the shortest path from the top-left corner to the bottom-right corner while being allowed to remove at most k obstacles
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        # four possible movement directions: Up, Left, Down, Right
        directions = [
            (-1, 0), # up
            (0, -1), # left
            (1, 0),  # down
            (0, 1)   # right
        ]
        # number of rows and columns
        m = len(grid)
        n = len(grid[0])
        # queue for breadth first search each state stores: (row, column, remaining obstacle eliminations)
        queue = deque()
        # start BFS from the top-left corner
        queue.append((0, 0, k))
        # store visited states as (row, column, remaining eliminations)same cell can be visited again if it has a different number of remaining obstacle eliminations.
        visited = set()
        visited.add((0, 0, k))
        # number of steps taken
        steps = 0
        # perform breadth first search
        while queue:
            # number of states at the current BFS level
            size = len(queue)
            # process every state in the current level
            for _ in range(size):
                curr_i, curr_j, obs = queue.popleft()
                # destination reached
                if curr_i == m - 1 and curr_j == n - 1:
                    return steps
                # explore all four directions
                for dx, dy in directions:
                    new_i = curr_i + dx
                    new_j = curr_j + dy
                    # ignore positions outside the grid
                    if (new_i < 0 or new_i >= m or new_j < 0 or new_j >= n):
                        continue
                    # if the next cell is empty and this state has not been visited
                    if (grid[new_i][new_j] == 0 and (new_i, new_j, obs) not in visited):
                        queue.append((new_i, new_j, obs))
                        visited.add((new_i, new_j, obs))
                    # if the next cell is an obstacle, eliminate it if possible
                    elif (grid[new_i][new_j] == 1 and obs > 0 and (new_i, new_j, obs - 1) not in visited):
                        queue.append((new_i, new_j, obs - 1))
                        visited.add((new_i, new_j, obs - 1))
            # increase the distance after processing one BFS level
            steps += 1
        # destination cannot be reached
        return -1

# Time Complexity : O(N)
# Space Complexity : O(N)