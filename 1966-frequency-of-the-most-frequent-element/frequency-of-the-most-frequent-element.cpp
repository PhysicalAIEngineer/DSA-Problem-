// Brute Force Code & Optimal Code
class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        // sort the array so we can increase smaller values up to the current largest value
        sort(nums.begin(), nums.end());
        // total number of elements
        int n = nums.size();
        // store maximum frequency found
        int result = 0;
        // left pointer of sliding window
        int i = 0;
        // sum of elements inside current window
        long long currSum = 0;
        // expand window using right pointer j
        for (int j = 0; j < n; j++) {
            // current largest value in the window
            long long target = nums[j];
            // add current element to window sum
            currSum += nums[j];
            // cost to make every element in the window equal to target required = (number of elements * target) - current sum
            if (1LL * (j - i + 1) * target - currSum > k) {
                // window needs more than k operations so remove the leftmost element
                currSum -= nums[i];
                i++;
            }
            // update maximum valid window size
            result = max(result, j - i + 1);
        }
        // return maximum possible frequency
        return result;
    }
};

// Time Complexity : O(NlogN)
// Space Complexity : O(1)