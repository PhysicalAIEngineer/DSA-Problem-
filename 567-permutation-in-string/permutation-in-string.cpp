// Brute Force Code & Optimal Code
class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        // length of s1 and s2
        int n = s1.size();
        int m = s2.size();
        // if s1 is larger than s2 its permutation cannot be present in s2
        if (n > m) {
            return false;
        }
        // frequency array for s1 frequency array for current window of s2
        vector<int> s1_freq(26, 0);
        vector<int> s2_freq(26, 0);
        // count frequency of every character in s1
        for (int i = 0; i < n; i++) {
            s1_freq[s1[i] - 'a']++;
        }
        // sliding window over s2
        int i = 0;  // left pointer
        int j = 0;  // right pointer
        while (j < m) {
            // add s2[j] to the current window
            s2_freq[s2[j] - 'a']++;
            // window size should always be n
            if (j - i + 1 > n) {
                // remove the leftmost character because the window became larger than n
                s2_freq[s2[i] - 'a']--;
                i++;
            }
            // if both frequency arrays are equal current window is a permutation of s1
            if (s1_freq == s2_freq) {
                return true;
            }
            // move right pointer forward
            j++;
        }
        // no permutation of s1 was found in s2
        return false;
    }
};

// Time Complexity : O(N)
// Space COmplexity : O(N)