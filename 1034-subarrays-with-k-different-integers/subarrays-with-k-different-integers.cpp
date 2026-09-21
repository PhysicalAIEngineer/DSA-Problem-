// Brute Force Code & Optimal Code
class Solution {
public:
    // count total subarrays having at most k distinct elements
    int slidingWindow(vector<int>& nums, int k) {
        // frequency map of elements in current window
        unordered_map<int, int> mp;
        // length of array
        int n = nums.size();
        // left and right pointers
        int i = 0;
        int j = 0;
        // total number of valid subarrays
        int count = 0;
        // expand window using j
        while (j < n) {
            // add nums[j] to the window
            mp[nums[j]]++;
            // if window has more than k distinct elements shrink it from the left
            while (mp.size() > k) {
                // remove nums[i] from the window
                mp[nums[i]]--;
                // if its frequency becomes 0 remove it from the map
                if (mp[nums[i]] == 0) {
                    mp.erase(nums[i]);
                }
                // move left pointer forward
                i++;
            }
            // all subarrays ending at j and starting from i to j are valid
            count += (j - i + 1);
            // move right pointer forward
            j++;
        }
        // return count of subarrays with at most k distinct elements
        return count;
    }
    int subarraysWithKDistinct(vector<int>& nums, int k) {
        // exactly k distinct = (at most k) - (at most k - 1)
        return slidingWindow(nums, k) - slidingWindow(nums, k - 1);
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)