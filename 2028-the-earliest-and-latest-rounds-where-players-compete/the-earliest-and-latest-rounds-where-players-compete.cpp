// Brute Force Code & Optimal Code
class Solution {
public:
    vector<int> earliestAndLatest(int n, int firstPlayer, int secondPlayer) {
        // current positions of the two target players
        int left = firstPlayer;
        int right = secondPlayer;
        // base case: if the two players are paired in the current round they meet immediately.
        if (left == n - right + 1) {
            return {1, 1};
        }
        // ensure the first player is always on the left side of the tournament bracket.
        if (left > n - right + 1) {
            int temp = n - left + 1;
            left = n - right + 1;
            right = temp;
        }
        // store the earliest and latest possible meeting rounds
        int minRound = n;
        int maxRound = 1;
        // number of players advancing to the next round
        int nextRoundPlayers = (n + 1) / 2;
        // case 1: both players are in the left half.
        if (right <= nextRoundPlayers) {
            // number of players before the first player
            int countLeft = left - 1;
            // number of players between the two players
            int midCount = right - left - 1;
            // try every possible number of survivors before the first player.
            for (int survivorsLeft = 0;
                 survivorsLeft <= countLeft;
                 survivorsLeft++) {
                // try every possible number of survivors between the two players.
                for (int survivorsMid = 0;
                     survivorsMid <= midCount;
                     survivorsMid++) {
                    // new position of the first player
                    int pos1 = survivorsLeft + 1;
                    // new position of the second player
                    int pos2 = pos1 + survivorsMid + 1;
                    // recursively calculate the earliest and latest meeting rounds.
                    vector<int> result = earliestAndLatest(nextRoundPlayers,pos1, pos2);
                    // add one for the current round
                    minRound = min(minRound, result[0] + 1);
                    maxRound = max(maxRound, result[1] + 1);
                }
            }
        }
        // case 2: players are on opposite sides.
        else {
            // mirrored position of the second player
            int fightsRight = n - right + 1;
            // number of players before the first player
            int countLeft = left - 1;
            // number of players between the first player and the mirrored second player
            int midCount = fightsRight - left - 1;
            // number of players between the mirrored position and the actual second player
            int remainMidCount = right - fightsRight - 1;
            // try every possible survivor arrangement
            for (int survivorsLeft = 0;
                 survivorsLeft <= countLeft;
                 survivorsLeft++) {
                for (int survivorsMid = 0;
                     survivorsMid <= midCount;
                     survivorsMid++) {
                    // new position of the first player
                    int pos1 = survivorsLeft + 1;
                    // new position of the second player
                    int pos2 = pos1 + survivorsMid + (remainMidCount + 1) / 2 +1;
                    // recursively solve the smaller tournament
                    vector<int> result = earliestAndLatest(nextRoundPlayers,pos1, pos2);
                    // include the current round
                    minRound = min(minRound, result[0] + 1);
                    maxRound = max(maxRound, result[1] + 1);
                }
            }
        }
        // return earliest and latest possible meeting rounds
        return {minRound, maxRound};
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)