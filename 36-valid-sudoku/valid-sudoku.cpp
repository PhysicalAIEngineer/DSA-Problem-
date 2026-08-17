// Brute Force Code & Optimal Code
class Solution {
public:
    // check whether the given Sudoku board is valid
    bool isValidSudoku(vector<vector<char>>& board) {
        // check every row
        for (int row = 0; row < 9; row++) {
            // store the digits already seen in this row
            vector<char> seen;
            for (int col = 0; col < 9; col++) {
                // ignore empty cells
                if (board[row][col] == '.') {
                    continue;
                }
                // check whether the current digit already exists
                bool duplicate = false;
                for (char value : seen) {
                    if (value == board[row][col]) {
                        duplicate = true;
                        break;
                    }
                }
                // duplicate digit found
                if (duplicate) {
                    return false;
                }
                // store the current digit
                seen.push_back(board[row][col]);
            }
        }
        // check every column
        for (int col = 0; col < 9; col++) {
            // store the digits already seen in this column
            vector<char> seen;
            for (int row = 0; row < 9; row++) {
                // ignore empty cells
                if (board[row][col] == '.') {
                    continue;
                }
                // check whether the current digit already exists
                bool duplicate = false;
                for (char value : seen) {
                    if (value == board[row][col]) {
                        duplicate = true;
                        break;
                    }
                }
                // duplicate digit found
                if (duplicate) {
                    return false;
                }
                // store the current digit
                seen.push_back(board[row][col]);
            }
        }
        // check every 3 x 3 sub-box
        for (int start_row = 0; start_row < 9; start_row += 3) {
            for (int start_col = 0; start_col < 9; start_col += 3) {
                // store the digits already seen in this box
                vector<char> seen;
                // traverse the current 3 x 3 sub-box
                for (int row = start_row; row < start_row + 3;row++) {
                    for (int col = start_col; col < start_col + 3; col++) {
                        // ignore empty cells
                        if (board[row][col] == '.') {
                            continue;
                        }
                        // check whether the current digit already exists
                        bool duplicate = false;
                        for (char value : seen) {
                            if (value == board[row][col]) {
                                duplicate = true;
                                break;
                            }
                        }
                        // duplicate digit found
                        if (duplicate) {
                            return false;
                        }
                        // store the current digit
                        seen.push_back(board[row][col]);
                    }
                }
            }
        }
        // no duplicates found in any row column, or 3 x 3 sub-box
        return true;
    }
};

// Time Complexity : O(N^6)
// Space Complexity : O(N)