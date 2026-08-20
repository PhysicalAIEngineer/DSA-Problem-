// Brute Force Code & Optimal Code
class Solution {
public:
    // store the length of the word
    int l;
    // store the number of rows in the board
    int m;
    // store the number of columns in the board
    int n;
    // Four possible directions from a cell
    vector<vector<int>> directions = {
        {0, 1},   // move right
        {0, -1},  // move left
        {1, 0},   // move down
        {-1, 0}   // move up
    };
    bool find(vector<vector<char>>& board, int i, int j, string& word, int idx) {
        // base case: if idx reaches the length of the word it means every character of the word has been successfully matched.
        if (idx >= l) {
            return true;
        }
        // check whether the current cell is valid.
        // return false if:
        // 1. row index is outside the board.
        // 2. column index is outside the board.
        // 3. current cell does not contain the required character.
        // if any condition is true this path cannot form the word.
        if (i < 0 || i >= m || j < 0 || j >= n || board[i][j] != word[idx]) {
            return false;
        }
        // save the current character
        char temp = board[i][j];
        // mark the current cell as visited '$' is used as a temporary marker.
        board[i][j] = '$';
        // try all four directions
        for (auto& direction : directions) {
            // calculate the coordinates of the next cell.
            // direction[0] -> row movement
            // direction[1] -> column movement
            int new_i = i + direction[0];
            int new_j = j + direction[1];
            // recursively search for the next character from the neighboring cell idx + 1 means the current character has already been matched.
            if (find(board, new_i, new_j, word, idx + 1)) {
                // complete path has been found
                return true;
            }
        }
        // backtracking: none of the four directions produced a valid path, so restore the original character.
        board[i][j] = temp;
        // no valid path was found from this cell
        return false;
    }
    bool exist(vector<vector<char>>& board, string word) {
        // number of rows in the board
        m = board.size();
        // number of columns in the board
        n = board[0].size();
        // store the length of the word
        l = word.length();
        // impossible check: word cannot exist if it contains more characters than the total number of cells each cell can be used at most once in a path.
        if (m * n < l) {
            return false;
        }
        // try every cell as a starting point
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                // current cell must contain the first character of the word if it does, start DFS from this cell.
                if (board[i][j] == word[0] && find(board, i, j, word, 0)
                ) {
                    // complete path was found
                    return true;
                }
            }
        }
        // none of the cells could form the word
        return false;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)