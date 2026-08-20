# Brute Force Code & Optimal Code
class Solution:
    def __init__ (self):
        # store the length of the word
        self.l = 0
        # store the number of rows in the board
        self.m = 0
        # store the number of column in the board
        self.n = 0
        # four possible direction from cell
        self.directions = [
            [0, 1], # move right
            [0, -1], # move left
            [1, 0], # move down
            [-1, 0], # move up
        ]
    def find(self, board, i, j, word, idx):
        # base case : if idx reaches the length of the word it means that every characters of the word has been successfully matched therefore word exists in the board
        if idx >= self.l:
            return True
        # check whether the current cell is valid 
        # return false if:
        # 1. row index is outside the board
        # 2. column index is outside the board
        # 3. current cell does not contain the required characters
        # if any these condition is true this path cannot from the word
        if (i <0 or i >= self.m or j < 0 or j >= self.n or board[i][j] != word[idx]):
            return False
        # save the current characters
        temp = board[i][j]
        # mark the current cell as visited "$" is used as tempoary markers
        board[i][j] = "$"
        # try all four directions
        for direction in self.directions:
            # calculate the coorinates of the next cell
            # direction[0] --> row movement
            # direction[1] --> column movement
            new_i = i + direction[0]
            new_j = j + direction[1]
            # recursively search for the next characters of the word from the neighboring cell idx + 1 means that the current characters has already been matched so need to match the next characters
            if self.find(board, new_i, new_j, word, idx + 1):
                # complete path has been found
                return True
        # backtracking of the four direction produced a valid path so restore the original characters so that this cell can be used by another possible path
        board[i][j] = temp
        # no valid path was found from this cell
        return False 
    def exist(self, board: List[List[str]], word: str) -> bool:
        # number of rows in the board
        self.m = len(board)
        # number of column in the board
        self.n = len(board[0])
        # store the length of the words
        self.l = len(word)
        # impossible check word cannot exists if it contain more characters than the total number of cells for each cell can be used at most once in path
        if self.m * self.n < self.l:
            return False
        # try every cell in starting points
        for i in range(self.m):
            for j in range(self.n):
                # current cell must contain the first characters of the word if it does start DFS from this cell
                if (board[i][j] == word[0] and self.find(board, i, j, word, 0)):
                    # complete path was found 
                    return True
        # none of the cells could from the word
        return False

# Time Complexity : O(N)
# Space Complexity : O(N)
        