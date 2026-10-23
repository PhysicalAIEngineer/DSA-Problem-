// Brute Force Code & Optimal Code
class Solution {
public:
    // memoization array: t[i] stores the maximum amount of money we can rob starting from house index i and continuing to the end a value of -1 means that the answer has not been calculated yet size 101 supports indices from 0 to 100.
    vector<int> t;
    // recursive helper function: solve(i) returns the maximum amount of money can rob starting from house index i.
    int solve(vector<int>& nums, int i, int n) {
        // base case: if i is greater than or equal to n, there are no houses left therefore, no additional money can be collected.
        if (i >= n) {
            return 0;
        }
        // memoization check: if t[i] is not -1, we have already calculated the maximum money obtainable starting from house i. return the cached result instead of solving it again.
        if (t[i] != -1) {
            return t[i];
        }
        // option 1: take the current house.
        // rob house i and collect nums[i] since two adjacent houses cannot both be robbed skip house i + 1 and continue from house i + 2 total money = money in current house + best money from i + 2.
        int take_current_house = nums[i] + solve(nums, i + 2, n);
        // option 2: skip the current house.
        // do not rob house i. Move to house i + 1 and find the maximum money obtainable from that point onward.
        int skip_current_house = solve(nums, i + 1, n);
        // choose the better option:
        // compare the money obtained by taking the current house with the money obtained by skipping it. store the larger value to avoid recalculating this subproblem.
        t[i] = max(take_current_house, skip_current_house);
        // return the maximum money obtainable starting from house i.
        return t[i];
    }
    int rob(vector<int>& nums) {
        // store the total number of houses.
        int n = nums.size();
        // initialize the memoization array with -1 each position represents a house index whose answer has not been calculated yet.
        t.assign(101, -1);
        // start from house index 0 this calculates the maximum money that can be robbed without robbing two adjacent houses.
        return solve(nums, 0, n);
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)