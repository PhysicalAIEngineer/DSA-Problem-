// Brute Force Code & Optimal Code [DFS Method]
class Solution {
public:
    bool isCycleDFS(unordered_map<int, vector<int>>& adj, int vertex, vector<bool>& visited, vector<bool>& inRecursion) {
        // mark current node as visited
        visited[vertex] = true;
        // mark current node as part of the current DFS path
        inRecursion[vertex] = true;
        // visit all neighbours
        for (int neighbour : adj[vertex]) {
            // if neighbour is not visited continue DFS from neighbour
            if (!visited[neighbour]) {
                if (isCycleDFS(adj, neighbour, visited, inRecursion)) {
                    return true;
                }
            }
            // if neighbour is already in the current DFS path then a cycle is found
            else if (inRecursion[neighbour]) {
                return true;
            }
        }
        // DFS of this node is complete remove it from the current DFS path
        inRecursion[vertex] = false;
        // no cycle found from this node
        return false;
    }
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        // adjacency list
        unordered_map<int, vector<int>> adj;
        // visited[i] = true if course i was visited before
        vector<bool> visited(numCourses, false);
        // inRecursion[i] = true if course i is currently present in the DFS path
        vector<bool> inRecursion(numCourses, false);
        // build the directed graph
        for (auto& vec : prerequisites) {
            // "a" = course to be taken
            int a = vec[0];
            // "b" = prerequisite course
            int b = vec[1];
            // create edge: b ---> a
            adj[b].push_back(a);
        }
        // check every course
        for (int i = 0; i < numCourses; i++) {
            // start DFS only if course is not visited
            if (!visited[i]) {
                // if DFS detects a cycle courses cannot be completed
                if (isCycleDFS(adj, i, visited, inRecursion)) {
                    return false;
                }
            }
        }
        // no cycle found, so all courses can be completed
        return true;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)