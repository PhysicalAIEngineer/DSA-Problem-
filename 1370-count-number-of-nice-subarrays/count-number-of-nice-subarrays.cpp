// Brute Force Code & Optimal Code
class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        // total number of elements in the array
        int n = nums.size();
        // count of odd numbers inside the current window
        int odd_count = 0;
        // number of valid subarrays ending at the current right index
        int count = 0;
        // total number of nice subarrays
        int result = 0;
        // left and right pointers of the sliding window
        int left = 0;
        int right = 0;
        // expand the window using the right pointer
        while (right < n) {
            // if the current element is odd add it to the odd-number count
            if (nums[right] % 2 != 0) {
                odd_count++;
                // new odd number changes the possible starting positions so reset count
                count = 0;
            }
            // shrink the window while it contains exactly k odd numbers
            while (odd_count == k) {
                // current window is valid can also remove leading even numbers and still have exactly k odd numbers each such choice creates another valid subarray
                count++;
                // if the left element is odd removing it reduces the odd count
                if (nums[left] % 2 == 1) {
                    odd_count--;
                }
                // move the left pointer forward
                left++;
            }
            // every valid starting position found above creates a nice subarray ending at right
            result += count;
            // move the right pointer forward
            right++;
        }
        // return the total number of subarrays containing exactly k odd numbers
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)