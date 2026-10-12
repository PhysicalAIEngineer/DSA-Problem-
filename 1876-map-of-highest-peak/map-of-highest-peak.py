# Brute Force Code & Optimal Code
from collections import deque
class Solution:
    def highestPeak(self, isWater):
        # get the number of rows and columns
        m = len(isWater)
        n = len(isWater[0])
        # define the four possible movement directions
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        # initialize all cell heights as -1 (unvisited)
        height = [[-1] * n for _ in range(m)]
        # create a queue for BFS
        queue = deque()
        # water cells have height 0 add all water cells to the queue as BFS starting points
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    height[i][j] = 0
                    queue.append((i, j))
        # apply Multi-Source BFS to calculate the heights
        while queue:
            # get the number of cells at the current BFS level
            N = len(queue)
            while N:
                # remove the front cell from the queue
                i, j = queue.popleft()
                # Visit all four neighboring cells
                for dir in directions:
                    i_ = i + dir[0]
                    j_ = j + dir[1]
                    # check whether the neighbor is inside the grid and unvisited
                    if (0 <= i_ < m and 0 <= j_ < n and height[i_][j_] == -1):
                        # set the neighbor's height one greater than the current cell
                        height[i_][j_] = height[i][j] + 1
                        # add the neighbor to the queue for further exploration
                        queue.append((i_, j_))
                # move to the next cell in the current BFS level
                N -= 1
        # return the matrix containing the highest possible heights
        return height

# Time Complexity : O(N)
# Space Complexity : O(N)