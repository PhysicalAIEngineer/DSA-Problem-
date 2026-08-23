// Brute Force Code & Optimal Code
class Solution {
public:
    // return the total number of subarrays consisting only of zeros.
    long long zeroFilledSubarray(vector<int>& nums) {
        // store the total number of zero-filled subarrays.
        long long result = 0;
        // count consecutive zeros ending at the current index.
        long long countSubarrays = 0;
        // traverse every element in the array.
        for (int num : nums) {
            // if the current element is zero extend the consecutive zero sequence.
            if (num == 0) {
                countSubarrays++;
            }
            else {
                // otherwise, reset the consecutive zero count.
                countSubarrays = 0;
            }
            // every consecutive zero ending at the current index forms a new zero-filled subarray.
            result += countSubarrays;
        }
        // return the total number of zero-filled subarrays.
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(1)