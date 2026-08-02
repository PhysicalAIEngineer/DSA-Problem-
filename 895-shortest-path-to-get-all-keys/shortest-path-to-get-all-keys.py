# Brute Force Code & Optimal Code
from collections import deque
class Solution:
    # find the minimum number of steps needed to collect all keys
    def shortestPathAllKeys(self, grid: list[str]):
        # number of rows and columns
        m = len(grid)
        n = len(grid[0])
        # four possible movement directions: down, up, right, left
        directions = [
            (1, 0), # down
            (-1, 0), # up
            (0, 1), # right
            (0, -1) # left
        ]
        # BFS queue stores:
        # row          -> current row
        # col          -> current column
        # steps        -> number of moves taken
        # key_status   -> keys currently collected
        queue = deque()
        # count the total number of keys
        key_count = 0
        # find the starting position and count all available keys
        for i in range(m):
            for j in range(n):
                # '@' represents the starting position
                if grid[i][j] == '@':
                    queue.append((i, j, 0, 0))
                # keys are represented by lowercase letters a-f
                elif 'a' <= grid[i][j] <= 'f':
                    key_count += 1
        # create the bitmask representing the state where we have collected every key.
        # Example:
        # 3 keys -> 111 -> 7
        # 4 keys -> 1111 -> 15
        # (1 << key_count) - 1
        # creates all 1s for the available keys
        final_key_status = (1 << key_count) - 1
        # visited[row][col][key_status]
        # state depends on both:
        # 1. our current position
        # 2. which keys currently have
        # reaching the same cell with different keys represents different states.
        visited = [[[False] * (final_key_status + 1) for _ in range(n)] for _ in range(m)]
        # starting position from the queue
        start_i, start_j, _, _ = queue[0]
        # mark the starting state as visited initially,have no keys
        visited[start_i][start_j][0] = True
        # start Breadth-First Search
        while queue:
            # get the current BFS state
            row, col, steps, key_status = queue.popleft()
            # If have collected all keys this is the shortest path because BFS processes states level by level
            if key_status == final_key_status:
                return steps
            # try moving in all four directions
            for dr, dc in directions:
                # calculate the new position
                new_row = row + dr
                new_col = col + dc
                # ignore positions outside the grid
                if (new_row < 0 or new_row >= m or new_col < 0 or new_col >= n
                ):
                    continue
                # walls cannot be crossed
                if grid[new_row][new_col] == '#':
                    continue
                # character at the new position
                ch = grid[new_row][new_col]
                # case 1: reached a lock
                if 'A' <= ch <= 'F':
                    # convert the lock character into its corresponding key index
                    # A -> 0
                    # B -> 1
                    # C -> 2
                    key_index = ord(ch) - ord('A')
                    # check whether we already have the key required to open this lock shift the key bit to the right and check whether it is 1
                    have_key = (key_status >> key_index) & 1
                    # only pass through the lock if  have its corresponding key
                    if have_key == 1:
                        # check whether this state has already been visited
                        if not visited[new_row][new_col][key_status]:
                            # mark this state as visited
                            visited[new_row][new_col][key_status] = True
                            # add the new state to the queue
                            queue.append((new_row, new_col, steps + 1,key_status))
                # case 2: reached a key
                elif 'a' <= ch <= 'f':
                    # convert the key character into a bit position
                    # a -> 0
                    # b -> 1
                    # c -> 2
                    key_index = ord(ch) - ord('a')
                    # add the new key to our bitmask
                    # example:
                    # key_status = 001
                    # new key    = 010
                    # result     = 011
                    new_key_status = (key_status | (1 << key_index))
                    # check whether this position with this collection of keys has already been visited
                    if not visited[new_row][new_col][new_key_status]:
                        # mark the new state as visited
                        visited[new_row][new_col][new_key_status] = True
                        # add the state to the BFS queue
                        queue.append((new_row, new_col, steps + 1,new_key_status))
                # case 3: empty cell
                else:
                    # move normally without changing the current key collection
                    if not visited[new_row][new_col][key_status]:
                        # mark the state as visited
                        visited[new_row][new_col][key_status] = True
                        # add the new state to the queue
                        queue.append((new_row, new_col, steps + 1, key_status))
        # BFS finished without collecting all the required keys
        return -1

# Time Complexity : O(N)
# Space Complexity : O(N) 