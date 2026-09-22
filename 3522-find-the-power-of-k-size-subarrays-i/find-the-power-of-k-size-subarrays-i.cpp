// Brute Force Code & Optimal Code
class Solution {
public:
    vector<int> resultsArray(vector<int>& nums, int k) {
        // length of the array
        int n = nums.size();
        // there are (n - k + 1) windows of size k initially store -1 for every window
        vector<int> result(n - k + 1, -1);
        // count of consecutive increasing elements
        int count = 1;
        // process the first window of size k
        for (int i = 1; i < k; i++) {
            // check if current element is exactly 1 greater than the previous element
            if (nums[i] == nums[i - 1] + 1) {
                count++;
            } else {
                // consecutive sequence is broken start counting again from current element
                count = 1;
            }
        }
        // if all k elements are consecutive the last element is the answer
        if (count == k) {
            result[0] = nums[k - 1];
        }
        // process remaining windows using sliding window
        int i = 1;
        int j = k;
        while (j < n) {
            // check if nums[j] continues the consecutive sequence
            if (nums[j] == nums[j - 1] + 1) {
                count++;
            } else {
                // sequence is broken start a new consecutive sequence
                count = 1;
            }
            // if we have at least k consecutive elements current window is valid
            if (count >= k) {
                // largest element of the window is nums[j]
                result[i] = nums[j];
            }
            // move the sliding window forward
            i++;
            j++;
        }
        // return the result for all windows
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)