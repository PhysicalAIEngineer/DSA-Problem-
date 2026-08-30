// Brute Force Code & Optimal Code
class Solution {
public:
    // store the restored original array.
    vector<int> result;
    void solve(int u, int prev, unordered_map<int, vector<int>>& adj) {
        // add the current node to the answer DFS visits nodes in the same order as they appear in the original array.
        result.push_back(u);
        // visit every node connected to the current node.
        for (int v : adj[u]) {
            // do not move back to the node from which we came.
            if (v != prev) {
                // continue DFS from the next node.
                solve(v, u, adj);
            }
        }
    }
    vector<int> restoreArray(vector<vector<int>>& adjacentPairs) {   
        // create an adjacency list.
        // adj[u] contains all numbers that are directly
        // adjacent to u in the original array.
        unordered_map<int, vector<int>> adj;
        // build the undirected graph using all adjacent pairs.
        for (auto& pair : adjacentPairs) {
            // extract the two adjacent numbers.
            int u = pair[0];
            int v = pair[1];
            // add v to u's list of neighbors.
            adj[u].push_back(v);
            // add u to v's list of neighbors.
            adj[v].push_back(u);
        }
        // find an endpoint of the original array.
        // in the graph:
        // - two endpoints have degree 1.
        // - every middle element has degree 2.
        int startPoint = -1;
        // check every node in the graph.
        for (auto& it : adj) {
            int node = it.first;
            // node with only one neighbor must be an endpoint.
            if (adj[node].size() == 1) {
                // use this endpoint as the starting point for DFS.
                startPoint = node;
                break;
            }
        }
        // start DFS from the endpoint.
        // prev = -1 because the starting node does not have a previous node.
        solve(startPoint, -1, adj);
        // return the restored original array.
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)