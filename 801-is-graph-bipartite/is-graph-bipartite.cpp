// Brute Force Code [DFS Method]
class Solution {
public:
    bool checkBipartiteDFS(vector<vector<int>>& adj,int curr,vector<int>& color,int currColor) {
        // give the current node its color
        color[curr] = currColor;
        // visit all adjacent nodes
        for (int v : adj[curr]) {
            // if adjacent node has the same color then graph cannot be bipartite
            if (color[v] == color[curr]) {
                return false;
            }
            // if adjacent node is not colored yet
            if (color[v] == -1) {
                // give the opposite color to the adjacent node 1 -> 0 & 0 -> 1
                int colorOfV = 1 - currColor;
                // recursively check the remaining graph
                if (checkBipartiteDFS(adj, v, color, colorOfV) == false) {
                    return false;
                }
            }
        }
        // no conflict found in this DFS
        return true;
    }
    bool isBipartite(vector<vector<int>>& adj) {
        int V = adj.size();
        // -1 means the node is not colored yet
        vector<int> color(V, -1);
        // 1 = red & 0 = green check every node because the graph can contain multiple disconnected components
        for (int i = 0; i < V; i++) {
            // if node is not visited/colored start a new DFS from this node
            if (color[i] == -1) {
                // start coloring this component with color 1
                if (checkBipartiteDFS(adj, i, color, 1) == false) {
                    return false;
                }
            }
        }
        // all nodes are colored without any conflict
        return true;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)