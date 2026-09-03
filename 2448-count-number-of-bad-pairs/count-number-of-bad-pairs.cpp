// Brute Force Code & Optimal Code
class Solution {
public:
    long long countBadPairs(vector<int>& nums) {
        // store the number of elements
        int n = nums.size();
        // stores the total number of bad pairs
        long long result = 0;
        // transform every element nums[i] = nums[i] - i this transformation helps us identify good pairs
        for (int i = 0; i < n; i++) {
            nums[i] = nums[i] - i;
        }
        // map to store the frequency of each transformed value seen so far
        unordered_map<int, int> mp;
        // store the first transformed value because there are no previous elements for i = 0
        mp[nums[0]] = 1;
        // process every element starting from index 1
        for (int j = 1; j < n; j++) {
            // count how many previous elements have the same transformed value as nums[j] these elements form good pairs with j
            long long countOfNumsj = mp[nums[j]];
            // there are exactly j elements before index j because their indices are 0, 1, ..., j - 1
            long long totalNumsBeforej = j;
            // previous elements with a different transformed value form bad pairs with index j
            long long badPairs = totalNumsBeforej - countOfNumsj;
            // add the bad pairs found for this index
            result += badPairs;
            // add the current transformed value to the frequency map
            mp[nums[j]]++;
        }
        // return the total number of bad pairs
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)