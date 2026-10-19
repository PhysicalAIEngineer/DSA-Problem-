// Brute Force Code & Optimal Code
class Solution {
public:
    bool check(unordered_map<int, vector<int>>& mp, int node, int destination,vector<bool>& visited) {
        // if the current node is the destination, return true
        if (node == destination) {
            return true;
        }
        // stop if the current node has already been visited
        if (visited[node]) {
            return false;
        }
        // mark the current node as visited
        visited[node] = true;
        // traverse all neighboring nodes using DFS
        for (int i : mp[node]) {
            // check whether the destination is reachable
            if (check(mp, i, destination, visited)) {
                return true;
            }
        }
        // no path to the destination was found
        return false;
    }
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        // if source and destination are the same, return true
        if (source == destination) {
            return true;
        }
        // create an adjacency list for the undirected graph
        unordered_map<int, vector<int>> mp;
        // add every edge in both directions
        for (auto& vec : edges) {
            int u = vec[0];
            int v = vec[1];
            // connect u to v
            mp[u].push_back(v);
            // connect v to u
            mp[v].push_back(u);
        }
        // initialize all nodes as unvisited
        vector<bool> visited(n, false);
        // start DFS from source and check if destination is reachable
        return check(mp, source, destination, visited);
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)