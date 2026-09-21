// Brute Force Code & Optimal Code
class Solution {
public:
    int solve(int start, int end, string& word, int k) {
        // count total complete substrings
        int result = 0;
        // try having 1 to 26 different characters
        for (int chars = 1; chars <= 26; chars++) {
            // minimum length required = chars * k if segment is smaller, no need to continue
            if (chars * k > end - start + 1) {
                break;
            }
            // frequency of each character in current window
            vector<int> count(26, 0);
            // number of characters whose frequency is exactly k
            int goodChars = 0;
            // start of sliding window
            int i = start;
            // window must contain exactly chars characters each appearing k times
            int windowLength = chars * k;
            // expand the window using j
            for (int j = start; j <= end; j++) {
                // current character
                char ch = word[j];
                // increase frequency of current character
                count[ch - 'a']++;
                // if frequency becomes exactly k this character becomes a good character
                if (count[ch - 'a'] == k) {
                    goodChars++;
                }
                // if frequency becomes k + 1 it is no longer a good character
                else if (count[ch - 'a'] == k + 1) {
                    goodChars--;
                }
                // if window becomes larger than required size remove the leftmost character
                if (j - i + 1 > windowLength) {
                    // character leaving the window
                    char leftChar = word[i];
                    // check frequency before removing
                    if (count[leftChar - 'a'] == k) {
                        goodChars--;
                    }
                    // if frequency was k + 1 after removing one it becomes k
                    else if (count[leftChar - 'a'] == k + 1) {
                        goodChars++;
                    }
                    // remove leftmost character from window
                    count[leftChar - 'a']--;
                    // move window start forward
                    i++;
                }
                // if exactly 'chars' characters have frequency k current window is a complete substring
                if (goodChars == chars) {
                    result++;
                }
            }
        }
        // return number of complete substrings
        return result;
    }
    int countCompleteSubstrings(string word, int k) {
        // length of the string
        int n = word.size();
        // total answer
        int result = 0;
        // start of current valid segment
        int last = 0;
        // find continuous segments satisfying difference between adjacent characters <= 2
        for (int i = 1; i <= n; i++) {
            // if we reach the end or adjacent characters differ by more than 2
            if (i == n || abs(word[i] - word[i - 1]) > 2) {
                // process the current valid segment
                result += solve(last, i - 1, word, k);
                // start a new valid segment
                last = i;
            }
        }
        // return total complete substrings
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)