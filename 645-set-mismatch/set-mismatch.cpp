// Optimal Code
class Solution {
public:
    // return the duplicated number and the missing number
    vector<int> findErrorNums(vector<int>& nums) {
        // total number of elements
        int n = nums.size();
        // variables to store the missing and duplicate numbers
        int missing = 0;
        int duplicates = 0;
        // dictionary to map: number -> frequency
        unordered_map<int, int> mp;
        // count the frequency of every number in the array
        for (int x : nums) {
            mp[x]++;
        }
        // check every number from 1 to n
        for (int i = 1; i <= n; i++) {
            // if the number exists in the dictionary
            if (mp.count(i)) {
                // frequency of 2 means the number is duplicated
                if (mp[i] == 2) {
                    duplicates = i;
                }
            }
            else {
                // if the number is not present in the dictionary, it is missing
                missing = i;
            }
        }
        // return duplicate and missing number
        return {duplicates, missing};
    }
};

// Time Complexity : O(N)
// Space Complexity : O(1)