// Brute Force Code & Optimal Code
class Solution {
public:
    // store all valid sentences
    vector<string> result;
    // store all dictionary words
    unordered_set<string> dict;
    void solve(int i, string currSentence, string& s) {
        // if have reached the end of the string the current sentence is complete.
        if (i >= s.length()) {
            result.push_back(currSentence);
            return;
        }
        // try every possible ending position for the current word.
        for (int j = i; j < s.length(); j++) {
            // create the substring from index i to j.
            string tempWord = s.substr(i, j - i + 1);
            // check whether the current substring exists in the dictionary.
            if (dict.find(tempWord) != dict.end()) {
                // save the original sentence so that it can be restored after recursion.
                string origSentence = currSentence;
                // add a space if the sentence already contains a word.
                if (!currSentence.empty()) {
                    currSentence += " ";
                }
                // add the current dictionary word.
                currSentence += tempWord;
                // recursively process the remaining part of the string.
                solve(j + 1, currSentence, s);
                // backtrack and restore the sentence to its previous state.
                currSentence = origSentence;
            }
        }
    }
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        // convert the word dictionary into for fast word lookup.
        for (string word : wordDict) {
            dict.insert(word);
        }
        // store the current sentence.
        string currSentence = "";
        // start backtracking from index 0.
        solve(0, currSentence, s);
        // return all possible valid sentences.
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)