// Brute Force Code & Optimal Code
class Solution {
public:
    int solve(string& s, int idx, unordered_set<string>& st,
              int currCount, int maxCount) {
        // pruning: currently at index idx, there are (s.length() - idx) characters remaining in the best possible case, every remaining character can become a separate unique substring therefore, this is the maximum number of new substrings can still create.
        if (currCount + (s.length() - idx) <= maxCount) {
            return maxCount;
        }
        // base case: if idx reaches the end of the string the entire string has been split successfully.
        if (idx == s.length()) {
            // update the maximum number of unique substrings found so far.
            return max(maxCount, currCount);
        }
        // try every possible substring starting from idx try every possible ending position j.
        for (int j = idx; j < s.length(); j++) {
            // create the substring from idx to j.
            string sub = s.substr(idx, j - idx + 1);
            // choose this substring only if it has not already been used in the current partition.
            if (st.find(sub) == st.end()) {
                // choose add the substring to the set of used substrings.
                st.insert(sub);
                // recursively split the remaining part of the string j + 1 -> first index after the selected substring currCount + 1 -> selected one new unique substring.
                maxCount = solve(s, j + 1, st, currCount + 1, maxCount);
                // backtrack remove the substring so that it can be considered again in a different branch.
                st.erase(sub);
            }
        }
        // return the best answer found from this state.
        return maxCount;
    }
    int maxUniqueSplit(string s) {
        // store all substrings currently used in the current partition unordered_set provides fast lookup.
        unordered_set<string> st;
        // store the maximum number of unique substrings found so far.
        int maxCount = 0;
        // number of substrings selected so far.
        int currCount = 0;
        // start backtracking from index 0.
        maxCount = solve(s, 0, st, currCount, maxCount);
        // return the maximum number of unique substrings.
        return maxCount;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)