// Brute Force Code & Optimal Code
class Solution {
public:
    bool findSafeWalk(vector<vector<int>>& grid, int health) {
        // define the four possible movement directions
        vector<pair<int, int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        // get the number of rows and columns
        int m = grid.size();
        int n = grid[0].size();
        // store the minimum health cost required to reach each cell initialize all cells with infinity
        vector<vector<int>> result(m, vector<int>(n, INT_MAX));
        // create a deque for 0-1 BFS
        deque<pair<int, int>> dq;
        // set the starting cell's health cost
        result[0][0] = grid[0][0];
        dq.push_front({0, 0});
        // process cells until the deque becomes empty
        while (!dq.empty()) {
            // remove the front cell from the deque
            auto [r, c] = dq.front();
            dq.pop_front();
            // explore all four neighboring cells
            for (auto direction : directions) {
                int nr = r + direction.first;
                int nc = c + direction.second;
                // skip the neighbor if it is outside the grid
                if (nr < 0 || nr >= m || nc < 0 || nc >= n) {
                    continue;
                }
                // check whether moving to this neighbor gives a lower health cost
                if (result[r][c] + grid[nr][nc] < result[nr][nc]) {
                    // update the minimum health cost for the neighbor
                    result[nr][nc] = result[r][c] + grid[nr][nc];
                    // if the neighbor has cost 0, add it to the front
                    if (grid[nr][nc] == 0) {
                        dq.push_front({nr, nc});
                    }
                    else {
                        // if the neighbor has cost 1, add it to the back
                        dq.push_back({nr, nc});
                    }
                }
            }
        }
        // return true if at least 1 health remains after reaching the destination
        return health - result[m - 1][n - 1] >= 1;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)