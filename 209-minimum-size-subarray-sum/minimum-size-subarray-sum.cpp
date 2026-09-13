// Brute Force Code & Optimal Code
class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        // total number of elements in the array
        int n = nums.size();
        // initialize the sliding window pointer
        int left = 0;
        int right = 0;
        // variable to store the sum of the current window
        int current_sum = 0;
        // variable to store the minimum length of valid subarray
        int minimum_length = n + 1;
        // expand the sliding window using the right pointer
        while (right < n) {
            // include the current element in the window
            current_sum += nums[right];
            // when the current window sum is at least the target
            while (current_sum >= target) {
                // update the minimum length
                minimum_length = min(minimum_length, right - left + 1);
                // remove the leftmost element from the window
                current_sum -= nums[left];
                // slide the window to the right
                left++;
            }
            // slide the window to the right
            right++;
        }
        // if no valid subarray exists return 0 otherwise return the minimum length found
        return minimum_length == n + 1 ? 0 : minimum_length;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)