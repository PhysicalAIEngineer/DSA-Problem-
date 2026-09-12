// Brute Force Code & Optimal Code
class Solution {
public:
    int minKBitFlips(vector<int>& nums, int k) {
        // total number of elements in the array
        int n = nums.size();
        // stores the total number of k-bit flips performed
        int flips = 0;
        // is_flipped[i] = true means flip operation starts at index i
        vector<bool> is_flipped(n, false);
        // number of flip operations that are currently affecting the current index
        int active_flips = 0;
        // traverse every element in the array
        for (int i = 0; i < n; i++) {
            // if flip started at index (i - k) its effect ends before the current index so remove it from the active flip count
            if (i >= k && is_flipped[i - k]) {
                active_flips--;
            }
            // determine the effective value of nums[i] if active_flips is even: current value remains unchanged or  if active_flips is odd: current value is flipped if the effective value is 0, must start a new flip here
            if (active_flips % 2 == nums[i]) {
                // not enough elements remain to perform a k-length flip
                if (i + k > n) {
                    return -1;
                }
                // start a new flip at index i
                active_flips++;
                // mark that a flip starts here
                is_flipped[i] = true;
                // increase the total flip count
                flips++;
            }
        }
        // return the minimum number of flips required
        return flips;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)