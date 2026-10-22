// Brute Force Code & Optimal Code
class Solution {
public:
    int minTime(int n, vector<vector<int>>& edges, vector<bool>& hasApple) {
        // adjacency list to represent the undirected tree adj[u] contains all the neighbors of node u.
        vector<vector<int>> adj(n);
        // build the adjacency list from the given edges since the tree is undirected, add both directions.
        for (auto& edge : edges) {
            int u = edge[0];
            int v = edge[1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        // DFS calculates the minimum time required to collect all apples in the subtree rooted at curr and return to curr parent is the node from which arrived at curr it prevents DFS from moving backward in the tree.
        function<int(int, int)> DFS = [&](int curr, int parent) {
            // total time required to collect all apples in the current node's subtree and return to curr.
            int time = 0;
            // explore every neighbor of the current node.
            for (int child : adj[curr]) {
                // skip the parent node to avoid traversing backward.
                if (child == parent) {
                    continue;
                }
                // recursively calculate the time needed to collect apples in the child's subtree and return to child.
                int time_from_child = DFS(child, curr);
                // visit this child's subtree if:
                // 1. time_from_child > 0: there is an apple deeper in the child's subtree.
                // 2. hasApple[child] is true: the child itself has an apple.
                if (time_from_child > 0 || hasApple[child]) {
                    // add the time required to visit this subtree 2 represents traveling from curr to child and returning from child to curr time_from_child covers the deeper subtree.
                    time += 2 + time_from_child;
                }
            }
            // return the total time needed to collect all apples in curr's subtree and return to curr.
            return time;
        };
        // start DFS from node 0, the root of the tree the root has no parent, so use -1.
        return DFS(0, -1);
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)