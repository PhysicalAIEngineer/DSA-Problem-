// Brute Force Code & Optimal Code
class Solution {
public:
    vector<int> parent;
    vector<int> rank;
    int find(int x) {
        // if x is its own parent then x is the root of its component
        if (x == parent[x]) {
            return x;
        }
        // path compression: make x directly point to the root
        parent[x] = find(parent[x]);
        // return the root
        return parent[x];
    }
    void Union(int x, int y) {
        // find the roots of both nodes
        int x_parent = find(x);
        int y_parent = find(y);
        // if both nodes already belong to the same component nothing to merge
        if (x_parent == y_parent) {
            return;
        }
        // union by rank attach the smaller tree under the larger tree
        if (rank[x_parent] > rank[y_parent]) {
            parent[y_parent] = x_parent;
        }
        else if (rank[x_parent] < rank[y_parent]) {
            parent[x_parent] = y_parent;
        }
        else {
            // both trees have the same rank attach x tree under y tree
            parent[x_parent] = y_parent;
            // increase the rank of the new root
            rank[y_parent]++;
        }
    }
    int makeConnected(int n, vector<vector<int>>& connections) {
        // to connect n computers at least n - 1 cables are required
        if (connections.size() < n - 1) {
            return -1;
        }
        // parent array of DSU
        parent = vector<int>(n);
        // rank array for union by rank
        rank = vector<int>(n, 0);
        // initially every computer is its own parent so every computer is a separate component
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
        // initially there are n separate components
        int components = n;
        // process every available connection
        for (auto& vec : connections) {
            // if both computers belong to different components this connection can merge the two components
            if (find(vec[0]) != find(vec[1])) {
                // two components become one so decrease component count by 1
                components--;
                // merge the two components
                Union(vec[0], vec[1]);
            }
        }
        // if there are 'components' separate components need components - 1 connections to connect them all
        return components - 1;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)