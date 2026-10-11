// Brute Force Code & Optimal Code
class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        // number of rows and columns
        int rows = grid.size();
        int columns = grid[0].size();
        // queue stores all rotten oranges
        queue<pair<int, int>> q;
        // count total fresh oranges
        int freshcount = 0;
        // store all rotten oranges and count fresh oranges
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                // add rotten orange to the queue
                if (grid[i][j] == 2) {
                    q.push({i, j});
                }
                // count fresh orange
                else if (grid[i][j] == 1) {
                    freshcount++;
                }
            }
        }
        // if there are no fresh oranges, no time is required
        if (freshcount == 0) {
            return 0;
        }
        // four possible directions: up, down, left, right
        vector<pair<int, int>> directions = {
            {-1, 0},
            {1, 0},
            {0, -1},
            {0, 1}
        };
        // track number of minutes
        int track_numberminutes = 0;
        // multi-source BFS: all initially rotten oranges start together
        while (!q.empty()) {
            // number of oranges rotten at the beginning of this minute
            int size = q.size();
            // process all oranges that rot at the same time
            while (size--) {
                // get one rotten orange
                auto [i, j] = q.front();
                q.pop();
                // check all four directions
                for (auto direction : directions) {
                    // calculate neighbour coordinates
                    int new_i = i + direction.first;
                    int new_j = j + direction.second;
                    // check if position is inside the grid and orange is fresh
                    if (new_i >= 0 && new_i < rows && new_j >= 0 && new_j < columns && grid[new_i][new_j] == 1) {
                        // make the fresh orange rotten
                        grid[new_i][new_j] = 2;
                        // add it to the queue to spread rot in the next minute
                        q.push({new_i, new_j});
                        // one less fresh orange remains
                        freshcount--;
                    }
                }
            }
            // one complete BFS level = one minute
            track_numberminutes++;
        }
        // return required time if all fresh oranges became rotten subtract 1 because the final BFS level adds one extra minute
        return (freshcount == 0) ? track_numberminutes - 1 : -1;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)