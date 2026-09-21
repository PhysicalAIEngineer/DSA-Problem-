// Brute Force Code & Optimal Code
class Solution {
public:
    int numSubarraysWithSum(vector<int>& nums, int goal) {
        // number of consecutive zeros before the first useful element
        int prefix_zeros = 0;
        // sum of current sliding window
        int window_sum = 0;
        // total number of subarrays having sum = goal
        int count = 0;
        // left and right pointers
        int i = 0;
        int j = 0;
        // expand window using j
        while (j < nums.size()) {
            // add current element to window sum
            window_sum += nums[j];
            // shrink window when nums[i] is 0 so can remove it and create another valid subarray, or when window_sum > goal
            while (i < j && (nums[i] == 0 || window_sum > goal)) {
                // If removing a 1, reset zero count
                if (nums[i] == 1) {
                    prefix_zeros = 0;
                }
                // if removing a 0, increase the number of extra starting positions
                else {
                    prefix_zeros++;
                }
                // remove nums[i] from current window
                window_sum -= nums[i];
                // move left pointer forward
                i++;
            }
            // if current window has the required sum count the current window plus all possible extra leading-zero choices
            if (window_sum == goal) {
                count += 1 + prefix_zeros;
            }
            // move right pointer forward
            j++;
        }
        // return total number of valid subarrays
        return count;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)