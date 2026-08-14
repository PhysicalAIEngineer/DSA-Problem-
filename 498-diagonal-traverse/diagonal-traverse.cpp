// Optimal Code
class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& mat) {
        // number of rows and columns
        int m = mat.size();
        int n = mat[0].size();
        // dictionary to map: (row + col) -> elements on the diagonal
        unordered_map<int, vector<int>> mp;
        // store the final diagonal traversal
        vector<int> result;
        // group all matrix elements by their diagonal index (row + col)
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                // cells having the same value of (row + col) belong to the same diagonal
                int key = i + j;
                // create a new list for the diagonal if it does not exist
                if (mp.find(key) == mp.end()) {
                    mp[key] = {};
                }
                // store the current element
                mp[key].push_back(mat[i][j]);
            }
        }
        // even diagonals are traversed upward & odd diagonals are traversed downward
        bool flip = true;
        // process diagonals in increasing order
        for (int key = 0; key < m + n - 1; key++) {
            // reverse every alternate diagonal to obtain the required zigzag order
            if (flip) {
                reverse(mp[key].begin(), mp[key].end());
            }
            // add the current diagonal to the final answer
            result.insert(result.end(), mp[key].begin(), mp[key].end());
            // toggle the traversal direction for the next diagonal
            flip = !flip;
        }
        // return the diagonal traversal
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)