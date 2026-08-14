// Brute Force Code
class Solution {
public:
    // sort every diagonal of the matrix in ascending order
    vector<vector<int>> diagonalSort(vector<vector<int>>& mat) {
        // number of rows and columns
        int rows = mat.size();
        int cols = mat[0].size();
        // function to sort a single diagonal starting from (startRow, startCol)
        auto sortDiagonal = [&](int startRow, int startCol) {
            // store all elements of the current diagonal
            vector<int> diagonal;
            int row = startRow;
            int col = startCol;
            // collect the diagonal elements
            while (row < rows && col < cols) {
                diagonal.push_back(mat[row][col]);
                row++;
                col++;
            }
            // sort the collected elements
            sort(diagonal.begin(), diagonal.end());
            // put the sorted elements back into the same diagonal
            row = startRow;
            col = startCol;
            int index = 0;
            while (row < rows && col < cols) {
                mat[row][col] = diagonal[index];
                index++;
                row++;
                col++;
            }
        };
        // sort all diagonals that start from the first row
        for (int col = 0; col < cols; col++) {
            sortDiagonal(0, col);
        }
        // sort all diagonals that start from the first column skip the top-left cell because its diagonal has already been processed
        for (int row = 1; row < rows; row++) {
            sortDiagonal(row, 0);
        }
        // return the matrix with all diagonals sorted
        return mat;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)