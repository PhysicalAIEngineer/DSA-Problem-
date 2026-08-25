// Brute Force Code & Optimal Code
class Solution {
public:
    // store the final answer.
    string result = "";
    bool isSubsequence(string& s, string& sub, int k) {
        // pointer for traversing string s.
        int i = 0;
        // pointer for counting how many characters of sub * k have been matched.
        int j = 0;
        // length of the candidate subsequence.
        int L = sub.length();
        // length of the original string.
        int n = s.length();
        // check whether sub repeated k times can be formed as a subsequence of s.
        while (i < n && j < k * L) {
            // candidate string is repeated k times j % L gives the position inside sub.
            // Example:
            // sub = "abc"
            // j = 0 -> sub[0] -> 'a'
            // j = 1 -> sub[1] -> 'b'
            // j = 2 -> sub[2] -> 'c'
            // j = 3 -> sub[0] -> 'a'
            if (s[i] == sub[j % L]) {
                // current character matched.
                j++;
            }
            // move to the next character of s.
            i++;
        }
        // if all k copies of sub were matched then sub repeated k times is a subsequence of s.
        return j == k * L;
    }
    bool backtracking(string& s, string& curr, vector<bool>& canUse,vector<int>& requiredFreq, int k, int maxLen
    ) {
        // if the candidate has reached the required length check whether it can be repeated k times as a subsequence of s.
        if (curr.length() == maxLen) {
            // check whether curr * k is a subsequence of s.
            if (isSubsequence(s, curr, k)) {
                // store the valid candidate.
                result = curr;
                // valid answer has been found.
                return true;
            }
            // candidate is not valid.
            return false;
        }
        // try characters from 'z' down to 'a' important because we want the lexicographically largest answer.
        for (int i = 25; i >= 0; i--) {
            // skip the character if:
            // 1. it does not appear at least k times.
            // 2. already used all allowed copies of this character.
            if (!canUse[i] || requiredFreq[i] == 0) {
                continue;
            }
            // convert the index back to a character.
            // 0  -> 'a'
            // 1  -> 'b'
            // ...
            // 25 -> 'z'
            char ch = char('a' + i);
            // DO / CHOOSE
            // add the current character to the candidate.
            curr += ch;
            // use one available copy of this character.
            requiredFreq[i]--;
            // EXPLORE
            // continue building the candidate.
            if (backtracking(s, curr, canUse, requiredFreq, k, maxLen)) {
                // valid answer was found.
                return true;
            }
            // UNDO / BACKTRACK
            // remove the last chosen character.
            curr.pop_back();
            // restore the available frequency.
            requiredFreq[i]++;
        }
        // no valid candidate could be created from this state.
        return false;
    }
    string longestSubsequenceRepeatedK(string s, int k) {
        // length of the original string.
        int n = s.length();
        // frequency of every character from 'a' to 'z'.
        vector<int> freq(26, 0);
        // count how many times each character appears in s.
        for (char ch : s) {
            // convert character to an index:
            // 'a' -> 0
            // 'b' -> 1
            // ...
            // 'z' -> 25
            int index = ch - 'a';
            // increase the character frequency.
            freq[index]++;
        }
        // canUse[i] tells whether character i appears at least k times in s.
        vector<bool> canUse(26, false);
        // requiredFreq[i] tells the maximum number of times character i can appear in the candidate.
        vector<int> requiredFreq(26, 0);
        // process every character.
        for (int i = 0; i < 26; i++) {
            // character must appear at least k times to appear once in a subsequence repeated k times.
            if (freq[i] >= k) {
                // this character can be used.
                canUse[i] = true;
                // if a character appears freq[i] times it can appear at most freq[i] / k times in the candidate subsequence.
                // Example:
                // freq['a'] = 7
                // k = 3
                // maximum number of 'a' in answer:
                // 7 / 3 = 2
                requiredFreq[i] = freq[i] / k;
            }
        }
        // answer repeated k times must fit inside s. therefore, the maximum possible length of the candidate is n / k.
        int maxLen = n / k;
        // try candidate lengths from largest to smallest first valid length is automatically the maximum possible length.
        for (int length = maxLen; length >= 0; length--) {
            // backtracking modifies requiredFreq so create a fresh copy for each length.
            vector<int> tempRequiredFreq = requiredFreq;
            // start building a new candidate string.
            string curr = "";
            // try to construct a valid candidate of the current length.
            if (backtracking(s, curr, canUse, tempRequiredFreq, k, length)) {
                // because:
                // 1. try longer lengths first.
                // 2. try characters from 'z' to 'a'.
                // first valid answer is therefore the longest and lexicographically largest.
                return result;
            }
        }
        // if no non-empty candidate was found return the empty string.
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)