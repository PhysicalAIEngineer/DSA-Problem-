// Brute Force Code & Optimal Code
class Solution {
public:
    // memoization table: t[i][j] stores the total number of unique paths from the current cell (i, j) to the destination cell (m - 1, n - 1) -1 means that the result has not been calculated yet.
    vector<vector<int>> t;
    // recursive function: solve(i, j) returns the number of unique paths from the current cell (i, j) to the destination.1. i -> current row index. & 2. j -> current column index can move only: 1. right -> (i, j + 1) & 2. down  -> (i + 1, j) moving left or upward is not allowed.
    int solve(int i, int j, int m, int n) {
        // base case 1: destination reached.
        // the destination is the bottom-right cell (m-1, n-1) if the current position is the destination have successfully found one complete path.
        if (i == m - 1 && j == n - 1) {
            return 1;
        }
        // base case 2: current position is outside the grid.
        // valid row indices are from 0 to m-1 & valid column indices are from 0 to n - 1. if the current position is outside these boundaries this path cannot reach the destination.
        if (i < 0 || i >= m || j < 0 || j >= n) {
            return 0;
        }
        // memoization: check whether the number of paths from the current cell (i, j) has already been calculated if t[i][j] is not -1, return the stored result instead of making the same recursive calls again.
        if (t[i][j] != -1) {
            return t[i][j];
        }
        // option 1: move right.
        // from the current cell (i, j), move one column to the right new position becomes (i, j + 1) the recursive call returns the number of valid paths from that position to the destination.
        int right = solve(i, j + 1, m, n);
        // option 2: move down.
        // from the current cell (i, j), move one row downward the new position becomes (i + 1, j) recursive call returns the number of valid paths from that position to the destination.
        int down = solve(i + 1, j, m, n);
        // calculate the total number of unique paths.
        // every valid path must begin with either: 1. right movement. & 2. down movement. these two groups of paths are independent so add their results to get the total number of paths store the answer in the memoization table so that future calls to the same cell can reuse it.
        t[i][j] = right + down;
        // return the total number of unique paths from (i, j).
        return t[i][j];
    }
    int uniquePaths(int m, int n) {
        // step 1: Initialize the memoization table.
        // it has (m + 1) rows and (n + 1) columns every cell is initialized to -1, indicating that its result has not been calculated yet.
        t.assign(m + 1, vector<int>(n + 1, -1));
        // step 2: start recursion from the top-left corner.
        // starting position: row = 0 & column = 0 solve(0, 0) calculates the total number of unique paths from the starting cell to the destination.
        return solve(0, 0, m, n);
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)