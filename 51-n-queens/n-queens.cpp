// Brute Force Code & Optimal Code
class Solution {
public:
    // vector to store all valid board configurations
    vector<vector<string>> result;
    // backtracking function to place queens row by row
    void solve(vector<string>& board, int row, unordered_set<int>& columns,unordered_set<int>& diagonals, unordered_set<int>& anti_diagonals) {
        // if queens have been placed in all rows store the current board configuration
        if (row == board.size()) {
            // store the current board
            result.push_back(board);
            return;
        }
        // try placing a queen in every column of the current row
        for (int col = 0; col < board.size(); col++) {
            // compute the current diagonal identifiers
            int diagonal_id = row - col;
            int antidiagonal_id = row + col;
            // skip this position if it is already under attack
            if (columns.count(col) || diagonals.count(diagonal_id) || anti_diagonals.count(antidiagonal_id)) {
                continue;
            }
            // mark the current column and diagonals as occupied
            columns.insert(col);
            diagonals.insert(diagonal_id);
            anti_diagonals.insert(antidiagonal_id);
            // place the queen
            board[row][col] = 'Q';
            // recursively place queens in the next row
            solve(board, row + 1, columns, diagonals, anti_diagonals);
            // remove the queen and free the column and diagonals
            columns.erase(col);
            diagonals.erase(diagonal_id);
            anti_diagonals.erase(antidiagonal_id);
            board[row][col] = '.';
        }
    }
    // return all valid N-Queens configurations
    vector<vector<string>> solveNQueens(int n) {
        // if board size is zero return an empty list
        if (n == 0) {
            return {};
        }
        // clear any previously stored solutions
        result.clear();
        // create an empty n x n board
        vector<string> board(n, string(n, '.'));
        // sets to keep track of occupied columns main diagonals, and anti-diagonals
        unordered_set<int> columns;
        unordered_set<int> diagonals;
        unordered_set<int> anti_diagonals;
        // start placing queens from the first row
        solve(board, 0, columns, diagonals, anti_diagonals);
        // return all valid board configurations
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)