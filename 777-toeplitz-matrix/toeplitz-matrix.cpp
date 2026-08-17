// Brute Force Code & Optimal Code
class Solution {
public:
    // check whether the given matrix is a Toeplitz matrix toeplitz matrix has the property that every top-left to bottom-right diagonal contains the same value.
    bool isToeplitzMatrix(vector<vector<int>>& matrix) {
        // number of rows and columns
        int m = matrix.size();
        int n = matrix[0].size();
        // traverse the matrix starting from the second row and second column
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                // compare the current element with its top-left diagonal neighbor if they are different, the matrix is not a Toeplitz matrix.
                if (matrix[i][j] != matrix[i - 1][j - 1]) {
                    return false;
                }
            }
        }
        // every element matches its top-left diagonal neighbor, so the matrix is Toeplitz.
        return true;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(1)