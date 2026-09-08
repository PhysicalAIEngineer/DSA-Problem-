// Brute Force Code & Optimal Code
class Solution {
public:
    int numberOfSpecialChars(string word) {
        // store the last position of each lowercase character
        // example: lastSmall[0] = last position of 'a'
        vector<int> lastSmall(26, -1);
        // store the first position of each uppercase character
        // example: firstCapital[0] = first position of 'A'
        vector<int> firstCapital(26, -1);
        // traverse every character in the word
        for (int i = 0; i < word.size(); i++) {
            // get the current character
            char ch = word[i];
            // if the character is lowercase
            if (islower(ch)) {
                // store its latest index
                // 'a' -> 0
                // 'b' -> 1
                // ...
                // 'z' -> 25
                lastSmall[ch - 'a'] = i;
            }
            // otherwise, the character is uppercase
            else {
                // store only the first occurrence of the uppercase character
                // example: if 'A' appears at index 3 store 3 and don't overwrite it later
                if (firstCapital[ch - 'A'] == -1) {
                    firstCapital[ch - 'A'] = i;
                }
            }
        }
        // store the number of special characters
        int count = 0;
        // check all 26 letters
        for (int i = 0; i < 26; i++) {
            // character is special if:
            // 1. Its lowercase version exists
            // 2. Its uppercase version exists
            // 3. The last lowercase occurrence comes before the first uppercase occurrence
            // Example:
            // word = "aaAb"
            // lastSmall['a'] = 1
            // firstCapital['A'] = 2
            // 1 < 2, so 'a' is special
            if (lastSmall[i] != -1 && firstCapital[i] != -1 && lastSmall[i] < firstCapital[i]) {
                // found one special character
                count++;
            }
        }
        // return the total number of special characters
        return count;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)