// Brute Force Code
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // store the total number of elements
        int n = nums.size();
        // try every possible first element
        for (int i = 0; i < n; i++) {
            // pair it with every element that comes after it
            for (int j = i + 1; j < n; j++) {
                // check whether the current pair adds up to the target
                if (nums[i] + nums[j] == target) {
                    // return the indices of the matching pair
                    return {i, j};
                }
            }
        }
        // return an empty vector if no pair is found
        return {};
    }
};

// Time Complexity : O(N^2)
// Space Complexity : O(N)