// Brute Force Code & Optimal Code
class Solution {
public:
    // store the number of rows in the grid
    int m = 0;
    // store the number of columns in the grid
    int n = 0;
    // four possible directions
    vector<vector<int>> directions = {
        {-1, 0}, // move up
        {1, 0},  // move down
        {0, 1},  // move right
        {0, -1}  // move left
    };
    int DFS(vector<vector<int>>& grid, int i, int j) {
        // base case:
        // stop DFS if:
        // 1. i goes outside the grid
        // 2. j goes outside the grid
        // 3. current cell contains 0 gold
        // in all these cases, no more gold can be collected.
        if (i >= m || i < 0 || j >= n || j < 0 || grid[i][j] == 0) {
            return 0;
        }
        // store the original amount of gold present in the current cell need this value because we temporarily change the cell to 0.
        int originalGoldValue = grid[i][j];
        // mark the current cell as visited set the current cell to 0 so that the same cell cannot be visited again during this DFS path.
        grid[i][j] = 0;
        // store the maximum amount of gold that can be collected from neighboring cells.
        int maxGold = 0;
        // try all four directions
        for (auto& direction : directions) {
            // calculate the row of the next cell
            int new_i = i + direction[0];
            // calculate the column of the next cell
            int new_j = j + direction[1];
            // recursively explore the next cell take the maximum result among all four possible directions.
            maxGold = max(maxGold, DFS(grid, new_i, new_j));
        }
        // backtracking: restore the original amount of gold this is important because another DFS starting from a different cell should be able to use this cell again.
        grid[i][j] = originalGoldValue;
        // total gold collected from this path = gold in the current cell + maximum gold collected from its neighbors.
        return originalGoldValue + maxGold;
    }
    int getMaximumGold(vector<vector<int>>& grid) {
        // number of rows in the grid
        m = grid.size();
        // number of columns in the grid
        n = grid[0].size();
        // store the maximum amount of gold found among all possible paths.
        int maxGold = 0;
        // try every cell as a starting point
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                // only start from a cell that contains gold
                if (grid[i][j] != 0) {
                    // start DFS from this cell and update the maximum gold.
                    maxGold = max(maxGold, DFS(grid, i, j));
                }
            }
        }
        // return the maximum gold that can be collected
        return maxGold;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)