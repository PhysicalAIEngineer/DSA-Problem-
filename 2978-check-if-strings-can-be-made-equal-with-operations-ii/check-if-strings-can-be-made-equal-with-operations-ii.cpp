// Brute Force Code & Optimal Code
class Solution {
public:
    bool checkStrings(string s1, string s2) {
        // store character frequencies for even indices 0, 2, 4, 6, ...
        vector<int> even(26, 0);
        // store character frequencies for odd indices 1, 3, 5, 7, ...
        vector<int> odd(26, 0);
        // length of the string
        int n = s1.length();
        // check every index in both strings
        for (int i = 0; i < n; i++) {
            // if index is even
            if (i % 2 == 0) {
                // add the character from s1 to the even-frequency array
                even[s1[i] - 'a']++;
                // subtract the character from s2 from the even-frequency array
                even[s2[i] - 'a']--;
            }
            // if index is odd
            else {
                // add the character from s1 to the odd-frequency array
                odd[s1[i] - 'a']++;
                // subtract the character from s2 from the odd-frequency array
                odd[s2[i] - 'a']--;
            }
        }
        // check the frequency difference for every character from 'a' to 'z'
        for (int i = 0; i < 26; i++) {
            // if any frequency is different s1 and s2 cannot be transformed into each other
            if (even[i] != 0 || odd[i] != 0) {
                return false;
            }
        }
        // all even-index characters and all odd-index characters have the same frequencies
        return true;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)