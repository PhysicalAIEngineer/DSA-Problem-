// Brute Force Code & Optimal Code
class Solution {
public:
    // store the total number of elements in the input array
    int n = 0;
    void backtrack(vector<int>& nums, int idx,vector<int>& curr, vector<vector<int>>& result
    ) {
        // check whether the current subsequence is valid subsequence is valid if it contains at least 2 elements.
        if (curr.size() > 1) {
            // store a copy of the current subsequence use curr directly as a reference, but push_back() stores a copy of its current contents.
            result.push_back(curr);
        }
        // avoid duplicate choices at this recursion level set stores values that have already been used at the current recursion level it prevents generating the same subsequence multiple times when duplicate values exist.
        unordered_set<int> st;
        // try every possible next element starting from idx start from idx because a subsequence must preserve the original order of elements.
        for (int i = idx; i < n; i++) {
            // choose nums[i] when:
            // 1. curr is empty
            // 2. nums[i] is greater than or equal to the last element of curr this ensures the subsequence is non-decreasing also, nums[i] must not have already been used at this recursion level.
            if ((curr.empty() || nums[i] >= curr.back()) && st.find(nums[i]) == st.end()) {
                // choose nums[i] add the current number to the subsequence.
                curr.push_back(nums[i]);
                // explore further choices move to i + 1 because we cannot reuse the same array position.
                backtrack(nums, i + 1, curr, result);
                // backtrack remove the last element so that can try another possible choice.
                curr.pop_back();
                // mark this value as used at the current recursion level if the same value appears again at this level, it will be skipped.
                st.insert(nums[i]);
            }
        }
    }
    vector<vector<int>> findSubsequences(vector<int>& nums) {
        // store the number of elements in nums.
        n = nums.size();
        // store all valid subsequences.
        vector<vector<int>> result;
        // store the subsequence currently being built.
        vector<int> curr;
        // start backtracking from index 0.
        backtrack(nums, 0, curr, result);
        // return all valid non-decreasing subsequences of length at least 2.
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)