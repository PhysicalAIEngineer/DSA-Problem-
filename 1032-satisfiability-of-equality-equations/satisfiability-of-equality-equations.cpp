// Brute Force Code & Optimal Code
class Solution {
public:
    vector<int> parent;
    vector<int> rank;
    int find(int i) {
        // if i is not the root of its set recursively find the root
        if (parent[i] != i) {
            // path compression make i directly point to the root
            parent[i] = find(parent[i]);
        }
        // return the root
        return parent[i];
    }
    void Union(int x, int y) {
        // find the roots of x and y
        int p_x = find(x);
        int p_y = find(y);
        // if they belong to different sets merge the two sets
        if (p_x != p_y) {
            // union by rank attach the smaller rank tree under the larger rank tree
            if (rank[p_x] > rank[p_y]) {
                parent[p_y] = p_x;
            }
            else if (rank[p_y] > rank[p_x]) {
                parent[p_x] = p_y;
            }
            else {
                // both roots have the same rank attach p_x under p_y
                parent[p_x] = p_y;
                // increase the rank of the new root
                rank[p_y]++;
            }
        }
    }
    bool equationsPossible(vector<string>& equations) {
        // there are 26 lowercase English letters
        parent = vector<int>(26);
        rank = vector<int>(26);
        // initially every character is in its own set
        for (int i = 0; i < 26; i++) {
            parent[i] = i;
            rank[i] = 1;
        }
        // process all equality equations
        for (string& s : equations) {
            if (s[1] == '=') {
                // convert characters into numbers "a" -> 0, "b" -> 1, ... then merge their sets
                Union(s[0] - 'a', s[3] - 'a');
            }
        }
        // process all inequality equations
        for (string& s : equations) {
            if (s[1] == '!') {
                // if both characters have the same root equality equations already connected them therefore this inequality is impossible
                if (find(s[0] - 'a') == find(s[3] - 'a')) {
                    // connection found
                    return false;
                }
            }
        }
        // no contradiction found
        return true;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)