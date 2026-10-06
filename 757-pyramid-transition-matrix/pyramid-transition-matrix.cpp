// Brute Force Code & Optimal Code
class Solution {
public:
    // memoization dictionary stores whether a particular state is possible or not
    unordered_map<string, bool> t;
    bool solve(string current, unordered_map<string, vector<char>>& mp, int idx, string above) {
        // if only one character is left the pyramid is successfully formed
        if (current.size() == 1) {
            return true;
        }
        // create a unique key for the current state
        // 1. current --> current row
        // 2. idx --> current position
        // 3. above --> row being constructed
        string key = current + "_" + to_string(idx) + "_" + above;
        // if this state was already calculated return the stored result
        if (t.find(key) != t.end()) {
            return t[key];
        }
        // current row is completely processed move to the next row
        if (idx == current.size() - 1) {
            t[key] = solve(above, mp, 0, "");
            return t[key];
        }
        // take two adjacent blocks from current row
        // example: current = "BCD", idx = 0, pair = "BC"
        string pair = current.substr(idx, 2);
        // if this pair cannot produce any character pyramid cannot be formed
        if (mp.find(pair) == mp.end()) {
            t[key] = false;
            return false;
        }
        // try every possible character that can be placed above this pair
        for (char character : mp[pair]) {
            // do: add the selected character to the next row
            above += character;
            // explore: recursively continue building the current row
            if (solve(current, mp, idx + 1, above)) {
                t[key] = true;
                return true;
            }
            // undo: remove the last character and try another possibility
            above.pop_back();
        }
        // none of the possible characters worked
        t[key] = false;
        return false;
    }
    bool pyramidTransition(string bottom, vector<string>& allowed) {
        // map each pair to all possible characters that can be placed above it
        unordered_map<string, vector<char>> mp;
        // build mapping from allowed patterns
        for (string& pattern : allowed) {
            // first two characters form the pair
            string pair = pattern.substr(0, 2);
            // third character can be placed above the pair
            char character = pattern[2];
            // create a list for this pair if not present
            if (mp.find(pair) == mp.end()) {
                mp[pair] = {};
            }
            // add possible character for this pair
            mp[pair].push_back(character);
        }
        // clear memoization for a fresh call
        t.clear();
        // start building the pyramid from the bottom row
        return solve(bottom, mp, 0, "");
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)