// Brute Force Code & Optimal Code
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        // max heap implemented using negative values
        priority_queue<pair<int, int>> max_heap;
        // list to store the maximum element of each sliding window
        vector<int> result;
        // total number of elements in the array
        int n = nums.size();
        // traverse the array
        for (int i = 0; i < n; i++) {
            // remove elements from the heap that are no longer inside the current sliding window
            while (!max_heap.empty() &&
                   max_heap.top().second <= i - k) {
                max_heap.pop();
            }
            // insert the current element along with its index into the max heap
            max_heap.push({nums[i], i});
            // once the first window of size k is formed the heap top element is the maximum value
            if (i >= k - 1) {
                result.push_back(max_heap.top().first);
            }
        }
        // return the maximum values for every sliding window
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)