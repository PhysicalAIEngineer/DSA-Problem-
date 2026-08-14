// Brute Force Code & Optimal Code
class Solution {
public:
    // return all elements of the matrix in spiral order
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        // number of rows and columns
        int rows = matrix.size();
        int cols = matrix[0].size();
        // store the elements in spiral order
        vector<int> result;
        // matrix to keep track of already visited cells
        vector<vector<bool>> visited(rows, vector<bool>(cols, false));
        // directions in clockwise order: right, down, left, up
        vector<pair<int, int>> directions = {
            {0, 1},    // move right
            {1, 0},    // move down
            {0, -1},   // move left
            {-1, 0}    // move up
        };
        // current direction index
        int direction = 0;
        // start from the top-left corner
        int row = 0;
        int col = 0;
        // visit every cell exactly once
        for (int i = 0; i < rows * cols; i++) {
            // add the current element to the answer
            result.push_back(matrix[row][col]);
            // mark the current cell as visited
            visited[row][col] = true;
            // compute the next position
            int next_row = row + directions[direction].first;
            int next_col = col + directions[direction].second;
            // change direction if:
            // 1. next position is outside the matrix
            // 2. next position has already been visited
            if (next_row < 0 || next_row >= rows ||
                next_col < 0 || next_col >= cols ||
                visited[next_row][next_col]) {
                // move to the next direction
                direction = (direction + 1) % 4;
                // recompute the next position
                next_row = row + directions[direction].first;
                next_col = col + directions[direction].second;
            }
            // move to the next cell
            row = next_row;
            col = next_col;
        }
        // return the spiral traversal
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)