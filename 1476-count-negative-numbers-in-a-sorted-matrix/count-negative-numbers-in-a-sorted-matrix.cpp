// Brute Force Code & Optimal Code
class Solution {
public:
    // count the total number of negative values present in the matrix.
    int countNegatives(vector<vector<int>>& grid) {
        // number of rows in the matrix.
        int m = grid.size();
        // number of columns in the matrix.
        int n = grid[0].size();
        // store the total count of negative numbers.
        int result = 0;
        // traverse every row.
        for (int i = 0; i < m; i++) {
            // traverse every column of the current row.
            for (int j = 0; j < n; j++) {
                // check whether the current element is negative.
                if (grid[i][j] < 0) {
                    // increase the negative number count.
                    result++;
                }
            }
        }
        // return the total number of negative elements.
        return result;
    }
};

// Time Complexity : O(N^2)
// Space Complexity : O(N)