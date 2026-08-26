// Brute Force Code & Optimal Code
class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        // dictionary to store the frequency of every number in the array.
        unordered_map<int, int> mp;
        // count how many times each number appears.
        for (int x : arr) {
            // if x already exists in the map increase its frequency by 1. otherwise, its default frequency is 0 and then we add 1.
            mp[x]++;
        }
        // set to store frequencies that have been seen set is used because it does not allow duplicates.
        unordered_set<int> st;
        // check the frequency of every distinct number.
        for (auto& [x, freq] : mp) {
            // if this frequency already exists in the set then two different numbers have the same number of occurrences.
            if (st.find(freq) != st.end()) {
                // occurrences are not unique.
                return false;
            }
            // store the current frequency so that can detect it if another number has the same frequency.
            st.insert(freq);
        }
        // no duplicate frequency was found therefore, every number has a unique number of occurrences.
        return true;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)