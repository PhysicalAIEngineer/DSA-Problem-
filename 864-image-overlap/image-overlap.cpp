// Brute Force Code & Optimal Code
class Solution {
public:
    // find the maximum overlap between two binary images after translating one image in any direction
    int largestOverlap(vector<vector<int>>& img1,vector<vector<int>>& img2) {
        // size of the square matrices
        int n = img1.size();
        // store the maximum overlap found
        int maximum_overlap = 0;
        // try every possible vertical shift from -(n - 1) to (n - 1)
        for (int row_shift = -(n - 1);
             row_shift <= n - 1;
             row_shift++) {
            // try every possible horizontal shift from -(n - 1) to (n - 1)
            for (int col_shift = -(n - 1);
                 col_shift <= n - 1;
                 col_shift++) {
                // count the overlap for the current translation
                int current_overlap = 0;
                // traverse every cell in img1
                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < n; j++) {
                        // compute the new position after applying the shift
                        int new_row = i + row_shift;
                        int new_col = j + col_shift;
                        // ensure the shifted position lies inside img2
                        if (new_row >= 0 && new_row < n && new_col >= 0 && new_col < n) {
                            // count the overlap if both images contain 1
                            if (img1[i][j] == 1 &&
                                img2[new_row][new_col] == 1) {
                                current_overlap++;
                            }
                        }
                    }
                }
                // update the maximum overlap
                maximum_overlap = max(maximum_overlap, current_overlap);
            }
        }
        // return the largest overlap found
        return maximum_overlap;
    }
};

// Time Complexity : O(N^4)
// Space Complexity : O(N)