# Brute Force Code & Optimal Code
from collections import deque
class Solution:
    # return the distance of every cell from its nearest 0
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        # number of rows and columns
        m = len(mat)
        n = len(mat[0])
        # four possible movement directions
        directions = [
            (0, 1),    # right
            (0, -1),   # left
            (-1, 0),   # up
            (1, 0)     # down
        ]
        # queue used for BFS
        queue = deque()
        # distance matrix -1 means that the cell has not been visited yet.
        dist = [[-1] * n for _ in range(m)]
        # step 1: add all 0 cells to the queue
        # every 0 is a starting point because its distance to the nearest 0 is already 0 starting BFS from multiple 0s at the same time is called multi-source BFS.
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    # distance from a 0 to itself is 0
                    dist[i][j] = 0
                    # add this zero to the BFS queue
                    queue.append((i, j))
        # Step 2: perform multi-source BFS
        while queue:
            # remove the next cell from the queue
            row, col = queue.popleft()
            # explore all four neighboring cells
            for dr, dc in directions:
                # calculate the neighbor's position
                new_row = row + dr
                new_col = col + dc
                # make sure the neighbor is inside the boundaries of the matrix
                if (0 <= new_row < m and 0 <= new_col < n):
                    # if this cell has not been visited yet
                    if dist[new_row][new_col] == -1:
                        # its distance is one more than the distance of the current cell
                        dist[new_row][new_col] = (dist[row][col] + 1)
                        # add the newly visited cell to the BFS queue
                        queue.append((new_row, new_col))
        # distance matrix now contains the shortest distance from every cell to its nearest 0.
        return dist

# Time Complexity : O(N)
# Space Complexity : O(N)