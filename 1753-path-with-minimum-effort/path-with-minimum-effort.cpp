// Brute Force Code & Optimal Code
using namespace std;
class Solution {
public:
    int minimumEffortPath(vector<vector<int>>& heights) {
        // number of rows
        int m = heights.size();
        // number of columns
        int n = heights[0].size();
        // 4 possible directions: up, down, right, left
        vector<pair<int, int>> directions = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
        // result[x][y] stores the minimum effort required to reach cell (x, y)
        vector<vector<int>> result(m, vector<int>(n, INT_MAX));
        // min heap stores: (minimum effort, (row, column))
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> min_heap;
        // start from the top-left cell initial effort is 0
        min_heap.push({0, 0, 0});
        result[0][0] = 0;
        // Dijkstra algorithm
        while (!min_heap.empty()) {
            // cell with minimum effort
            auto [difference, x, y] = min_heap.top();
            min_heap.pop();
            // if reached the destination this is the minimum possible effort because min heap gives the smallest effort first
            if (x == m - 1 && y == n - 1) {
                return difference;
            }
            // check all 4 neighbouring cells
            for (auto direction : directions) {
                // calculate neighbour coordinates
                int x_ = x + direction.first;
                int y_ = y + direction.second;
                // check if neighbour is inside the grid
                if (x_ >= 0 && x_ < m && y_ >= 0 && y_ < n) {
                    // calculate effort of moving from current cell to neighbour
                    int currentDifference = abs(heights[x][y] - heights[x_][y_]);
                    // path effort is the maximum height difference encountered on the path
                    int newDifference = max(difference, currentDifference);
                    // if this path gives smaller effort
                    if (result[x_][y_] > newDifference) {
                        // store the minimum effort for this cell
                        result[x_][y_] = newDifference;
                        // push updated effort into min heap
                        min_heap.push({result[x_][y_], x_, y_});
                    }
                }
            }
        }
        // return minimum effort to reach destination
        return result[m - 1][n - 1];
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)