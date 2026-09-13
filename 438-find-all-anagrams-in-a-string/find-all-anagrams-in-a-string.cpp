// Brute Force Code & Optimal Code
class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        // frequency array to store the character counts of the pattern
        vector<int> count(26, 0);
        // length of the text and the pattern
        int m = s.size();
        int n = p.size();
        // store the frequency of each character in the pattern
        for (char ch : p) {
            count[ch - 'a']++;
        }
        // initialize the sliding window pointers
        int left = 0;
        int right = 0;
        // list to store the starting indices of all anagrams
        vector<int> result;
        // traverse the text using a sliding window
        while (right < m) {
            // include the current character in the window by decreasing its required frequency
            count[s[right] - 'a']--;
            // when the window size becomes equal to the pattern length
            if (right - left + 1 == n) {
                // if all frequencies are zero the current window is an anagram of the pattern
                if (count == vector<int>(26, 0)) {
                    result.push_back(left);
                }
                // remove the leftmost character from the window before sliding the window forward
                count[s[left] - 'a']++;
                // move left pointer forward
                left++;
            }
            // expand the window
            right++;
        }
        // return the list of starting indices
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)