// Brute Force Code & Optimal Code
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        // total number of elements in the array
        int n = nums.size();
        // set to store the elements currently inside the sliding window
        unordered_set<int> seen;
        // initialize the sliding window pointer
        int left = 0;
        int right = 0;
        // traverse the array using the right pointer
        while (right < n) {
            // if the window size becomes greater than k remove the leftmost element from the window
            if (abs(left - right) > k) {
                seen.erase(nums[left]);
                left++;
            }
            // if the current element already exists in the window nearby duplicate has been found
            if (seen.find(nums[right]) != seen.end()) {
                return true;
            }
            // add the current element to the sliding window
            seen.insert(nums[right]);
            // expand the window by moving the right pointer
            right++;
        }
        // no nearby duplicate exists
        return false;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)