// Brute Force Code & Optimal Code
class Solution {
public:
    // check whether the given character is a lowercase vowel
    bool isVowel(char ch) {
        return (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u');
    }
    int maxVowels(string s, int k) {
        // total number of characters in the string
        int n = s.size();
        // variable to store the maximum number of vowels found in any window of size k
        int maximum_vowels = 0;
        // variable to store the number of vowels in the current window
        int count = 0;
        // sliding window pointers
        int left = 0;
        int right = 0;
        // traverse the string
        while (right < n) {
            // include the current character in the sliding window
            if (isVowel(s[right])) {
                count++;
            }
            // when the window size becomes exactly k
            if (right - left + 1 == k) {
                // update the maximum vowel count
                maximum_vowels = max(maximum_vowels, count);
                // remove the leftmost character from the current window
                if (isVowel(s[left])) {
                    count--;
                }
                // shrink the window
                left++;
            }
            // expand the window
            right++;
        }
        // return the maximum number of vowels in any window
        return maximum_vowels;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)