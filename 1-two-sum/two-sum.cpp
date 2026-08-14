// Optimal Code
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // dictionary to store: number -> index
        unordered_map<int, int> mp;
        // Traverse the array
        for (int i = 0; i < nums.size(); i++) {
            // calculate the number needed to reach the target
            int complement = target - nums[i];
            // if the complement has already been seen return its index and the current index
            if (mp.find(complement) != mp.end()) {
                return {mp[complement], i};
            }
            // store the current number along with its index
            mp[nums[i]] = i;
        }
        // no valid pair found
        return {};
    }
};

// Time Complexity : O(N)
// Space Complexity : O(1)