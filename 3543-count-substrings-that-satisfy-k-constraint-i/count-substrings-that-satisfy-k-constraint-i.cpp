// Brute Fore Code & Optimal Code
class Solution {
public:
    int countKConstraintSubstrings(string s, int k) {
        // length of the string
        int n = s.size();
        // total number of valid substrings
        int result = 0;
        // count of 0s and 1s in the current window
        int count0 = 0;
        int count1 = 0;
        // sliding window pointers
        int i = 0;
        int j = 0;
        // extend until the length of string
        while (j < n) {
            // add the current character to the window
            if (s[j] == '0') {
                count0++;
            } else {
                count1++;
            }
            // window is invalid only when count0 > k and count1 > k, so keep shrinking from the left
            while (count0 > k && count1 > k) {
                // remove s[i] from the window
                if (s[i] == '0') {
                    count0--;
                } else {
                    count1--;
                }
                // move left pointer forward
                i++;
            }
            // current window [i...j] is valid number of valid substrings ending at j = j - i + 1
            result += (j - i + 1);
            // move right pointer forward
            j++;
        }
        // return total number of valid substrings
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)