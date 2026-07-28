# Brute Force & Optimal Code
from collections import deque
class Solution:
    # convert a square number into its corresponding (row, column) coordinates on the board
    def getCoord(self, square: int) -> tuple[int, int]:
        # compute the row index counting from the bottom
        row = self.n - 1 - (square - 1) // self.n
        # compute the column assuming left-to-right numbering
        col = (square - 1) % self.n
        # reverse the column for rows that are numbered from right to left
        if (self.n % 2 == 1 and row % 2 == 1) or (self.n % 2 == 0 and row % 2 == 0):
            col = self.n - 1 - col
        # return the board coordinates
        return row, col
    # return the minimum number of dice throws needed to reach the last square
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        # size of the board
        self.n = len(board)
        # number of dice throws taken
        steps = 0
        # queue for BFS
        queue = deque()
        # track visited board cells
        visited = [[False] * self.n for _ in range(self.n)]
        # mark the starting square (square 1) as visited
        visited[self.n - 1][0] = True
        # start BFS from square 1
        queue.append(1)
        # perform BFS
        while queue:
            # number of nodes at the current BFS level
            level_size = len(queue)
            # process all squares reachable in the current number of dice throws
            for _ in range(level_size):
                # get the current square
                current = queue.popleft()
                # if the final square is reached, return the number of moves
                if current == self.n * self.n:
                    return steps
                # try every possible dice roll (1 to 6)
                for dice in range(1, 7):
                    # ignore moves that go beyond the board
                    if current + dice > self.n * self.n:
                        break
                    # convert the square number into board coordinates
                    row, col = self.getCoord(current + dice)
                    # skip if this board cell has already been visited
                    if visited[row][col]:
                        continue
                    # mark the cell as visited
                    visited[row][col] = True
                    # normal square move to the next square
                    if board[row][col] == -1:
                        queue.append(current + dice)
                    # snake or ladder move to its destination
                    else:
                        queue.append(board[row][col])
            # one complete dice throw (one BFS level) finished
            steps += 1
        # last square cannot be reached
        return -1

# Time Complexity : O(N^2)
# Space Complexity : O(N^2)
