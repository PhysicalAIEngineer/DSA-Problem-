class Solution {public: vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& adj) {
        // stores all valid paths from source node (0) to target node (n - 1)
        vector<vector<int>> result;
        // DFS explores all possible paths
        function<void(int, vector<int>&)> DFS =
            [&](int start, vector<int>& temp) {
                // add the current node to the current path
                temp.push_back(start);
                // Base case: if reach the target node have found a complete path
                if (start == adj.size() - 1) {
                    // store a copy of the current path in result
                    result.push_back(temp);
                } 
                else {
                    // explore every neighbor of the current node
                    for (int x : adj[start]) {
                        // recursively explore the path through neighbor x
                        DFS(x, temp);
                    }
                }
                // backtracking: remove the current node after exploring all paths starting from this node
                temp.pop_back();
            };
        // start DFS from every neighbor of node 0
        for (int x : adj[0]) {
            // create a fresh path starting from the source node
            vector<int> temp = {0};
            // explore all paths beginning with neighbor x
            DFS(x, temp);
        }
        // return all paths from node 0 to node n - 1
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)