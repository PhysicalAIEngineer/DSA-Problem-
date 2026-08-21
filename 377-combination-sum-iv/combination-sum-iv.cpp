// Brute Force Code & Optimal Code
class Solution {
public:
    // store the number of elements in nums.
    int n;
    // memoization table t[target][idx] stores the number of ways to form 'target' starting from index 'idx'.
    vector<vector<int>> t;
    int solve(int idx, vector<int>& nums, int target) {
        // base case: if target becomes 0, we have successfully formed the required target this represents one valid combination.
        if (target == 0) {
            return 1;
        }
        // invalid case: if have gone beyond the array there are no more numbers to choose if target becomes negative the current combination exceeded the target.
        if (idx >= n || target < 0) {
            return 0;
        }
        // check the memoization table if this state has already been calculated return the stored answer.
        if (t[target][idx] != -1) {
            return t[target][idx];
        }
        // store the total number of valid combinations found for the current state.
        int result = 0;
        // try every possible number can choose any number from idx to n - 1 as the next element of the combination.
        for (int i = idx; i < n; i++) {
            // choose nums[i] subtract nums[i] from the remaining target and start again from index 0 because:
            // 1. numbers can be used multiple times.
            // 2. order matters.
            int take_i = solve(0, nums, target - nums[i]);
            // add the number of valid combinations obtained by choosing nums[i].
            result += take_i;
        }
        // store the answer for the current state so that it can be reused later.
        t[target][idx] = result;
        // return the number of valid combinations.
        return result;
    }
    int combinationSum4(vector<int>& nums, int target) {
        // store the number of elements in nums.
        n = nums.size();
        // create the memoization table.
        // rows    -> remaining target
        // columns -> current index
        // -1      -> state has not been calculated yet.
        t = vector<vector<int>>(target + 1, vector<int>(n, -1));
        // start the recursive process with:
        // idx = 0    -> use every number
        // target     -> target we need to form
        return solve(0, nums, target);
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)