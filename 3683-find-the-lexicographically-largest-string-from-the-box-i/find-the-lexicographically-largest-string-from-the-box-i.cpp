// Brute Force Code & Optimal Code
class Solution {
public:
    // find the starting index of the lexicographically largest suffix
    int bestStartingPoint(string word, int n) {
        // current best starting index
        int i = 0;
        // candidate starting index
        int j = 1;
        // compare suffixes until all candidates have been processed
        while (j < n) {
            int k = 0;
            // skip matching characters while both suffixes are equal
            while (j + k < n && word[i + k] == word[j + k]) {
                k++;
            }
            // if the suffix starting at j is lexicographically larger update the best starting index
            if (j + k < n && word[j + k] > word[i + k]) {
                i = j;
                j++;
            }
            // otherwise, skip suffixes that have already been compared
            else {
                j = j + k + 1;
            }
        }
        // return the best starting position
        return i;
    }
    string answerString(string word, int numFriends) {
        // total number of characters
        int n = word.length();
        // if there is only one friend, return the whole string
        if (numFriends == 1) {
            return word;
        }
        // find the starting index of the lexicographically largest suffix
        int start = bestStartingPoint(word, n);
        // maximum possible length of a substring in a valid split
        int longest_possible_length = n - (numFriends - 1);
        // actual number of characters to take without exceeding the string
        int characters_to_take = min(longest_possible_length, n - start);
        // return the required substring
        return word.substr(start, characters_to_take);
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)