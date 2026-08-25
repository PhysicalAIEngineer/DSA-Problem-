// Brute Force Code & Optimal Code
class Solution {
public:
    // store the total number of valid subsets found
    int result = 0;
    // store the value of k
    int K = 0;
    void dfs(vector<int>& nums, int idx, unordered_map<int, int>& mp) {
        // base case: if  have processed all elements the current subset is one valid subset.
        if (idx == nums.size()) {
            // count this subset
            result++;
            return;
        }
        // do not take nums[idx] skip the current number and move to the next index.
        dfs(nums, idx + 1, mp);
        // take nums[idx] number can be added to the current subset only if: nums[idx] - K is not present and
        // nums[idx] + K is not present this ensures that the absolute difference between any two selected numbers is not K.
        if (mp[nums[idx] - K] == 0 &&
            mp[nums[idx] + K] == 0) {
            // add nums[idx] to the current subset store its frequency in the hashmap.
            mp[nums[idx]]++;
            // recursively process the remaining elements
            dfs(nums, idx + 1, mp);
            // backtracking remove nums[idx] from the current subset before trying another choice.
            mp[nums[idx]]--;
        }
    }
    int beautifulSubsets(vector<int>& nums, int k) {
        // reset the result in case the same solution object is used again.
        result = 0;
        // store k so that dfs() can access it
        K = k;
        // hashmap storing the frequency of each number currently selected in the subset.
        unordered_map<int, int> mp;
        // start DFS from the first element
        dfs(nums, 0, mp);
        // DFS also counts the empty subset problem asks for non-empty subsets so remove the empty subset from the answer.
        return result - 1;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)