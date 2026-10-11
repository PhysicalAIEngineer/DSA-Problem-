# Brute Force Code & Optimal Code
from collections import deque 
class Solution: 
    def orangesRotting(self, grid): 
        # number of rows and columns
        rows = len(grid) 
        columns = len(grid[0]) 
        # queue stores all rotten oranges
        queue = deque()
        # count total fresh oranges
        freshcount = 0 
        # store all rotten oranges and count fresh oranges
        for i in range(rows): 
            for j in range(columns):
                # add rotten orange to the queue
                if grid[i][j] == 2: 
                    queue.append((i, j)) 
                # count fresh orange
                elif grid[i][j] == 1: 
                    freshcount += 1 
        # if there are no fresh oranges no time is required
        if freshcount == 0: 
            return 0 
        # four possible directions up, down, left, right
        directions = [ 
            (-1, 0), 
            (1, 0), 
            (0, -1), 
            (0, 1) 
        ] 
        # track number of minutes
        track_numberminutes = 0 
        # multi-Source BFS all initially rotten oranges start together
        while queue: 
            # number of oranges that are rotten at the beginning of this minute
            size = len(queue) 
            # process all oranges that rot at the same time
            while size:
                # get one rotten orange
                i, j = queue.popleft() 
                # check all four directions
                for direction in directions: 
                    # calculate neighbour coordinates
                    new_i = i + direction[0] 
                    new_j = j + direction[1] 
                    # Check position is inside the grid & orange is fresh
                    if (0 <= new_i < rows and  0 <= new_j < columns and grid[new_i][new_j] == 1): 
                        # make the fresh orange rotten
                        grid[new_i][new_j] = 2 
                        # add it to queue it will spread rot in the next minute
                        queue.append((new_i, new_j)) 
                        # one less fresh orange remains
                        freshcount -= 1 
                size -= 1 
            # one complete BFS level = one minute
            track_numberminutes += 1 
        # if all fresh oranges became rotten return the required time last track_numberminutes += 1 happens after processing the final level, so subtract 1
        return track_numberminutes - 1 if freshcount == 0 else -1

# Time Complexity : O(N)
# Space Complexity : O(N)