// Brute Force Code & Optimal Code
class Solution {
public:
    bool backtrack(int idx, vector<pair<int, int>>& empty_cells,vector<vector<char>>& board, vector<unordered_set<char>>& rows,vector<unordered_set<char>>& cols, vector<unordered_set<char>>& boxes) {
        // base case: all empty cells filled successfully
        if (idx == empty_cells.size()) {
            return true;
        }
        int r = empty_cells[idx].first;
        int c = empty_cells[idx].second;
        // find the 3 x 3 box index
        int box_idx = (r / 3) * 3 + (c / 3);
        // iterate through all 9 possible digits
        for (char d = '1'; d <= '9'; d++) {
            // check whether digit can be placed
            if (rows[r].find(d) == rows[r].end() && cols[c].find(d) == cols[c].end() && boxes[box_idx].find(d) == boxes[box_idx].end()) {
                // place digit
                board[r][c] = d;
                rows[r].insert(d);
                cols[c].insert(d);
                boxes[box_idx].insert(d);
                // move directly to the next empty cell
                if (backtrack(idx + 1, empty_cells, board, rows, cols, boxes)) {
                    return true;
                }
                // backtrack & undo choices
                board[r][c] = '.';
                rows[r].erase(d);
                cols[c].erase(d);
                boxes[box_idx].erase(d);
            }
        }
        return false;
    }
    void solveSudoku(vector<vector<char>>& board) {
        // track filled numbers in each row column and 3 x 3 box
        vector<unordered_set<char>> rows(9);
        vector<unordered_set<char>> cols(9);
        vector<unordered_set<char>> boxes(9);
        // store coordinates of all empty cells
        vector<pair<int, int>> empty_cells;
        // pre-populate the sets and collect all empty cell coordinates
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                char val = board[r][c];
                if (val != '.') {
                    rows[r].insert(val);
                    cols[c].insert(val);
                    int box_idx = (r / 3) * 3 + (c / 3);
                    boxes[box_idx].insert(val);
                } else {
                    empty_cells.push_back({r, c});
                }
            }
        }
        // backtracking over pre-collected empty cells
        backtrack(0, empty_cells, board, rows, cols, boxes);
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)