// Brute Force Code & Optimal Code
class Solution {
public:
    // store the number of rows in the grid
    int m;
    // store the number of column in the grid
    int n;
    // possible row movements when moving to the next column
    // 1. -1 --> move diagonally upward
    // 2. 1 --> move diagonally downward
    // 3. 0 --> move straight to the right 
    // column always increases by 1 
    vector<int> directions = {-1, 0, 1};
    int DFS(int row, int col,
            vector<vector<int>>& grid,
            vector<vector<int>>& t) {
        // check whether have alreay calcualted the answer for this cell it t[row][col] is not -1 return the stored result instend of calculating it again
        if (t[row][col] != -1) {
            return t[row][col];
        }
        // store the maximum number of moves that can be made starting from the current cell intially assume that cannot move anywhere
        int moves = 0;
        // try all three posssible row movements
        // 1. diagonally up
        // 2. straight right
        // 3. diagonally down
        for (int& dir : directions) {
            // calculate the row of the next cell
            int newrow = row + dir;
            // only move one column to the right
            int newcol = col + 1;
            // check whether the next cell is valid
            // condition 1 : row cannot go above the grid
            // condition 2 : row cannot go below the grid
            // condition 3 : newcol >= 0 column must be valid
            // condition 4 : newcol < self.n cannot move outside the grid
            // condition 5 : grid[newrow][newcol] > grid[row][col] -> next cell must contain a strictly greater value than the current cell
            if (newrow >= 0 && newrow < m && newcol >= 0 && newcol < n && grid[newrow][newcol] > grid[row][col]) {
                // move to the next valid cell so check  1 represents  the move from the current cell to the next cell DFS() gives the maximum number of additional moves possible from there therefore total moves = 1 + moves possible from next cell
                moves = max(moves, 1 + DFS(newrow, newcol, grid, t));
            }
        }
        // store the calculated answer for the current cell this memorization step
        return t[row][col] = moves;
    }
    int maxMoves(vector<vector<int>>& grid) {
        // number of rows in the grid
        m = grid.size();
        // number of column in the grid
        n = grid[0].size();
        // store the maximum number of moves found among all possible starting cells
        int result = 0;
        // create the memoization table t[row][col] represents : maximum number fo moves that can be made starting from grid[row][col] so -1 means this cell has not been calculated yet
        vector<vector<int>> t(m, vector<int>(n, -1));
        // allowed to start from any row in the first column therefore try DFS from every cell in column 0
        for (int row = 0; row < m; row++) {
            // calculate the maximum moves starting from the current row in column 0 keep the maximum result found
            result = max(result, DFS(row, 0, grid, t));
        }
        // return the maximum number of valid moves
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)