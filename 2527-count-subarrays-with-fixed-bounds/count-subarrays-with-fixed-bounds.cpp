// Brute Force Code & Optimal Code
class Solution {
public:
    long long countSubarrays(vector<int>& nums, int mink, int maxk) {
        // variable to store the total number of fixed bound subarrays
        long long answer = 0;
        // most recent index where mink was found
        int minimum_position = -1;
        // most recent index where maxk was found
        int maximum_position = -1;
        // most recent index of an element outside the valid range [mink, maxk]
        int left_boundary = -1;
        // traverse the array
        for (int i = 0; i < nums.size(); i++) {
            // if the current element is invalid update the left boundary
            if (nums[i] < mink || nums[i] > maxk) {
                left_boundary = i;
            }
            // record the latest position of mink
            if (nums[i] == mink) {
                minimum_position = i;
            }
            // record the latest position of maxk
            if (nums[i] == maxk) {
                maximum_position = i;
            }
            // earliest of the latest positions of mink and maxk determines how many valid subarrays can end at index i
            int count = min(minimum_position, maximum_position) - left_boundary;
            // only positive values contribute to the final answer
            answer += max(0, count);
        }
        // return the total number of fixed bound subarrays
        return answer;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)