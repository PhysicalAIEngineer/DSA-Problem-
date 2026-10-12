// Brute Force Code & Optimal Code
class Solution {
public:
    vector<vector<int>> highestPeak(vector<vector<int>>& isWater) {
        // get the number of rows and columns
        int m = isWater.size();
        int n = isWater[0].size();
        // define the four possible movement directions
        vector<pair<int, int>> directions = {{0, 1}, {0, -1}, {-1, 0}, {1, 0}};
        // initialize all cell heights as -1 (unvisited)
        vector<vector<int>> height(m, vector<int>(n, -1));
        // create a queue for BFS
        queue<pair<int, int>> q;
        // water cells have height 0 add all water cells to the queue as BFS starting points
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (isWater[i][j] == 1) {
                    height[i][j] = 0;
                    q.push({i, j});
                }
            }
        }
        // apply Multi-Source BFS to calculate the heights
        while (!q.empty()) {
            // get the number of cells at the current BFS level
            int N = q.size();
            while (N--) {
                // remove the front cell from the queue
                auto [i, j] = q.front();
                q.pop();
                // visit all four neighboring cells
                for (auto dir : directions) {
                    int i_ = i + dir.first;
                    int j_ = j + dir.second;
                    // check whether the neighbor is inside the grid and unvisited
                    if (i_ >= 0 && i_ < m && j_ >= 0 && j_ < n && height[i_][j_] == -1) {
                        // set the neighbor's height one greater than the current cell
                        height[i_][j_] = height[i][j] + 1;
                        // add the neighbor to the queue for further exploration
                        q.push({i_, j_});
                    }
                }
            }
        }
        // return the matrix containing the highest possible heights
        return height;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)