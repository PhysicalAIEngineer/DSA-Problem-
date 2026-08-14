// Optimal Code [Using Sorting]
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // dictionary to map: sorted string -> list of anagrams
        unordered_map<string, vector<string>> mp;
        // traverse every string
        for (string str : strs) {
            // sort the characters of the string all anagrams produce the same sorted key
            string key = str;
            sort(key.begin(), key.end());
            // create a new group if the key does not already exist
            if (mp.find(key) == mp.end()) {
                mp[key] = {};
            }
            // add the original string to its corresponding group
            mp[key].push_back(str);
        }
        // store all anagram groups
        vector<vector<string>> result;
        // collect every group from the dictionary
        for (auto& pair : mp) {
            result.push_back(pair.second);
        }
        // return all grouped anagrams
        return result;
    }
};

// Time Complexity : O(Nlog)
// Space Complexity : O(N)