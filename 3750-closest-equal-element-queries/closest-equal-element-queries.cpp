// Brute Force Code & Optimal Code
class Solution {
public:
    vector<int> solveQueries(vector<int>& nums, vector<int>& queries) {
        // store the length of the array
        int n = nums.size();
        // dictionary:
        // key   -> element
        // value -> list of all indices where that element occurs
        unordered_map<int, vector<int>> mp;
        // store all positions of every element
        for (int i = 0; i < n; i++) {
            // if this element is not present in the dictionary create an empty list for it
            if (mp.find(nums[i]) == mp.end()) {
                mp[nums[i]] = {};
            }
            // store the current index
            mp[nums[i]].push_back(i);
        }
        // store answers for all queries
        vector<int> result;
        // process every query
        for (int qi : queries) {
            // get the element present at the query index
            int element = nums[qi];
            // get all indices where this element occurs
            vector<int>& vec = mp[element];
            // number of occurrences of this element
            int sz = vec.size();
            // if the element occurs only once there is no other occurrence to find
            if (sz == 1) {
                result.push_back(-1);
                continue;
            }
            // find the position of qi inside vec using binary search (lower_bound)
            int left = 0;
            int right = sz - 1;
            while (left <= right) {
                // find the middle position
                int mid = (left + right) / 2;
                // if vec[mid] is smaller than qi search on the right side
                if (vec[mid] < qi) {
                    left = mid + 1;
                }
                // otherwise, search on the left side
                else {
                    right = mid - 1;
                }
            }
            // left is the position of qi in vec
            int pos = left;
            // start with the largest possible distance
            int res = INT_MAX;
            // check the right neighbour get the next occurrence after qi % sz handles the circular case: if pos is the last occurrence it goes back to the first occurrence
            int rightIndex = vec[(pos + 1) % sz];
            // normal absolute distance
            int d = abs(qi - rightIndex);
            // circular distance from index 8 to index 1 through the circular path = 10 - 7 = 3
            int circularDist = n - d;
            // take the smaller of normal distance and circular distance
            res = min({res, d, circularDist});
            // check the left neighbour get the previous occurrence before qi + sz and % sz handles the circular case when pos is 0
            int leftIndex = vec[(pos - 1 + sz) % sz];
            // normal absolute distance
            d = abs(qi - leftIndex);
            // circular distance
            circularDist = n - d;
            // update the minimum distance
            res = min({res, d, circularDist});
            // store the minimum distance for this query
            result.push_back(res);
        }
        // return answers for all queries
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)