// Brute Force Code & Optimal Code
class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        // variable to store the number of zeros in the current window
        int zero_count = 0;
        // variable to store the maximum length of a valid subarray
        int longest_window = 0;
        // left pointer of the sliding window
        int left = 0;
        // traverse the array using the right pointer
        for (int right = 0; right < nums.size(); right++) {
            // include the current element in the sliding window
            if (nums[right] == 0) {
                zero_count++;
            }
            // shrink the window until it contains at most one zero
            while (zero_count > 1) {
                // if a zero leaves the window update the zero count
                if (nums[left] == 0) {
                    zero_count--;
                }
                // move the left pointer to shrink the window
                left++;
            }
            // update the maximum valid length since one element must be deleted the window length is (right - left)
            longest_window = max(longest_window, right - left);
        }
        // return the maximum length after deleting one element
        return longest_window;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)