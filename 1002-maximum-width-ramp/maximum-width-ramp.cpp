// Brute Force Code & Optimal Code
class Solution {
public:
    int maxWidthRamp(vector<int>& nums) {
        // total number of elements in the array
        int n = nums.size();
        // maximum_right[i] stores the maximum value from index i to the end of the array
        vector<int> maximum_right(n);
        maximum_right[n - 1] = nums[n - 1];
        // build the maximum_right array by traversing from right to left
        for (int i = n - 2; i >= 0; i--) {
            maximum_right[i] =
                max(maximum_right[i + 1], nums[i]);
        }
        // variable to store the maximum ramp width
        int maximum_ramp = 0;
        // initialize two pointers
        // left  -> possible starting index of the ramp
        // right -> possible ending index of the ramp
        int left = 0;
        int right = 0;
        // traverse the array using the right pointer
        while (right < n) {
            // if nums[left] is greater than every value from right onward, move the left pointer until a valid ramp becomes possible
            while (left < right && nums[left] > maximum_right[right]) {
                left++;
            }
            // update the maximum ramp width
            maximum_ramp = max(maximum_ramp, right - left);
            // move to the next ending index
            right++;
        }
        // return the maximum ramp width found
        return maximum_ramp;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(1)