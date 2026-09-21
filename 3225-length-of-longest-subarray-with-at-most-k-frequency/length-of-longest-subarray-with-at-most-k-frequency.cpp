// Brute Force Code & Optimal Code
class Solution {
public:
    int maxSubarrayLength(vector<int>& nums, int k) {
        // length of the array
        int n = nums.size();
        // frequency map mp[x] = number of times x appears in current window
        unordered_map<int, int> mp;
        // left and right pointers
        int i = 0;
        int j = 0;
        // maximum valid subarray length
        int result = 0;
        // expand window using j
        while (j < n) {
            // add nums[j] to the current window
            mp[nums[j]]++;
            // if the frequency of nums[j] becomes greater than k, shrink the window from the left
            while (i < j && mp[nums[j]] > k) {
                // remove nums[i] from the frequency map
                mp[nums[i]]--;
                // move left pointer forward
                i++;
            }
            // current window is valid update maximum length
            result = max(result, j - i + 1);
            // move right pointer forward
            j++;
        }
        // return maximum valid subarray length
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)