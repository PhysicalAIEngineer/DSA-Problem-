// Brute Force Code & Optimal Code
class Solution {
public:
    pair<int, int> BFS(unordered_map<int, vector<int>>& adj, int source) {
        // queue for BFS
        queue<int> q;
        q.push(source);
        // track visited nodes
        unordered_map<int, bool> visited;
        visited[source] = true;
        // distance from source
        int distance = 0;
        // farthest node found so far
        int farthestnode = source;
        // BFS traversal
        while (!q.empty()) {
            // number of nodes in the current level
            int size = q.size();
            while (size--) {
                // remove current node from queue
                int current = q.front();
                q.pop();
                // last node processed in this level
                farthestnode = current;
                // visit all neighbours
                for (int neighbour : adj[current]) {
                    if (!visited[neighbour]) {
                        visited[neighbour] = true;
                        q.push(neighbour);
                    }
                }
            }
            // increase distance if another level exists
            if (!q.empty()) {
                distance++;
            }
        }
        // return farthest node and its distance
        return {farthestnode, distance};
    }
    int finddiameter(unordered_map<int, vector<int>>& adj) {
        // first BFS: find one endpoint of the diameter
        auto [farthestnode, dist] = BFS(adj, 0);
        // second BFS: find the diameter
        auto [otherendnode, diameter] = BFS(adj, farthestnode);
        return diameter;
    }
    unordered_map<int, vector<int>> bulidadj(vector<vector<int>>& edges) {
        // build adjacency list
        unordered_map<int, vector<int>> adj;
        for (auto& edge : edges) {
            int u = edge[0];
            int v = edge[1];
            // create empty lists for u and v
            adj[u];
            adj[v];
            // tree is undirected, so add edges in both directions
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        return adj;
    }
    int minimumDiameterAfterMerge(vector<vector<int>>& edges1, vector<vector<int>>& edges2) {
        // build adjacency lists for both trees
        auto adj1 = bulidadj(edges1);
        auto adj2 = bulidadj(edges2);
        // find the diameter of both trees
        int diameter_1 = finddiameter(adj1);
        int diameter_2 = finddiameter(adj2);
        // minimum possible diameter after merging
        int combined = (diameter_1 + 1) / 2 + (diameter_2 + 1) / 2 + 1;
        // return the maximum of all three possibilities
        return max({diameter_1, diameter_2, combined});
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)