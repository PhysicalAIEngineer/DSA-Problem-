// Brute Force Code & Optimal Code
class Solution {public: int N; vector<int> count; int result_base_node = 0; vector<int> sumOfDistancesInTree(int n, vector<vector<int>>& edges) {
        // adjacency list to represent the undirected tree
        vector<vector<int>> adj(n);
        // stores the total number of nodes in the tree
        N = n;
        // count[i] stores the size of the subtree rooted at node i including node i itself and all its descendants
        count.assign(n, 0);
        // stores the sum of distances from node 0 to every other node this is calculated during the first DFS traversal.
        result_base_node = 0;
        // build the adjacency list from the given edges
        for (auto& edge : edges) {
            int u = edge[0];
            int v = edge[1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        // first DFS: calculate subtree sizes and the answer for node 0
        function<int(int, int, int)> DFSBase =
            [&](int curr_node, int prev_node, int curr_depth) {
                // count the current node as part of its own subtree
                int total_node = 1;
                // add the current node's distance from node 0 since DFS starts at node 0 with depth 0 curr_depth represents the distance from node 0 to curr_node. Summing all depths gives the total distance from node 0 to every node in the tree.
                result_base_node += curr_depth;
                // visit all neighboring nodes
                for (int child : adj[curr_node]) {
                    // skip the parent to avoid traversing backward
                    if (child == prev_node) {
                        continue;
                    }
                    // calculate the size of the child's subtree and add it to the current subtree size
                    total_node += DFSBase(child, curr_node, curr_depth + 1);
                }
                // store the complete subtree size of the current node
                count[curr_node] = total_node;
                // return this subtree size to the parent call
                return total_node;
            };
        // second DFS: reroot the tree and calculate all answers
        function<void(int, int, vector<int>&)> DFS = [&](int parent_node, int prev_node, vector<int>& result) {
                // visit every child of the current node
                for (int child : adj[parent_node]) {
                    // skip the parent to avoid going backward
                    if (child == prev_node) {
                        continue;
                    }
                    // rerooting formula: result[child] = result[parent_node] - count[child] + (N - count[child])
                    // nodes inside the child's subtree become one edge closer to the new root their total distance decreases by count[child] nodes outside the child's subtree become one edge farther from the new root their total distance increases by N - count[child].
                    result[child] = result[parent_node] - count[child]  + (N - count[child]);
                    // recursively calculate answers for descendants
                    DFS(child, parent_node, result);
                }
            };
        // run the first DFS starting from node 0. this calculates: 1. subtree size of every node &  2. sum of distances from node 0 to all nodes
        DFSBase(0, -1, 0);
        // result[i] stores the sum of distances from node i to every other node in the tree
        vector<int> result(n, 0);
        // first DFS has already calculated the answer for node 0
        result[0] = result_base_node;
        // run the second DFS to calculate all remaining answers using the rerooting formula
        DFS(0, -1, result);
        // return the answer for every node
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)