// Optimal Code
class Solution {
public:
    // return the number of subarrays whose sum is divisible by k
    int subarraysDivByK(vector<int>& nums, int k) {
        // dictionary to store: remainder -> frequency
        unordered_map<int, int> remainder_frequency;
        // running prefix sum
        long long prefix_sum = 0;
        // prefix sum with remainder 0 exists before the array starts
        remainder_frequency[0] = 1;
        // store the total number of valid subarrays
        int result = 0;
        // traverse every element in the array
        for (int num : nums) {
            // update the running prefix sum
            prefix_sum += num;
            // compute the remainder when divided by k
            int remainder = prefix_sum % k;
            // adjust negative remainders
            if (remainder < 0) {
                remainder += k;
            }
            // if this remainder has appeared before, every previous occurrence forms a subarray whose sum is divisible by k
            if (remainder_frequency.count(remainder)) {
                result += remainder_frequency[remainder];
            }
            // record the current remainder
            remainder_frequency[remainder]++;
        }
        // return the total number of valid subarrays
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(1)