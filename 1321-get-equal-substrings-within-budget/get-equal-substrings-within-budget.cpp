// Brute Force Code & Optimal Code
class Solution {
public:
    int equalSubstring(string s, string t, int maxCost) {
        // length of the strings
        int n = s.size();
        // maximum length of valid substring
        int maxLen = 0;
        // total cost of changing s to t for the current window
        int currCost = 0;
        // left and right pointers
        int i = 0;
        int j = 0;
        // expand window using j
        while (j < n) {
            // cost to change s[j] into t[j]
            currCost += abs(s[j] - t[j]);
            // if total cost exceeds maxCost shrink the window from the left
            while (currCost > maxCost) {
                // remove the cost of s[i] -> t[i]
                currCost -= abs(s[i] - t[i]);
                // move left pointer forward
                i++;
            }
            // current window is valid update maximum length
            maxLen = max(maxLen, j - i + 1);
            // move right pointer forward
            j++;
        }
        // return maximum possible length
        return maxLen;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)