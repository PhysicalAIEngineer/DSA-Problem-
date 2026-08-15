// Brute Force Code & Optimal Code
class Solution {
public:
    // vector to store all possible permutations
    vector<vector<int>> result;
    // total number of elements in the array
    int n = 0;
    // backtracking function to generate all permutations using in-place swapping
    void solve(int index, vector<int>& nums) {
        // if every position has been fixed store a copy of the current permutation
        if (index == n) {
            result.push_back(nums);
            return;
        }
        // try placing every remaining element at the current position
        for (int i = index; i < n; i++) {
            // swap the current element into the current position
            swap(nums[index], nums[i]);
            // recursively fix the next position
            solve(index + 1, nums);
            // backtrack by restoring the original order
            swap(nums[index], nums[i]);
        }
    }
    // return all possible permutations
    vector<vector<int>> permute(vector<int>& nums) {
        // clear any previously stored permutations
        result.clear();
        // store the total number of elements
        n = nums.size();
        // start generating permutations from the first position
        solve(0, nums);
        // return all generated permutations
        return result;
    }
};

// Time Complexity : O(N!)
// Space Complexity : O(N)