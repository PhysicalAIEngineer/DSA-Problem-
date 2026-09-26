// Brute Fore Code & Optimal Code [DFS Method]
class Solution {
public:
    // flag to indicate whether a cycle exists
    bool hasCycle = false;
    void DFS(unordered_map<int, vector<int>>& adj, int u, vector<bool>& visited, vector<int>& st, vector<bool>& inRecursion) {
        // mark current node as visited
        visited[u] = true;
        // mark current node as part of current DFS path
        inRecursion[u] = true;
        // first process all neighbours of u then add u to stack
        for (int v : adj[u]) {
            // if v is already in the current DFS path then a cycle is present
            if (inRecursion[v]) {
                hasCycle = true;
                return;
            }
            // if v is not visited, perform DFS
            if (!visited[v]) {
                DFS(adj, v, visited, st, inRecursion);
            }
        }
        // add current node after all its neighbours are processed
        st.push_back(u);
        // DFS of u is completed so remove u from current recursion path
        inRecursion[u] = false;
    }
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        // create adjacency list
        unordered_map<int, vector<int>> adj;
        // track whether each course has been visited
        vector<bool> visited(numCourses, false);
        // track nodes currently present in DFS recursion path
        vector<bool> inRecursion(numCourses, false);
        // reset cycle flag
        hasCycle = false;
        // stack to store DFS finishing order
        vector<int> st;
        // build the directed graph
        for (auto& vec : prerequisites) {
            // 'a' = course to be taken
            int a = vec[0];
            // 'b' = prerequisite course
            int b = vec[1];
            // create edge: b ---> a
            adj[b].push_back(a);
        }
        // perform DFS for every course because graph may have multiple components
        for (int i = 0; i < numCourses; i++) {
            if (!visited[i]) {
                DFS(adj, i, visited, st, inRecursion);
            }
        }
        // Final topological ordering if cycle is present valid course order is not possible
        if (hasCycle) {
            return {};
        }
        // reverse DFS finishing order
        vector<int> result;
        while (!st.empty()) {
            result.push_back(st.back());
            st.pop_back();
        }
        // Return valid course order
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)