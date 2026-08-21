// Brute Force Code & Optimal Code
class Solution {
public:
    // store all combinations
    vector<vector<int>> result;
    void solve(int start, int n, int k, vector<int>& temp) {
        // if have selected k numbers store the current combination.
        if (k == 0) {
            result.push_back(temp);
            return;
        }
        // try every number from start to n.
        for (int i = start; i <= n; i++) {
            // Choose i
            temp.push_back(i);
            // choose the remaining k - 1 numbers from the numbers after i.
            solve(i + 1, n, k - 1, temp);
            // backtrack remove i from the current combination.
            temp.pop_back();
        }
    }
    vector<vector<int>> combine(int n, int k) {
        // current combination
        vector<int> temp;
        // start selecting numbers from 1.
        solve(1, n, k, temp);
        // return all combinations.
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)