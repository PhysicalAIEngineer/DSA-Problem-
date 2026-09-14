// Brute Force Code & Optimal Code
class Solution {
public:
    int minimumLength(string s) {
        // length of the string
        int n = s.size();
        // two pointers
        // i --> starts from the left
        // j --> starts from the right
        int i = 0;
        int j = n - 1;
        // continue while left and right characters are same
        while (i < j && s[i] == s[j]) {
            // store the common character
            char ch = s[i];
            // remove all consecutive occurrences of this character from the left side
            while (i < j && s[i] == ch) {
                i++;
            }
            // remove all consecutive occurrences of this character from the right side
            while (j >= i && s[j] == ch) {
                j--;
            }
        }
        // remaining characters from i to j give the minimum possible length
        return j - i + 1;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)