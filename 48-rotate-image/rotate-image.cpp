// Brute Force Code & Opitmal Code
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        // size of the square matrix
        int n = matrix.size();
        // compute the transpose of the matrix swap matrix[i][j] with matrix[j][i] for all elements on and above the main diagonal
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                swap(matrix[i][j], matrix[j][i]);
            }
        }
        // reverse every row
        for (int i = 0; i < n; i++) {
            reverse(matrix[i].begin(), matrix[i].end());
        }
    }
};

// Time Complexity : O(N^2)
// Space Complexity : O(N)