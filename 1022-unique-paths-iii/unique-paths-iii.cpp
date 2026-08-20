// Brute Force Code & Optimal Code
class Solution {
public:
    // store the number of rows in the grid
    int m = 0;
    // store the number of columns in the grid
    int n = 0;
    // store the total number of non-obstacle cells that must be visited.
    int emptyCells = 0;
    // store the total number of valid paths
    int result = 0;
    // four possible movements from the current cell
    vector<vector<int>> directions{
        {1, 0},   // move down
        {-1, 0},  // move up
        {0, 1},   // move right
        {0, -1}   // move left
    };
    // DFS function to explore all possible paths
    void dfs(vector<vector<int>>& grid, int curr_count, int i, int j) {
        // check whether the current cell is valid stop the current path if:
        // 1. row is outside the grid
        // 2. column is outside the grid
        // 3. cell is an obstacle
        // 4. cell was already visited
        // use -1 to represent both obstacles and temporarily visited cells.
        if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] == -1) {
            return;
        }
        // check whether we reached the ending cell once we reach the ending square cannot continue walking path is valid only if every required non-obstacle cell has been visited exactly once.
        if (grid[i][j] == 2) {
            // if curr_count equals emptyCells all required cells have been visited.
            if (curr_count == emptyCells) {
                // found one valid path
                result++;
            }
            // whether valid or invalid, stop this path because the ending cell has been reached.
            return;
        }
        // mark the current cell as visited set it to -1 so that do not visit the same cell again during this path.
        grid[i][j] = -1;
        // try all four possible directions
        for (vector<int>& direction : directions) {
            // calculate the coordinates of the next cell
            int new_i = i + direction[0];
            int new_j = j + direction[1];
            // recursively explore the next cell so, curr_count + 1 means that the current cell has now been visited.
            dfs(grid, curr_count + 1, new_i, new_j);
        }
        // backtracking restore the current cell after exploring all possible paths from it this allows the cell to be used again when exploring a different path.
        grid[i][j] = 0;
    }
    // return the number of unique paths that visit every non-obstacle cell exactly once.
    int uniquePathsIII(vector<vector<int>>& grid) {
        // number of rows
        m = grid.size();
        // number of columns
        n = grid[0].size();
        // reset the number of required cells and the number of valid paths.
        emptyCells = 0;
        result = 0;
        // variables to store the starting cell
        int start_x = 0;
        int start_y = 0;
        // find the starting cell and count all empty cells.
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                // if the cell is 0, it is an empty cell that must be visited.
                if (grid[i][j] == 0) {
                    emptyCells++;
                }
                // if the cell is 1, store its coordinates because DFS must start from here.
                if (grid[i][j] == 1) {
                    start_x = i;
                    start_y = j;
                }
            }
        }
        // include the starting cell in the number of cells that must be visited need to visit every non-obstacle cell exactly once before reaching the ending cell.
        emptyCells++;
        // start DFS curr_count = 0 because no cell has been counted as visited before DFS starts.
        int curr_count = 0;
        // start exploring from the starting cell
        dfs(grid, curr_count, start_x, start_y);
        // return the total number of valid paths
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)