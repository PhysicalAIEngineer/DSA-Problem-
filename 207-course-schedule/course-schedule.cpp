// Brute Force Code & Optimal Code [BFS Method]
class Solution {
public:
    bool topologicalSortCheck(unordered_map<int, vector<int>>& adj, int n, vector<int>& indegree) {
        // queue for nodes whose indegree becomes 0
        queue<int> que;
        // count how many nodes we can process
        int count = 0;
        // add all nodes having indegree = 0 these nodes have no pending prerequisites
        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                count++;
                que.push(i);
            }
        }
        // BFS using Kahn's Algorithm
        while (!que.empty()) {
            // take a course with no remaining prerequisite
            int u = que.front();
            que.pop();
            // visit all courses that depend on course u
            for (int v : adj[u]) {
                // one prerequisite of v is now completed
                indegree[v]--;
                // if all prerequisites of v are completed
                if (indegree[v] == 0) {
                    // v can now be completed
                    count++;
                    que.push(v);
                }
            }
        }
        // if were able to process all courses then there is no cycle
        if (count == n) {
            return true;
        }
        // some courses could not be processed which means a cycle is present
        return false;
    }
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        // adjacency list adj[b] contains courses that can be taken after b
        unordered_map<int, vector<int>> adj;
        // indegree[i] = number of prerequisites for course i
        vector<int> indegree(numCourses, 0);
        // process every prerequisite pair
        for (auto& vec : prerequisites) {
            // 'a' is the course we want to take
            int a = vec[0];
            // 'b' is the prerequisite course
            int b = vec[1];
            // create edge: b ---> a must complete b before taking a
            adj[b].push_back(a);
            // one prerequisite is going into course a
            indegree[a]++;
        }
        // check whether all courses can be processed if a cycle is present, not possible
        return topologicalSortCheck(adj, numCourses, indegree);
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)