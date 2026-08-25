// Brute Force Code & Optimal Code
class Solution {
public:
    void solve(int n, string curr, vector<string>& result) {
        // base case: if the current string reaches length n have constructed one complete happy string.
        if (curr.length() == n) {
            // store the completed happy string.
            result.push_back(curr);
            return;
        }
        // try each possible character in lexicographical order: 'a' -> 'b' -> 'c'
        for (char ch = 'a'; ch <= 'c'; ch++) {
            // happy string cannot contain the same character at two consecutive positions.
            if (!curr.empty() && curr.back() == ch) {
                continue;
            }
            // DO / CHOOSE
            // add the current character to the string.
            curr += ch;
            // EXPLORE
            // recursively choose the next character.
            solve(n, curr, result);
            // UNDO / BACKTRACK
            // remove the last character so that can try another possible character.
            curr.pop_back();
        }
    }
    string getHappyString(int n, int k) {
        // start with an empty string.
        string curr = "";
        // store all generated happy strings.
        vector<string> result;
        // generate every possible happy string of length n.
        solve(n, curr, result);
        // if fewer than k happy strings exist the k-th string does not exist.
        if (result.size() < k) {
            return "";
        }
        // characters are tried in the order 'a', 'b', 'c' so the generated strings are already in lexicographical order k is 1-based, while vector indices are 0-based so use k - 1.
        return result[k - 1];
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)