# Brute Force Code & Optimal Code
class Solution:
    def __init__ (self):
        # store the number of rows in the grid
        self.m = 0
        # storet the number of column in the grid
        self.n = 0
        # possible row movements when moving to the next column
        # 1. -1 --> move diagonally upward
        # 2. 1 --> move diagonally downward
        # 3. 0 --> move straight to the right 
        # column always increases by 1 
        self.directions = [-1, 0, 1]
    def DFS(self, row, col, grid, t):
        # check whether have alreay calcualted the answer for this cell it t[row][col] is not -1 return the stored result instend of calculating it again
        if t[row][col] != -1:
            return t[row][col]
        # storet the maximum number of moves that can be made starting from the current cell intially assume that cannot move anywhere
        moves = 0
        # try all three posssible row movements
        # 1. diagonally up
        # 2. straight right
        # 3. diagonally down
        for direction in self.directions:
            # calculate the row of the next cell
            newrow = row + direction
            # only move one column to the right
            newcol = col + 1
            # check whether the next cell is valid
            # condition 1 : row cannot go above the grid
            # condition 2 : row cannot go below the grid
            # condition 3 : newcol >= 0 column must be valid
            # condition 4 : newcol < self.n cannot move outside the grid
            # condition 5 : grid[newrow][newcol] > grid[row][col] -> next cell must contain a strictly greater value than the current cell
            if (newrow >= 0 and newrow < self.m and newcol >= 0
            and newcol < self.n and grid[newrow][newcol] > grid[row][col]):
                # move to the next valid cell so check  1 represents  the move from the current cell to the next cell DFS() gives the maximum number of additional moves possible from there therefore total moves = 1 + moves possible from next cell
                moves = max(moves, 1 + self.DFS(newrow, newcol, grid, t))
        # store the calculated answer for the current cell this memorization step
        t[row][col] = moves
        # return the maximum number of moves possible starting from this cell
        return moves
    def maxMoves(self, grid: list[list[int]]):
        # number of rows in the grid
        self.m = len(grid)
        # number of column in the grid
        self.n = len(grid[0])
        # store the maximum number of moves found among all possible starting cells
        result = 0
        # create the memoization table t[row][col] represents : maximum number fo moves that can be made starting from grid[row][col] so -1 means this cell has not been calculated yet
        t = [[-1] * self.n for _ in range(self.m)]
        # allowed to start from any row in the first column therefore try DFS from every cell in column 0
        for row in range(self.m):
            # calculate the maximum moves starting from the current row in column 0 keep the maximum result found
            result = max(result, self.DFS(row, 0, grid, t))
        # return the maximum number of valid moves 
        return result 

# Time Complexity : O(N)
# Space Complexity : O(N) 
                