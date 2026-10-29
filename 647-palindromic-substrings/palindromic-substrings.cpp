// Brute Force Code & Optimal Code
class Solution {
public:
    // recursive function to check whether s[i...j] is a palindrome.
    // i -> starting index of the substring.
    // j -> ending index of the substring.
    // returns true if the substring is a palindrome otherwise returns false.
    bool check(string& s, int i, int j) {
        // base case: if i >= j, the two pointers have either:
        // 1. crossed each other (i > j), meaning no characters remain to be compared.
        // 2. met at the same position (i == j), meaning only one character remains.
        // an empty substring or a single-character substring is always considered a palindrome.
        if (i >= j) {
            return true;
        }
        // case 1: characters at both ends match.
        if (s[i] == s[j]) {
            // matching characters do not violate the palindrome property move the left pointer one position to the right and the right pointer one position to the left.
            // Recursively check whether the remaining inner substring is also a palindrome.
            return check(s, i + 1, j - 1);
        }
        // case 2: characters at both ends do not match substring cannot be a palindrome, so return false immediately without checking the inner characters.
        return false;
    }
    int countSubstrings(string s) {
        // calculate the length of the input string.
        int n = s.length();
        // initialize the counter it stores the total number of palindromic substrings.
        int count = 0;
        // generate all possible substrings the outer loop chooses the starting index i.
        for (int i = 0; i < n; i++) {
            // inner loop chooses the ending index j. and j starts from i because a substring's ending index cannot be smaller than its starting index.
            for (int j = i; j < n; j++) {
                // check whether the current substring s[i...j] is a palindrome.
                if (check(s, i, j)) {
                    // palindromic substring has been found increase the count by 1 every occurrence is counted separately even if multiple substrings contain identical characters.
                    count++;
                }
            }
        }
        // return the total number of palindromic substrings.
        return count;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)