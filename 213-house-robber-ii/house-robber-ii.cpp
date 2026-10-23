// Brute Force Code & Optimal Code
class Solution {
public:
    // memoization array: t[i] stores the maximum amount of money we can rob when considering houses starting at index i. a value of -1 means that the answer has not been calculated yet size 101 supports indices from 0 to 100.
    vector<int> t;
    // recursive helper function: solve(i, end) returns the maximum money we can rob from house i through house end, inclusive the end parameter limits the range of houses being considered.
    int solve(vector<int>& nums, int i, int end) {
        // base case: if i has moved beyond the last allowed house there are no houses left to consider, so return 0.
        if (i > end) {
            return 0;
        }
        // memoization check: if have already calculated the answer for index i return the cached result instead of repeating the work.
        if (t[i] != -1) {
            return t[i];
        }
        // option 1: rob the current house.
        // collect the money in house i since adjacent houses cannot both be robbed skip house i + 1 and continue from house i + 2.
        int rob_current_house = nums[i] + solve(nums, i + 2, end);
        // option 2: skip the current house.
        // do not rob house i. Move to house i + 1 and calculate the maximum money obtainable from the remaining houses.
        int skip_current_house = solve(nums, i + 1, end);
        // choose the better of the two options.
        // store the answer so it can be reused if this subproblem is encountered again.
        t[i] = max(rob_current_house, skip_current_house);
        // return the maximum money obtainable starting at index i.
        return t[i];
    }
    int rob(vector<int>& nums) {
        // store the total number of houses.
        int n = nums.size();
        // edge case 1:
        // if there is only one house, rob it because there are no other houses that could be adjacent to it.
        if (n == 1) {
            return nums[0];
        }
        // edge case 2:
        // if there are exactly two houses, they are adjacent can rob only one, so choose the house with more money.
        if (n == 2) {
            return max(nums[0], nums[1]);
        }
        // initialize the memoization array with -1 each position represents a house index whose answer has not been calculated yet.
        t.assign(101, -1);
        // case 1: Exclude the last house.
        // consider houses from index 0 through index n - 2 the first house is allowed, but the last house is excluded this removes the circular conflict between the first and last houses, turning the remaining houses into a linear problem.
        int exclude_last_house = solve(nums, 0, n - 2);
        // reset the memoization array before solving the second case this prevents answers calculated for the first range from being incorrectly reused for a different range.
        t.assign(101, -1);
        // case 2: Exclude the first house.
        // consider houses from index 1 through index n - 1 the first house is excluded, but the last house is allowed this also removes the circular conflict and leaves a linear house Robber problem.
        int exclude_first_house = solve(nums, 1, n - 1);
        // optimal solution must belong to one of these two cases:
        // 1. exclude the last house.
        // 2. exclude the first house.
        // return whichever case gives us more money.
        return max(exclude_last_house, exclude_first_house);
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)