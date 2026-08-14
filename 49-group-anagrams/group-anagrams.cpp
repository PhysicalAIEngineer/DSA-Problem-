// Optimal Code [Without Sorting]
class Solution {
public:
    // generate a canonical representation of a string using character frequencies
    string generate(string s) {
        // frequency array for characters 'a' to 'z'
        vector<int> count(26, 0);
        // count the frequency of each character
        for (char ch : s) {
            count[ch - 'a']++;
        }
        // build the canonical string from the frequency array
        string new_string;
        for (int i = 0; i < 26; i++) {
            // append each character according to its frequency
            if (count[i] > 0) {
                new_string.append(count[i], char(i + 'a'));
            }
        }
        // return the canonical string
        return new_string;
    }
    // group all anagrams together
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // dictionary to map: canonical string -> list of anagrams
        unordered_map<string, vector<string>> mp;
        // process every string
        for (string s : strs) {
            // generate the canonical key
            string key = generate(s);
            // create a new group if the key is not present
            if (mp.find(key) == mp.end()) {
                mp[key] = {};
            }
            // add the original string to its anagram group
            mp[key].push_back(s);
        }
        // store all grouped anagrams
        vector<vector<string>> result;
        // collect every group from the dictionary
        for (auto& pair : mp) {
            result.push_back(pair.second);
        }
        // return all anagram groups
        return result;
    }
};

// Time Complexity : O(N)
// Space Compelxity : O(N)