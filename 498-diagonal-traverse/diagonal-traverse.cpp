// Brute Force Code
class Solution {
public:
    // return the diagonal traversal of the matrix
    vector<int> findDiagonalOrder(vector<vector<int>>& mat) {
        // number of rows and columns
        int rows = mat.size();
        int cols = mat[0].size();
        // store the final diagonal traversal
        vector<int> result;
        // total number of diagonals in the matrix
        int total_diagonals = rows + cols - 1;
        // process each diagonal
        for (int diagonal = 0; diagonal < total_diagonals; diagonal++) {
            // store current diagonal elements
            vector<int> current_diagonal;
            // collect all elements belonging to this diagonal
            for (int row = 0; row < rows; row++) {
                for (int col = 0; col < cols; col++) {
                    // cells with the same value of (row + col) belong to the same diagonal
                    if (row + col == diagonal) {
                        current_diagonal.push_back(mat[row][col]);
                    }
                }
            }
            // even-numbered diagonals are traversed from bottom to top, so reverse their order
            if (diagonal % 2 == 0) {
                reverse(current_diagonal.begin(),current_diagonal.end());
            }
            // append the current diagonal to the result
            result.insert(result.end(), current_diagonal.begin(),current_diagonal.end());
        }
        // return the diagonal traversal
        return result;
    }
};

// Time Complexity : O(N^3)
// Space Complexity : O(N)