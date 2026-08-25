// Brute Force Code & Optimal Code 
class Solution {
public:
    vector<vector<int>> findWinners(vector<vector<int>>& matches) {
        // dictionary to store how many matches each player has lost.
        unordered_map<int, int> lost;
        // step 1: count the losses of every player.
        for (auto& match : matches) {
            // match[0] = winner
            // match[1] = loser
            int lose = match[1];
            // increase the loss count of the losing player.
            lost[lose]++;
        }
        // store players who have never lost a match.
        vector<int> notLost;
        // store players who have lost exactly one match.
        vector<int> oneLos;
        // step 2: find players with 0 or 1 loss.
        for (auto& match : matches) {
            // player who lost this match.
            int lose = match[1];
            // player who won this match.
            int win = match[0];
            // if the losing player has lost exactly once add them to the one-loss list this player can appear as a loser only once so duplicates are not added.
            if (lost[lose] == 1) {
                oneLos.push_back(lose);
            }
            // if the winning player is not present in lost they have never lost any match.
            if (lost.find(win) == lost.end()) {
                // add the player to the no-loss list.
                notLost.push_back(win);
                // mark this player as already processed 2 is only used as a marker it does not represent the actual loss count.
                lost[win] = 2;
            }
        }
        // sort players in ascending order as required.
        sort(notLost.begin(), notLost.end());
        sort(oneLos.begin(), oneLos.end());
        // return: [0-loss players, 1-loss players]
        return {notLost, oneLos};
    }
};

// Time Complexity : O(Nlog)
// Space Complexity : O(N)