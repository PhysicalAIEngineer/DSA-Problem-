// Optimal Code
class Solution {
public:
    // sort every diagonal of the matrix in ascending order
    vector<vector<int>> diagonalSort(vector<vector<int>>& mat) {
        // number of rows and columns
        int m = mat.size();
        int n = mat[0].size();
        // dictionary to map: (row - column) -> elements of that diagonal
        unordered_map<int, vector<int>> mp;
        // collect all elements of each diagonal
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                // cells with the same value of (row - column) belong to the same diagonal
                int key = i - j;
                // create a new list for this diagonal if it does not exist
                if (mp.find(key) == mp.end()) {
                    mp[key] = {};
                }
                // store the current element
                mp[key].push_back(mat[i][j]);
            }
        }
        // sort the elements of every diagonal
        for (auto& pair : mp) {
            sort(pair.second.begin(), pair.second.end());
        }
        // put sorted values back into the matrix traverse from bottom-right so that pop_back() removes the largest remaining element
        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                // calculate the diagonal key
                int key = i - j;
                // take the largest remaining element and place it at the current position
                mat[i][j] = mp[key].back();
                // remove the used element
                mp[key].pop_back();
            }
        }
        // return the matrix with sorted diagonals
        return mat;
    }
};

// Time Complexity : O(Nlog)
// Space Complexity : O(N)