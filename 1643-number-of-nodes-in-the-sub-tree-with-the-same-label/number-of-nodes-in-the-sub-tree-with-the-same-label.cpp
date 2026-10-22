// Brute Force Code & Optimal Code
class Solution {
public:
    vector<int> countSubTrees(int n, vector<vector<int>>& edges, string labels) {
        // build an adjacency list to represent the undirected tree adj[u] contains all the neighbors of node u.
        vector<vector<int>> adj(n);
        for (auto& edge : edges) {
            int u = edge[0];
            int v = edge[1];
            // since the tree is undirected, add both directions.
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        // result[u] stores the number of nodes in the subtree rooted at u that have the same label as node u.
        vector<int> result(n, 0);
        // frequency array for the 26 lowercase English letters.
        // count[0]  -> frequency of 'a'
        // count[1]  -> frequency of 'b'
        // count[25] -> frequency of 'z'
        // initially, no nodes have been counted.
        vector<int> count(26, 0);
        // DFS explores the subtree rooted at node u parent is the node from which we arrived at u.
        function<void(int, int)> DFS = [&](int u, int parent) {
            // get the label of the current node.
            char current_label = labels[u];
            // convert the character into an index from 0 to 25.
            // Example:
            // 'a' -> 0
            // 'b' -> 1
            // 'c' -> 2
            int index = current_label - 'a';
            // record the frequency of the current node's label before counting this node and its descendants.
            int count_before = count[index];
            // count the current node itself.
            count[index]++;
            // explore every neighbor of the current node.
            for (int v : adj[u]) {
                // skip the parent to avoid moving backward through the undirected tree.
                if (v == parent) {
                    continue;
                }
                // recursively explore the child's subtree the shared count array is updated by every DFS call.
                DFS(v, u);
            }
            // all descendants of u have now been explored read the frequency of u's label again.
            int count_after = count[index];
            // difference gives the number of nodes whose label matches labels[u] in the subtree rooted at u.
            result[u] = count_after - count_before;
        };
        // start DFS at node 0, the root of the tree the root has no parent, so use -1.
        DFS(0, -1);
        // return the answer for every node.
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)