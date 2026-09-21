// Brute Force Code & Optimal Code
class Solution {
public:
    int longestSubarray(vector<int>& nums, int limit) {
        // length of the array
        int n = nums.size();
        // max heap: store (-value, index) priority_queue is already a max heap store (value, index) directly.
        priority_queue<pair<int, int>> maxPq;
        // min heap: store (value, index)
        priority_queue<pair<int, int>,vector<pair<int, int>>,greater<pair<int, int>>> minPq;
        // sliding window pointers
        int i = 0;
        int j = 0;
        // store maximum valid window length
        int maxLength = 0;
        // expand the window using j
        while (j < n) {
            // add current element to max heap
            maxPq.push({nums[j], j});
            // add current element to min heap
            minPq.push({nums[j], j});
            // check whether current window is invalid max value - min value must be <= limit
            while (maxPq.top().first - minPq.top().first > limit) {
                // move left pointer just after the index of the smaller-indexed extreme element
                i = min(maxPq.top().second, minPq.top().second) + 1;
                // remove outdated elements from max heap whose index is outside the current window
                while (!maxPq.empty() && maxPq.top().second < i) {
                    maxPq.pop();
                }
                // remove outdated elements from min heap whose index is outside the current window
                while (!minPq.empty() && minPq.top().second < i) {
                    minPq.pop();
                }
            }
            // current window [i...j] is valid update maximum window length
            maxLength = max(maxLength, j - i + 1);
            // move right pointer forward
            j++;
        }
        // return longest valid subarray length
        return maxLength;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)