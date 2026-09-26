// Brute Fore Code & Optimal Code [BFS Method]
class Solution {
public:
    // using Kahn's Algorithm (BFS)
    vector<int> topologicalSortCheck(unordered_map<int, vector<int>>& adj, int n, vector<int>& indegree) {
        // queue stores nodes whose indegree becomes 0
        queue<int> que;
        // count how many courses we can process
        int count = 0;
        // store the valid course order
        vector<int> result;
        // add all courses having indegree = 0 these courses have no prerequisites
        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                // add course to result
                result.push_back(i);
                // one course is processed
                count++;
                // add course to queue
                que.push(i);
            }
        }
        // BFS
        while (!que.empty()) {
            // take a course whose prerequisites are completed
            int u = que.front();
            que.pop();
            // visit all courses dependent on u
            for (int v : adj[u]) {
                // one prerequisite of v is completed
                indegree[v]--;
                // if all prerequisites of v are completed
                if (indegree[v] == 0) {
                    // add v to the course order
                    result.push_back(v);
                    // one more course is processed
                    count++;
                    // process v later
                    que.push(v);
                }
            }
        }
        // if all courses are not processed then a cycle is present
        if (count != n) {
            return {};
        }
        // return valid course order
        return result;
    }
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        // adjacency list
        unordered_map<int, vector<int>> adj;
        // indegree[i] = number of prerequisites of course i
        vector<int> indegree(numCourses, 0);
        // build the directed graph
        for (auto& vec : prerequisites) {
            // 'a' = course to be taken
            int a = vec[0];
            // 'b' = prerequisite course
            int b = vec[1];
            // create edge: b ---> a
            adj[b].push_back(a);
            // one prerequisite is going into course a
            indegree[a]++;
        }
        // find the topological order if cycle is present, return []
        return topologicalSortCheck(adj, numCourses, indegree);
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)