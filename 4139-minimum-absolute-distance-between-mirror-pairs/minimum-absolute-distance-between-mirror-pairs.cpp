// Brute Force Code & Optimal Code
class Solution {
public:
    int getReverse(int n) {
        // store the reversed numbers
        int reversed = 0;
        // continue until all digits are processed
        while (n > 0) {
            // get the last digit of n
            int rem = n % 10;
            // add the digit to the reversed numbers
            reversed = reversed * 10 + rem;
            // remove the last digit from n
            n /= 10;
        }
        // return the reversed numbers
        return reversed;
    }
    int minMirrorPairDistance(vector<int>& nums) {
        // store the length of the array
        int n = nums.size();
        // dictionary:
        // key   --> reversed values
        // value --> index where that value was found
        unordered_map<int, int> mp;
        // store the minimum distance found so far
        int result = INT_MAX;
        // traverse the array from left to right
        for (int i = 0; i < n; i++) {
            // if nums[i] is already present in the map it means some previous number has reversed values equal to nums[i]
            if (mp.find(nums[i]) != mp.end()) {
                // calculate the distance between the current index and previous index
                result = min(result, i - mp[nums[i]]);
            }
            // reverse the current number and store its index
            mp[getReverse(nums[i])] = i;
        }
        // if no mirror pair was found return -1 otherwise return the minimum distance
        return result == INT_MAX ? -1 : result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)