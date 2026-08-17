// Brute Force Code
class Solution {
public:
    // find the duplicated and missing numbers in the given array
    vector<int> findErrorNums(vector<int>& nums) {
        // total number of elements
        int n = nums.size();
        // store the duplicate and missing numbers
        int duplicate = -1;
        int missing = -1;
        // find the duplicated number
        for (int i = 1; i <= n; i++) {
            // count how many times the current number appears
            int count = 0;
            for (int num : nums) {
                if (num == i) {
                    count++;
                }
            }
            // if the number appears twice it is the duplicate
            if (count == 2) {
                duplicate = i;
            }
        }
        // find the missing number
        for (int i = 1; i <= n; i++) {
            // assume the number is not present
            bool found = false;
            // search for the current number in the array
            for (int num : nums) {
                if (num == i) {
                    found = true;
                    break;
                }
            }
            // if the number is not found it is the missing number
            if (!found) {
                missing = i;
            }
        }
        // return duplicate and missing numbers
        return {duplicate, missing};
    }
};

// Time Complexity : O(N^2)
// Space Complexity : O(N)