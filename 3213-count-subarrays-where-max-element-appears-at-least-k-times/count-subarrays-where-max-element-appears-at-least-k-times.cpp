// Brute Force Code & Optimal Code
class Solution {
public:
    long long countSubarrays(vector<int>& nums, int k) {
        // find the maximum element in the array
        int maxE = *max_element(nums.begin(), nums.end());
        // length of the array
        int n = nums.size();
        // left and right pointers of sliding window
        int i = 0;
        int j = 0;
        // total number of valid subarrays
        long long result = 0;
        // count of maximum elements in current window
        int countMax = 0;
        // expand window using j
        while (j < n) {
            // if current element is the maximum increase its count
            if (nums[j] == maxE) {
                countMax++;
            }
            // if window contains at least k maximum elements
            while (countMax >= k) {
                // every index from j to n-1 can be the ending point of a valid subarray
                result += n - j;
                // if nums[i] is maximum, remove it from the window
                if (nums[i] == maxE) {
                    countMax--;
                }
                // move left pointer forward
                i++;
            }
            // move right pointer forward
            j++;
        }
        // return total number of valid subarrays
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(1)