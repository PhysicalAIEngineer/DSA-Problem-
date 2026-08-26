// Brute Force Code & Optimal Code
class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        // dictionary to store the frequency of each number in the array
        unordered_map<int, int> mp;
        // count how many times each number appears
        for (int num : nums) {
            // if num is already present increase its frequency by 1 otherwise start its frequency at 1
            mp[num]++;
        }
        // store the total number of good pairs
        int result = 0;
        // check every distinct number
        for (auto& [num, count] : mp) {
            // if a number appears count times choose any 2 occurrences to form a pair
            result += (count * (count - 1)) / 2;
        }
        // return the total number of pairs where both indices contain the same value
        return result;
    }
};

// Time Complexity : O(N)
// Space Comlexity : O(1)