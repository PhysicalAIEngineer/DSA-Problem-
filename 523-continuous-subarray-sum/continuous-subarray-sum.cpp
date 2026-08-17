// Brute Force Code & Optimal Code
class Solution {
public:
    // check if there exists a continuous subarray of length at least 2 whose sum is a multiple of k
    bool checkSubarraySum(vector<int>& nums, int k) {
        // total number of elements
        int n = nums.size();
        // cictionary to map: remainder -> first index where it appeared
        unordered_map<int, int> mp;
        // remainder 0 is assumed to occur before the array starts this helps handle subarrays that begin at index 0.
        mp[0] = -1;
        // running prefix sum
        long long prefix_sum = 0;
        // traverse every element
        for (int i = 0; i < n; i++) {
            // update the prefix sum
            prefix_sum += nums[i];
            // compute the remainder when the prefix sum is divided by k
            int remainder = prefix_sum % k;
            // if this remainder has already appeared before
            if (mp.count(remainder)) {
                // subarray between the previous occurrence and the current index has a sum divisible by k check that its length is at least 2.
                if (i - mp[remainder] >= 2) {
                    return true;
                }
            }
            else {
                // store only the first occurrence of each remainder because it gives the longest possible subarray
                mp[remainder] = i;
            }
        }
        // no valid subarray was found
        return false;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)