// Optimal Code
class Solution {
public:
    // recursive function to find the winner's index (0-based)
    int findWinnerIdx(int n, int k) {
        // base case: if only one player is left its index is 0.
        if (n == 1) {
            return 0;
        }
        // recursively find the winner's index when there are n - 1 players.
        int index = findWinnerIdx(n - 1, k);
        // convert the winner's index from the smaller circle (n - 1 players) to the current circle of n players using the josephus formula.
        index = (index + k) % n;
        // return the winner's index for n players.
        return index;
    }
    // return the winner's number (1-based)
    int findTheWinner(int n, int k) {
        // find the winner's index (0-based)
        int result_index = findWinnerIdx(n, k);
        // convert the 0-based index into the required 1-based player number
        return result_index + 1;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(1)