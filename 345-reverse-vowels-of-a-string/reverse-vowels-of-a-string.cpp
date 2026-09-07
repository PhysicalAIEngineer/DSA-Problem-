// Brute Force Code & Optimal Code
class Solution {
public:
    // helper function to check whether a character is a vowel
    bool isVowel(char ch) {return ch == 'a' || ch == 'e' || ch == 'i' ||  ch == 'o' || ch == 'u' || ch == 'A' || ch == 'E' || ch == 'I' ||  ch == 'O' || ch == 'U';}
    string reverseVowels(string s) {
        // convert the string to a list of characters
        string character = s;
        // total number of characters
        int n = character.length();
        // initialize two pointers
        int left = 0;
        int right = n - 1;
        // continue until the pointers meet
        while (left < right) {
            // move the left pointer forward until it points to a vowel
            if (!isVowel(character[left])) {
                left++;
            }
            // move the right pointer backward until it points to a vowel
            else if (!isVowel(character[right])) {
                right--;
            }
            // both pointers are at vowels so swap them
            else {
                swap(character[left], character[right]);
                // move both pointers inward
                left++;
                right--;
            }
        }
        // return the modified string
        return character;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)