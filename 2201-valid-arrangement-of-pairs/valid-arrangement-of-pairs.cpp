// Brute Force Code & Optimal Code
class Solution {
public:
    vector<vector<int>> validArrangement(vector<vector<int>>& pairs) {
        // build adjacency list adj[u] contains all nodes v such that edge u -> v exists
        unordered_map<int, vector<int>> adj;
        // store indegree and outdegree of every node
        unordered_map<int, int> indegree;
        unordered_map<int, int> outdegree;
        // build the graph
        for (auto& edge : pairs) {
            int u = edge[0];
            int v = edge[1];
            // add directed edge: u -> v
            adj[u].push_back(v);
            // increase outdegree of u
            outdegree[u]++;
            // increase indegree of v
            indegree[v]++;
        }
        // start from the first pair's starting node
        int startNode = pairs[0][0];
        // find the start node of the euler path for an Euler path: outdegree - indegree = 1
        for (auto& [node, neighbours] : adj) {
            if (outdegree[node] - indegree[node] == 1) {
                startNode = node;
                break;
            }
        }
        // stack is used to simulate DFS eulerPath will store the final Euler path
        vector<int> EulerPath;
        vector<int> st;
        // start DFS from the starting node
        st.push_back(startNode);
        while (!st.empty()) {
            // look at the top node of the stack
            int curr = st.back();
            // if current node still has unused outgoing edges
            if (!adj[curr].empty()) {
                // take the last neighbour and remove this edge so it is used only once
                int neighbour = adj[curr].back();
                adj[curr].pop_back();
                // move to the neighbour
                st.push_back(neighbour);
            } else {
                // no outgoing edge is left from curr add curr to euler path
                EulerPath.push_back(curr);
                // remove curr from stack
                st.pop_back();
            }
        }
        // nodes are collected in reverse order reverse them to get the correct Euler path
        reverse(EulerPath.begin(), EulerPath.end());
        // build result pairs from consecutive nodes
        vector<vector<int>> result;
        for (int i = 0; i < (int)EulerPath.size() - 1; i++) {
            result.push_back({EulerPath[i], EulerPath[i + 1]});
        }
        // return the valid arrangement of pairs
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)