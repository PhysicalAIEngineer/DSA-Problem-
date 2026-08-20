// Brute Force Code & Optimal Code
class Solution {
public:
    // store the length of the string
    int n = 0;
    // check whether s[l...r] is a palindrome.
    // use two pointers:
    // l -> starts from the left
    // r -> starts from the right
    // move both pointers toward the center.
    bool isPalindrome(string& s, int l, int r) {
        while (l < r) {
            // if the characters on the two sides are different the substring is not a palindrome.
            if (s[l] != s[r]) {
                return false;
            }
            // move the left pointer toward the center.
            l++;
            // move the right pointer toward the center.
            r--;
        }
        // all corresponding characters matched so the substring is a palindrome.
        return true;
    }
    void backtrack(string& s, int idx, vector<string>& curr,vector<vector<string>>& result) {
        // base case: if idx reaches the end of the string the entire string has been partitioned.
        if (idx == n) {
            // store a copy of the current partition result.push_back(curr) stores a copy because curr will be modified later during backtracking.
            result.push_back(curr);
            return;
        }
        // try every possible ending position current substring starts at idx try ending it at: idx, idx + 1, idx + 2, ..., n - 1
        for (int i = idx; i < n; i++) {
            // check whether s[idx...i] is a palindrome only palindrome substrings can be included in the current partition.
            if (isPalindrome(s, idx, i)) {
                // choose the palindrome substring.
                curr.push_back(s.substr(idx, i - idx + 1));
                // explore the remaining string next substring must start from i + 1 because s[idx...i] has already been selected.
                backtrack(s, i + 1, curr, result);
                // backtrack remove the last selected substring so that can try another partition.
                curr.pop_back();
            }
        }
    }
    vector<vector<string>> partition(string s) {
        // store the length of the string.
        n = s.length();
        // store all valid palindrome partitions.
        vector<vector<string>> result;
        // store the current partition being constructed.
        vector<string> curr;
        // start backtracking from index 0.
        backtrack(s, 0, curr, result);
        // return all possible palindrome partitions.
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)