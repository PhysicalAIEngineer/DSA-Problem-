// Brute Force Code
class Solution {
public:
    int findTheWinner(int n, int k) {
        // create a vector containing all players numbered from 1 to n
        vector<int> players;
        for (int i = 1; i <= n; i++) {
            players.push_back(i);
        }
        // start counting from the first player index 0
        int index = 0;
        // continue eliminating players until only one player remains
        while (players.size() > 1) {
            // move (k - 1) steps from the current position modulo is used to wrap around the circular list.
            index = (index + k - 1) % players.size();
            // remove the player at the calculated index next round automatically starts from the player immediately after the removed player.
            players.erase(players.begin() + index);
        }
        // only remaining player is the winner
        return players[0];
    }
};

// Time Complexity : O(N)
// Space Complexity : O(1)