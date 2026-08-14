// Optimal Code
class Solution {
public:
    vector<int> findOriginalArray(vector<int>& changed) {
        // total number of elements
        int n = changed.size();
        // valid doubled array must have an even number of elements
        if (n % 2 != 0) {
            return {};
        }
        // sort the array so that smaller numbers are processed first
        sort(changed.begin(), changed.end());
        // dictionary to map: number -> frequency
        unordered_map<int, int> mp;
        // count the frequency of every number
        for (int num : changed) {
            mp[num]++;
        }
        // store the reconstructed original array
        vector<int> result;
        // process the numbers in sorted order
        for (int num : changed) {
            // skip numbers that have already been paired
            if (mp[num] == 0) {
                continue;
            }
            // double of the current number
            int twice = 2 * num;
            // if the double does not exist or has already been used the array is invalid
            if (mp.find(twice) == mp.end() || mp[twice] == 0) {
                return {};
            }
            // add the current number to the original array
            result.push_back(num);
            // use one occurrence of the number and one occurrence of its double
            mp[num]--;
            mp[twice]--;
        }
        // return the recovered original array
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)