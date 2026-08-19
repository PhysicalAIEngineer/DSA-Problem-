// Optimal Code
class Solution {
public:
    // return the index with the minimum average difference
    int minimumAverageDifference(vector<int>& nums) {
        // total number of elements
        int n = nums.size();
        // calculate the total sum of all elements
        long long total_sum = 0;
        for (int num : nums) {
            total_sum += num;
        }
        // running sum of the left part
        long long left_sum = 0;
        // running sum of the right part
        long long right_sum = 0;
        // store the smallest average difference found so far
        long long min_diff = LLONG_MAX;
        // store the index with the minimum average difference
        int result_index = 0;
        // traverse every index as the split point
        for (int i = 0; i < n; i++) {
            // include the current element in the left part
            left_sum += nums[i];
            // remaining elements belong to the right part
            right_sum = total_sum - left_sum;
            // number of elements in the left part
            int left_count = i + 1;
            // number of elements in the right part
            int right_count = n - left_count;
            // compute the integer average of the left part
            long long left_avg = left_sum / left_count;
            // compute the integer average of the right part if the right part is empty, its average is 0
            long long right_avg = 0;
            if (i != n - 1) {
                right_avg =
                    right_sum / right_count;
            }
            // compute the absolute difference between the two averages
            long long diff = abs(left_avg - right_avg);
            // update the minimum difference and index
            if (diff < min_diff) {
                min_diff = diff;
                result_index = i;
            }
        }
        // return the index with the minimum average difference
        return result_index;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)