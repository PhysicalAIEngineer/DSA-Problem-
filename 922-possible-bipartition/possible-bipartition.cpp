// Brute Force Code & Optimal Code
class Solution {
public:
    bool isBipartite(unordered_map<int, vector<int>>& adjacent, int node,vector<int>& color) {
        // create a queue for BFS traversal
        queue<int> q;
        q.push(node);
        // assign color 1 to the starting node
        color[node] = 1;
        // perform BFS to check whether the graph is bipartite
        while (!q.empty()) {
            // remove the front node from the queue
            int u = q.front();
            q.pop();
            // visit all neighboring nodes
            for (int v : adjacent[u]) {
                // if adjacent nodes have the same color, the graph is not bipartite
                if (color[v] == color[u]) {
                    return false;
                }
                // if the neighbor is uncolored (-1), assign the opposite color
                if (color[v] == -1) {
                    color[v] = 3 - color[u];
                    // add the neighbor to the queue
                    q.push(v);
                }
            }
        }
        // return true if no coloring conflict is found
        return true;
    }
    bool possibleBipartition(int n, vector<vector<int>>& dislikes) {
        // create an adjacency list for the undirected graph
        unordered_map<int, vector<int>> adjacent;
        // build the graph using dislike relationships
        for (auto & vec : dislikes) {
            int u = vec[0];
            int v = vec[1];
            // add an edge from u to v
            adjacent[u].push_back(v);
            // add an edge from v to u
            adjacent[v].push_back(u);
        }
        // initialize all people as uncolored (-1)
        vector<int> color(n + 1, -1);
        // check every connected component of the graph
        for (int i = 1; i <= n; i++) {
            // start BFS if the current person is not yet colored
            if (color[i] == -1) {
                // return false if the component cannot be colored with two colors
                if (!isBipartite(adjacent, i, color)) {
                    return false;
                }
            }
        }
        // return true if the entire graph is bipartite
        return true;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)