// Optimal Code
class Solution {
public:
    // recursive function with memoization
    // 1. idx     : current index in nums
    // 2. curror  : bitwise OR of elements selected so far
    // 3. nums    : input array
    // 4. maxor   : maximum possible OR
    // 5. t       : DP/memoization table
    int countSubsets(int idx, int currOr, vector<int>& nums, int maxOr, vector<vector<int>>& t) {
        // base case: all elements have been processed.
        if(idx == nums.size()) {
            // if current OR equals maximum OR this is one valid subset.
            if(currOr == maxOr)
                return t[idx][currOr] = 1; 
            // otherwise, this subset is invalid.
            return t[idx][currOr] = 0;
        }
        // check whether this state has already been calculated.
        if(t[idx][currOr] != -1) {
            return t[idx][currOr];
        }
        // choice 1: include nums[idx] in the subset.
        int takeCount = countSubsets(idx+1, currOr | nums[idx], nums, maxOr, t);
        // choice 2: do not include nums[idx].
        int notTakeCount = countSubsets(idx+1, currOr, nums, maxOr, t);
        // combine both choice total number of valid subset is : subset that take nums[idx] + subset that do not take nums[idx]
        return t[idx][currOr] = takeCount + notTakeCount;
    }
    int countMaxOrSubsets(vector<int>& nums) {
        // find the maximum possible OR the maximum OR is the OR of all elements.
        int maxOr = 0;
        // calculate or all element
        for(int &num : nums) {
            maxOr |= num;
        }
        // number of elements.
        int n = nums.size();
        // DP table:
        // t[idx][curror]
        // idx     -> current position
        // curror  -> OR obtained so far
        // -1 means the state has not been calculated yet.
        vector<vector<int>> t(n+1, vector<int>(maxOr+1, -1));
        // initially no elements have been selected so current OR is 0.
        int currOr = 0;
        // start recursion from index 0
        return countSubsets(0, currOr, nums, maxOr, t);
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)