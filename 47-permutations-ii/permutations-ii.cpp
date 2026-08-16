// Brute Force Code & Optimal Code
class Solution {
public:
    // vector to store all unique permutations
    vector<vector<int>> result;
    // total number of elements in the array
    int n = 0;
    // backtracking function to generate unique permutations using in-place swapping
    void solve(int index, vector<int>& nums) {
        // if every position has been fixed store a copy of the current permutation
        if (index == n) {
            result.push_back(nums);
            return;
        }
        // set to keep track of values already used at the current recursion level
        unordered_set<int> used;
        // Try placing every remaining element at the current position
        for (int i = index; i < n; i++) {
            // skip duplicate values to avoid generating duplicate permutations
            if (used.count(nums[i])) {
                continue;
            }
            // mark the current value as used
            used.insert(nums[i]);
            // swap the current element into the current position
            swap(nums[index], nums[i]);
            // recursively fix the next position
            solve(index + 1, nums);
            // backtrack by restoring the original order
            swap(nums[index], nums[i]);
        }
    }
    // return all unique permutations
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        // clear any previously stored permutations
        result.clear();
        // store the total number of elements
        n = nums.size();
        // start generating unique permutations
        solve(0, nums);
        // return all unique permutations
        return result;
    }
};

// Time Complexity : O(N!)
// Space Complexity : O(N)