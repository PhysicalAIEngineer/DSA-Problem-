// Brute Force Code & Optimal Code
class Solution {
public:
    int longestPalindrome(vector<string>& words) {
        // dictionary to store the frequency of words
        unordered_map<string, int> mp;
        // stores the maximum length of the palindrome
        int result = 0;
        // process every two-character word
        for (string &word : words) {
            // reverse the current word
            string reversedWord = word;
            reverse(reversedWord.begin(), reversedWord.end());
            // check if the reversed word is already available
            if (mp[reversedWord] > 0) {
                // one pair contains two words each word has 2 characters so, this pair adds 4 characters
                result += 4;
                // use one occurrence of the reversed word
                mp[reversedWord]--;
            }
            else {
                // no matching reversed word is available yet store the current word in the dictionary
                mp[word]++;
            }
        }
        // now check the remaining words that have the same two characters
        for (auto &it : mp) {
            // current word
            string word = it.first;
            // frequency of the current word
            int count = it.second;
            // Check whether both characters are the same
            if (word[0] == word[1] && count > 0) {
                // one center word contains 2 characters so, add 2 to the palindrome length
                result += 2;
                // only one equal-character word can be placed in the center
                break;
            }
        }
        // return the maximum length of the palindrome
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)