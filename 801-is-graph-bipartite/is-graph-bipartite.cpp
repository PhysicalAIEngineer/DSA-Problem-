// Brute Force Code [BFS Method]
class Solution {
public:
    bool checkBipartiteBFS(vector<vector<int>>& adj,int curr,vector<int>& color,int currColor
    ) {
        // give the starting node its color
        color[curr] = currColor;
        // queue for BFS traversal
        queue<int> que;
        que.push(curr);
        // continue BFS while queue is not empty
        while (!que.empty()) {
            // remove the front node from the queue
            int u = que.front();
            que.pop();
            // visit all adjacent nodes of u
            for (int v : adj[u]) {
                // if adjacent node already has the same color then graph is not bipartite
                if (color[v] == color[u]) {
                    return false;
                }
                // if adjacent node is not colored yet
                else if (color[v] == -1) {
                    // give opposite color to the adjacent node 1 -> 0 & 0 -> 1
                    color[v] = 1 - color[u];
                    // add the node to queue for further BFS
                    que.push(v);
                }
            }
        }
        // no color conflict found in this component
        return true;
    }
    bool isBipartite(vector<vector<int>>& adj) {
        int V = adj.size();
        // -1 means node is not colored yet
        vector<int> color(V, -1);
        // so,  1 = red & 0 = green check every connected component because graph can be disconnected
        for (int i = 0; i < V; i++) {
            // if node is not colored, start BFS from this node
            if (color[i] == -1) {
                // start this component with color 1
                if (checkBipartiteBFS(adj, i, color, 1) == false) {
                    return false;
                }
            }
        }
        // all components are successfully 2-colored
        return true;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)