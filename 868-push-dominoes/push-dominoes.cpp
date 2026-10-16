// Brute Force Code & Optimal Code
class Solution {
public:
    string pushDominoes(string dominoes) {
        // add sentinel dominoes at both ends to simplify edge cases
        string s = "L" + dominoes + "R";
        // total length of the modified string
        int n = s.length();
        // list used to build the final answer
        string result = "";
        // initialize two pointers left -> previous non-standing domino
        int left = 0;
        // right -> next non-standing domino
        int right = 1;
        // traverse the modified string
        while (right < n) {
            // skip all standing dominoes
            if (s[right] == '.') {
                right++;
                continue;
            }
            // number of standing dominoes between two non-dot dominoes
            int middle_length = right - left - 1;
            // ignore the left sentinel 'L' when building the answer
            if (left > 0) {
                result += s[left];
            }
            // case 1: both ends push in the same direction
            if (s[left] == s[right]) {
                result += string(middle_length, s[left]);
            }
            // case 2: forces move away from each other all dominoes in the middle remain standing
            else if (s[left] == 'L' && s[right] == 'R') {
                result += string(middle_length, '.');
            }
            // case 3: forces move toward each other half fall right, half fall left and the middle domino stays upright if the count is odd
            else {
                result += string(middle_length / 2, 'R');
                result += string(middle_length % 2, '.');
                result += string(middle_length / 2, 'L');
            }
            // move the left pointer to the current non-standing domino
            left = right;
            right++;
        }
        // return the final domino configuration
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)