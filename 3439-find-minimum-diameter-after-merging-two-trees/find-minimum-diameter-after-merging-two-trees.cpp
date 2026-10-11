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
        int farthestNode = source;
        // BFS traversal
        while (!q.empty()) {
            // number of nodes in current level
            int size = q.size();
            while (size--) {
                // remove current node from queue
                int current = q.front();
                q.pop();
                // last node processed in this level becomes the farthest node
                farthestNode = current;
                // visit all neighbours
                for (int neighbour : adj[current]) {
                    if (!visited[neighbour]) {
                        visited[neighbour] = true;
                        q.push(neighbour);
                    }
                }
            }
            // if next level exists, increase distance by 1
            if (!q.empty()) {
                distance++;
            }
        }
        // return farthest node and its distance
        return {farthestNode, distance};
    }
    int findDiameter(unordered_map<int, vector<int>>& adj) {
        // start BFS from any node (0) find the farthest node from it
        auto [farthestNode, dist] = BFS(adj, 0);
        // start BFS from farthestNode its farthest distance is the diameter
        auto [otherEndNode, diameter] = BFS(adj, farthestNode);
        return diameter;
    }
    unordered_map<int, vector<int>> buildAdj(vector<vector<int>>& edges) {
        // build adjacency list
        unordered_map<int, vector<int>> adj;
        for (auto& edge : edges) {
            int u = edge[0];
            int v = edge[1];
            // create empty lists for both nodes
            adj[u];
            adj[v];
            // tree is undirected, so add edge in both directions
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        return adj;
    }
    int minimumDiameterAfterMerge(vector<vector<int>>& edges1,vector<vector<int>>& edges2
    ) {
        // build adjacency lists for both trees
        auto adj1 = buildAdj(edges1);
        auto adj2 = buildAdj(edges2);
        // find diameter of first tree
        int diameter_1 = findDiameter(adj1);
        // find diameter of second tree
        int diameter_2 = findDiameter(adj2);
        // radius of first tree = (diameter_1 / 2) &  radius of second tree = c(diameter_2 / 2) + 1 for the new connecting edge
        int combined = (diameter_1 + 1) / 2 + (diameter_2 + 1) / 2 + 1;
        // final diameter is the maximum of diameter of tree 1 &  diameter of tree 2 & path passing through the new connecting edge
        return max({diameter_1, diameter_2, combined});
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)