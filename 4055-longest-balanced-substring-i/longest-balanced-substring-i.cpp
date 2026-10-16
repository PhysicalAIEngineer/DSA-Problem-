// Brute Force Code & Optimal Code
class Solution {
public:
    // check whether all characters appearing in the substring have the same frequency
    bool checkBalanced(vector<int>& frequency) {
        // store the common non-zero frequency
        int common = 0;
        // traverse the frequency array
        for (int i = 0; i < 26; i++) {
            // ignore characters that do not appear
            if (frequency[i] == 0) {
                continue;
            }
            // store the first non-zero frequency as the reference
            if (common == 0) {
                common = frequency[i];
            }
            // if any non-zero frequency differs, the substring is not balanced
            else if (frequency[i] != common) {
                return false;
            }
        }
        // all non-zero frequencies are equal
        return true;
    }
    int longestBalanced(string s) {
        // total number of characters in the string
        int n = s.length();
        // store the maximum balanced substring length
        int maximum_length = 0;
        // try every possible starting index
        for (int left = 0; left < n; left++) {
            // frequency array for the current substring
            vector<int> frequency(26, 0);
            // extend the substring one character at a time
            for (int right = left; right < n; right++) {
                // update the frequency of the newly added character
                frequency[s[right] - 'a']++;
                // if the substring is balanced, update the answer
                if (checkBalanced(frequency)) {
                    maximum_length = max(maximum_length, right - left + 1);
                }
            }
        }
        // return the length of the longest balanced substring
        return maximum_length;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)