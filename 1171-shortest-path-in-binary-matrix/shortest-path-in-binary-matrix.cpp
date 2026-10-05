// Brute Force Code & Optimal Code
class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        // number of rows
        int m = grid.size();
        // number of columns
        int n = grid[0].size();
        // if grid is empty or starting cell is blocked there is no possible path
        if (m == 0 || n == 0 || grid[0][0] != 0) {
            return -1;
        }
        // 8 possible directions: up, down, left, right, up-left, up-right, down-left, down-right
        vector<pair<int, int>> directions = {{1, 1}, {0, 1},{1, 0}, {0, -1}, {-1, 0}, {-1, -1}, {1, -1}, {-1, 1}
        };
        // result[x][y] stores the shortest distance from (0,0) to cell (x,y)
        vector<vector<int>> result(m, vector<int>(n, INT_MAX));
        // queue stores: (distance, (row, column))
        queue<pair<int, pair<int, int>>> queue_stores;
        // start from the top-left cell distance is 0 initially
        queue_stores.push({0, {0, 0}});
        result[0][0] = 0;
        // BFS
        while (!queue_stores.empty()) {
            // get the current cell and its distance
            auto current = queue_stores.front();
            queue_stores.pop();
            int distance = current.first;
            int x = current.second.first;
            int y = current.second.second;
            // check all 8 possible directions
            for (auto direction : directions) {
                int x_ = x + direction.first;
                int y_ = y + direction.second;
                // moving to any neighbouring cell costs 1
                int moving_neighbouring = 1;
                // check cell is inside the grid cell is open (0) found a shorter distance
                if (x_ >= 0 && x_ < m && y_ >= 0 && y_ < n && grid[x_][y_] == 0 && distance + moving_neighbouring < result[x_][y_]) {
                    // add the new cell to the queue
                    queue_stores.push({distance + moving_neighbouring, {x_, y_}});
                    // mark the cell as visited
                    grid[x_][y_] = 1;
                    // store the shortest distance
                    result[x_][y_] = distance + moving_neighbouring;
                }
            }
        }
        // if destination is still unreachable
        if (result[m - 1][n - 1] == INT_MAX) {
            return -1;
        }
        // result stores number of moves/edges add 1 because answer counts cells
        return result[m - 1][n - 1] + 1;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)