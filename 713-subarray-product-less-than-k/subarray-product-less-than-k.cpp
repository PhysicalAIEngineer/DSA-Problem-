// Brute Force Code & Optimal Code
class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        // if k <= 1, no positive product can be less than k
        if (k <= 1) {
            return 0;
        }
        // length of array
        int n = nums.size();
        // total number of valid subarrays
        int count = 0;
        // left and right pointers of sliding window
        int left = 0;
        int right = 0;
        // product of current window
        long long product = 1;
        // expand window using right pointer
        while (right < n) {
            // include nums[right] in the window
            product *= nums[right];
            // if product becomes >= k shrink window from the left
            while (product >= k) {
                // remove nums[left] from product
                product /= nums[left];
                // move left pointer forward
                left++;
            }
            // all subarrays ending at right and starting from left to right are valid
            count += (right - left) + 1;
            // move right pointer forward
            right++;
        }
        // return total number of valid subarrays
        return count;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)