// Brute Force Code & Optimal Code
class Solution {
public:
    // store the total number of words
    int n = 0;
    // store the maximum score found so far initially, no valid selection has been processed so use negative infinity.
    int maxScore = INT_MIN;
    void solve(int i, vector<int>& score, vector<string>& words, int currScore,vector<int>& freq) {
        // update the maximum score every point during the recursion represents a valid selection of some words.
        maxScore = max(maxScore, currScore);
        // base case: if all words have been processed there are no more choices to make.
        if (i >= n) {
            return;
        }
        // rry taking words[i] make a copy of the available letter frequencies because we modify this copy while checking whether the current word can be formed.
        vector<int> tempFreq = freq;
        // pointer used to process each character of the current word.
        int j = 0;
        // store the score of the current word
        int tempScore = 0;
        // check whether words[i] can be formed
        while (j < words[i].size()) {
            // get the current character
            char ch = words[i][j];
            // convert the character into an index:
            int index = ch - 'a';
            // use one occurrence of this character
            tempFreq[index]--;
            // add this character's score
            tempScore += score[index];
            // if the frequency becomes negative do not have enough copies of this character.
            if (tempFreq[index] < 0) {
                break;
            }
            // move to the next character
            j++;
        }
        // take words[i] if j reached the end of the word every required character was available.
        if (j == words[i].size()) {
            // continue processing the remaining words add the score of the current word to the current total score pass tempFreq because the letters used by this word are no longer available.
            solve(i + 1, score, words, currScore + tempScore, tempFreq);
        }
        // do not take words[i] skip the current word and move to the next word use the original freq because the current word was not selected, so no letters were used.
        solve(i + 1, score, words, currScore, freq);
    }
    int maxScoreWords(vector<string>& words, vector<char>& letters, vector<int>& score) {
        // create a frequency array freq[i] stores how many copies of the character corresponding to index i are available.
        vector<int> freq(26, 0);
        // count the frequency of every available letter
        for (char ch : letters) {
            // convert character into an index
            int index = ch - 'a';
            // increase its frequency
            freq[index]++;
        }
        // reset the maximum score
        maxScore = INT_MIN;
        // store the number of words
        n = words.size();
        // start backtracking from the first word.
        // initially:
        // - no words have been selected
        // - current score is 0
        // - all letters are available
        solve(0, score, words, 0, freq);
        // return the maximum score found
        return maxScore;
    }
};

// Time Complexity  : O(N)
// Space Complexity : O(N)