// Brute Force Code & Optimal Code
class Solution {
public:
    int minimumDistance(vector<int>& nums) {
        // store the length of the array
        int n = nums.size();
        // dictionary to store the indices of each number
        unordered_map<int, vector<int>> mp;
        // store the minimum distance found start with infinity because we have not found any valid triplet yet
        int result = INT_MAX;
        // traverse every index
        for (int k = 0; k < n; k++) {
            // if this number is appearing for the first time create an empty vector to store its indices
            if (mp.find(nums[k]) == mp.end()) {
                mp[nums[k]] = {};
            }
            // store the current index of this number
            mp[nums[k]].push_back(k);
            // need at least 3 occurrences of the same number to form a valid triplet
            if (mp[nums[k]].size() >= 3) {
                // get all indices where the current number appeared
                vector<int>& vec = mp[nums[k]];
                // number of occurrences of this number
                int siz = vec.size();
                // get the third-last occurrence
                int i = vec[siz - 3];
                // update the minimum distance between the first and third index
                result = min(result, k - i);
            }
        }
        // if result is still infinity no number appeared at least 3 times
        if (result == INT_MAX) {
            return -1;
        }
        // required distance is 2 times the difference between the first and third index
        return 2 * result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)