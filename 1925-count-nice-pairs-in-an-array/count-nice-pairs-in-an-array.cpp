// Brute Force Code & Optimal Code
class Solution {
public:
    // reverse the given number.
    int reverse(int num) {
        // store the reversed number.
        int reversed = 0;
        // reverse the number digit by digit.
        while (num > 0) {
            // last digit of num.
            int remainder = num % 10;
            // add the extracted digit to reversed.
            reversed = reversed * 10 + remainder;
            // remove the last digit from num.
            num /= 10;
        }
        // return the reversed number.
        return reversed;
    }
    int countNicePairs(vector<int>& nums) {
        // modulo value required by the problem.
        int mod = 1e9 + 7;
        // store the frequency of each transformed value.
        unordered_map<int, int> mp;
        // transform every number in nums.
        for (int i = 0; i < nums.size(); i++) {
            // calculate: nums[i] - reverse(nums[i])
            nums[i] = nums[i] - reverse(nums[i]);
        }
        // store the total number of nice pairs.
        long long result = 0;
        // process every transformed value.
        for (int i = 0; i < nums.size(); i++) {
            // every previous occurrence of the same transformed value forms a nice pair with the current value.
            result = (result + mp[nums[i]]) % mod;
            // add the current transformed value to the frequency map.
            mp[nums[i]]++;
        }
        // return the total number of nice pairs.
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)