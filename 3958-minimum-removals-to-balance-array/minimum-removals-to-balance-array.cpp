// Brute Force Code & Optimal Code
class Solution {
public:
    int minRemoval(vector<int>& nums, int k) {
        // total number of elements in the array
        int n = nums.size();
        // sort the array so the minimum and maximum elements of the window are at its ends
        sort(nums.begin(), nums.end());
        // initialize the current minimum and maximum elements
        int maximum_element = nums[0];
        int minimum_element = nums[0];
        // store the length of the longest valid subarray
        int longest_length = 1;
        // initialize two pointers left -> beginning of the window
        int left = 0;
        // right -> end of the window
        int right = 0;
        // traverse the array using the right pointer
        while (right < n) {
            // update the current maximum and minimum elements
            maximum_element = nums[right];
            minimum_element = nums[left];
            // shrink the window until the condition is satisfied
            while (left < right &&  maximum_element > 1LL * k * minimum_element) {
                left++;
                minimum_element = nums[left];
            }
            // update the longest valid window found so far
            longest_length = max(longest_length, right - left + 1);
            // expand the window
            right++;
        }
        // minimum removals = total elements - longest valid subarray
        return n - longest_length;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(1)