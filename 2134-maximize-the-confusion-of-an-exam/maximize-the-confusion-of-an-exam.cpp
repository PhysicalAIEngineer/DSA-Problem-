// Brute Force Code & Optimal Code
class Solution {
public:
    int maxConsecutiveAnswers(string answerkey, int k) {
        // variable to store the maximum valid window length
        int result = k;
        // dictionary to store the frequency of "T" and "F" in the current window
        unordered_map<char, int> frequency;
        // left pointer of the sliding window
        int left = 0;
        // traverse the string using the right pointer
        for (int right = 0; right < answerkey.size(); right++) {
            // include the current character in the sliding window
            char current = answerkey[right];
            frequency[current]++;
            // shrink the window while more than k flips are required
            while (min(frequency['T'], frequency['F']) > k) {
                // remove the leftmost character from the current window
                frequency[answerkey[left]]--;
                // move the left pointer to shrink the window
                left++;
            }
            // update the maximum valid window length
            result = max(result, right - left + 1);
        }
        // return the maximum number of consecutive equal answers
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)