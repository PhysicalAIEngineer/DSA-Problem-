// Brute Force Code & Optimal Code
class Solution {
public:
    // vector to store all possible subsets
    vector<vector<int>> result;
    // backtracking function to generate all subsets
    void solve(vector<int>& nums, int index,vector<int>& current) {
        // if all elements have been processed store the current subset
        if (index >= nums.size()) {
            result.push_back(current);
            return;
        }
        // include the current element
        current.push_back(nums[index]);
        // recursively process the next element
        solve(nums, index + 1, current);
        // backtrack by removing the last element
        current.pop_back();
        // exclude the current element
        solve(nums, index + 1, current);
    }
    // return all possible subsets
    vector<vector<int>> subsets(vector<int>& nums) {
        // clear any previously stored subsets
        result.clear();
        // vector to build the current subset
        vector<int> current;
        // start generating subsets
        solve(nums, 0, current);
        // return all generated subsets
        return result;
    }
};

// Time Complexity : O(N!)
// Space Complexity : O(N)