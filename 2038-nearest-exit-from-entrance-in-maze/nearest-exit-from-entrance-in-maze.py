# Brute Force Code & Optimal Code
from collections import deque
class Solution:
    def nearestExit(self, maze, entrance):
        # four possible movement directions : right, left, up, down
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # get the number of rows and columns
        m = len(maze)
        n = len(maze[0])
        # create a queue for BFS
        queue = deque()
        # add the entrance cell to the queue
        queue.append((entrance[0], entrance[1]))
        # mark the entrance as visited to avoid revisiting it
        maze[entrance[0]][entrance[1]] = '+'
        # count the number of steps from the entrance
        steps = 0
        # perform BFS until the queue becomes empty
        while queue:
            # number of cells at the current BFS level
            size = len(queue)
            while size:
                # remove the front cell from the queue
                temp = queue.popleft()
                r, c = temp
                # check whether the current cell is an exit the entrance itself cannot be considered an exit
                if (temp != (entrance[0], entrance[1]) and
                    (r == 0 or r == m - 1 or c == 0 or c == n - 1)):
                    return steps
                # explore all four neighboring cells
                for direction in directions:
                    i = r + direction[0]
                    j = c + direction[1]
                    # check whether the neighbor is inside the maze and has not been visited or blocked
                    if (0 <= i < m and 0 <= j < n and maze[i][j] != '+'):
                        # add the accessible neighbor to the queue
                        queue.append((i, j))
                        # mark the neighbor as visited
                        maze[i][j] = '+'
                # process the next cell at the current BFS level
                size -= 1
            # increase the distance after processing one BFS level
            steps += 1
        # return -1 if no exit can be reached
        return -1

# Time Complexity : O(N)
# Space Complexity : O(N)