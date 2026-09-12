// Brute Force Code & Optimal Code
class Solution {
public:
    vector<int> getAverages(vector<int>& nums, int k) {
        // number of elements in the array
        int n = nums.size();
        // if k = 0, the window contains only the current element
        if (k == 0) {
            return nums;
        }
        // initially every position is -1 because complete window may not exist
        vector<int> result(n, -1);
        // size of the window =  k elements on the left + centre element + k elements on the right
        int window_size = 2 * k + 1;
        // if the array is smaller than the required window no valid average can be calculated
        if (n < window_size) {
            return result;
        }
        // left boundary of the first window
        int left = 0;
        // right boundary of the first window
        int right = 2 * k;
        // centre of the first window
        int centre = k;
        // calculate the sum of the first window
        long long window_sum = 0;
        for (int i = left; i <= right; i++) {
            window_sum += nums[i];
        }
        // calculate and store the average for the first valid centre
        result[centre] = window_sum / window_size;
        // move the centre one position forward
        centre++;
        // move the right boundary one position forward
        right++;
        // continue sliding window until the right boundary reaches the end
        while (right < n) {
            // element that is leaving the current window
            int out_of_window = nums[left];
            // element that is entering the current window
            int came_to_window = nums[right];
            // remove the element leaving the window and add the new element entering the window
            window_sum = window_sum - out_of_window + came_to_window;
            // calculate the average for the new centre
            result[centre] = window_sum / window_size;
            // move the centre forward
            centre++;
            // move the left boundary forward
            left++;
            // move the right boundary forward
            right++;
        }
        // return all calculated averages
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)