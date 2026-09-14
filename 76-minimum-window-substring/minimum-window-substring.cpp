// Brute Force Code & Optimal Code
class Solution {
public:
    string minWindow(string s, string t) {
        // length of string s
        int n = s.size();
        // frequency map for characters of t
        unordered_map<char, int> mp;
        // store frequency of every character required from t
        for (char ch : t) {
            mp[ch]++;
        }
        // total number of characters still required
        int requiredCount = t.size();
        // sliding window pointers
        int i = 0;
        int j = 0;
        // starting index of the minimum window
        int minStart = 0;
        // length of the minimum valid window
        int minWindow = INT_MAX;
        // expand the window using j
        while (j < n) {
            char ch_j = s[j];
            // if this character is still required decrease the number of required characters
            if (mp[ch_j] > 0) {
                requiredCount--;
            }
            // decrease its frequency in the map negative value means we have extra copies
            mp[ch_j]--;
            // if all characters of t are present try to shrink the window from the left
            while (requiredCount == 0) {
                // update minimum window if current window is smaller
                if (minWindow > j - i + 1) {
                    minWindow = j - i + 1;
                    minStart = i;
                }
                // character leaving the window
                char ch_i = s[i];
                // restore its frequency
                mp[ch_i]++;
                // if frequency becomes positive this character is now missing from the window
                if (mp[ch_i] > 0) {
                    requiredCount++;
                }
                // move left pointer forward
                i++;
            }
            // move right pointer forward
            j++;
        }
        // if no valid window was found
        if (minWindow == INT_MAX) {
            return "";
        }
        // return the minimum window substring
        return s.substr(minStart, minWindow);
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)