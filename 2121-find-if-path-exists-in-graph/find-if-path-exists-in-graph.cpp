//Brute Force Code & Optimal Code [BFS Method]
class Solution {
public:
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        // create an adjacency list to represent the graph
        unordered_map<int, vector<int>> mp;
        // build the undirected graph
        for (auto& vec : edges) {
            int u = vec[0];
            int v = vec[1];
            // add an edge from u to v
            mp[u].push_back(v);
            // add an edge from v to u
            mp[v].push_back(u);
        }
        // track visited nodes to avoid revisiting them
        vector<bool> visited(n, false);
        // create a queue for BFS and add the source node
        queue<int> q;
        q.push(source);
        // mark the source as visited
        visited[source] = true;
        // perform BFS until the queue becomes empty
        while (!q.empty()) {
            // remove the front node from the queue
            int node = q.front();
            q.pop();
            // if the destination is reached, a path exists
            if (node == destination) {
                return true;
            }
            // visit all unvisited neighboring nodes
            for (int it : mp[node]) {
                if (!visited[it]) {
                    // mark the neighbor as visited
                    visited[it] = true;
                    // add the neighbor to the queue
                    q.push(it);
                }
            }
        }
        // return false if the destination is unreachable
        return false;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)