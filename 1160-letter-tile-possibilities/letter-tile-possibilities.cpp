// Brute Force Code & Optimal Code
class Solution {
public:
    // store the total number of tiles.
    int n = 0;
    void solve(string& tiles, vector<bool>& used,unordered_set<string>& result, string curr) {
        // add the current sequence to the set use a set because tiles may contain duplicate characters and only want to count unique sequences empty string is also added during the first call it will be removed from the final count by subtracting 1.
        result.insert(curr);
        // try every tile as the next character in the current sequence.
        for (int i = 0; i < n; i++) {
            // if this particular tile has already been used in the current sequence, we cannot use it again.
            if (used[i]) {
                continue;
            }
            // TRY / CHOOSE
            // add the current tile to the sequence.
            curr += tiles[i];
            // mark this tile as used.
            used[i] = true;
            // EXPLORE
            // recursively try adding another tile to the current sequence.
            solve(tiles, used, result, curr);
            // UNDO / BACKTRACK
            // mark the current tile as unused again so it can be used in another sequence.
            used[i] = false;
            // remove the last character from the sequence this restores curr to its previous state before trying the next tile.
            curr.pop_back();
        }
    }
    int numTilePossibilities(string tiles) {
        // store the number of tiles.
        n = tiles.length();
        // used[i] tells whether the tile at index i is currently part of the sequence.
        vector<bool> used(n, false);
        // store every unique sequence unordered_set automatically removes duplicate sequence that may be generated when tiles contain repeated characters.
        unordered_set<string> result;
        // start with an empty sequence.
        string curr = "";
        // start the backtracking process.
        solve(tiles, used, result, curr);
        // empty string was also added to the set since the problem asks for non-empty sequences subtract 1 from the total count.
        return result.size() - 1;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)