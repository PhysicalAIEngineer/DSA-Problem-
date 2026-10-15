// Brute Force Code & Optimal Code
class Solution {
public:
    int nearestExit(vector<vector<char>>& maze, vector<int>& entrance) {
        // four possible movement directions: right, left, down, up
        vector<pair<int, int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        // get the number of rows and columns
        int m = maze.size();
        int n = maze[0].size();
        // create a queue for BFS
        queue<pair<int, int>> q;
        // add the entrance cell to the queue
        q.push({entrance[0], entrance[1]});
        // mark the entrance as visited to avoid revisiting it
        maze[entrance[0]][entrance[1]] = '+';
        // count the number of steps from the entrance
        int steps = 0;
        // perform BFS until the queue becomes empty
        while (!q.empty()) {
            // number of cells at the current BFS level
            int size = q.size();
            while (size--) {
                // remove the front cell from the queue
                auto temp = q.front();
                q.pop();
                int r = temp.first;
                int c = temp.second;
                // check whether the current cell is an exit the entrance itself cannot be considered an exit
                if ((r != entrance[0] || c != entrance[1]) && (r == 0 || r == m - 1 || c == 0 || c == n - 1)) {
                    return steps;
                }
                // explore all four neighboring cells
                for (auto direction : directions) {
                    int i = r + direction.first;
                    int j = c + direction.second;
                    // check whether the neighbor is inside the maze and has not been visited or blocked
                    if (i >= 0 && i < m &&
                        j >= 0 && j < n &&
                        maze[i][j] != '+') {
                        // add the accessible neighbor to the queue
                        q.push({i, j});
                        // mark the neighbor as visited
                        maze[i][j] = '+';
                    }
                }
            }
            // increase the distance after processing one BFS level
            steps++;
        }
        // return -1 if no exit can be reached
        return -1;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)