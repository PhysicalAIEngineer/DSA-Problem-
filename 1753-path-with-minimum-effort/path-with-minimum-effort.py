# Brute Force Code & Optimal Code
import heapq
class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        # number of rows
        m = len(heights)
        # number of column
        n = len(heights[0])
        # 4 possible direction up, down, right, left
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        # resultx[x][y] stores the minimum effort required to reach cell (x, y)
        result = [[float("inf")] * n for _ in range(m)]
        # min heap stores : (minimum effort, [row, columns])
        min_heap = []
        # start from the top left cell initial effort is 0
        heapq.heappush(min_heap, (0, (0, 0)))
        result[0][0] = 0
        # dijkstra algoritms
        while min_heap:
            # cell with minimum efforts
            diffrence, node = heapq.heappop(min_heap)
            x, y = node
            # if reached the destination this is the minimum possible effort because min heap gives the smallest effort first
            if x == m - 1 and y == n - 1:
                return diffrence
            # check all 4 neighbouring cells
            for direction in directions:
                # calculate neighbours coorinates
                x_ = x + direction[0]
                y_ = y + direction[1]
                # check if neighbours is inside the grid
                x_ = x + direction[0]
                y_ = y + direction[1]
                # check if neighbours is inside the grid
                if 0 <= x_ < m and 0 <= y_ < n:
                    # calculate efforts of moving from current cell to neighbour
                    currentdiffrence = abs(heights[x][y] - heights[x_][y_])
                    # path effort is the maximum height diffrence encounterd on the path
                    newdiffrence = max(diffrence, currentdiffrence)
                    # if this path gives smaller effort update the result
                    if result[x_][y_] > newdiffrence:
                        # store the minimum effort for this cell
                        result[x_][y_] = newdiffrence
                        # push updated effort into min heap
                        heapq.heappush(min_heap, (result[x_][y_], (x_, y_)))
        # return minimum effort to reach destination
        return result[m - 1][n - 1]

# Time Complexity : O(N)
# Space Complexity : O(N)