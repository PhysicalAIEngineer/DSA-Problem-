// Brute Force Code & Optimal Code
class Solution {
public:
    int result = 0;
    int longestPath(vector<int>& parent, string s) {
        // total number of nodes in the tree.
        int n = parent.size();
        // stores the maximum valid path length found anywhere in the tree. Adjacent nodes must have different characters.
        result = 0;
        // build an adjacency list to represent the undirected tree.
        vector<vector<int>> adj(n);
        // parent[i] gives the parent of node i node 0 is the root, so start from node 1.
        for (int i = 1; i < n; i++) {
            int u = i;
            int v = parent[i];
            // add the parent-child relationship in both directions.
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        // DFS returns the length of the longest valid downward path starting at curr and extending into at most one subtree parent_node prevents traversing backward in the tree.
        function<int(int, int)> DFS = [&](int curr, int parent_node) {
            // length of the longest valid downward path among the children processed so far.
            int longest = 0;
            // length of the second-longest valid downward path two paths are needed because the longest path passing through curr may extend into two different subtrees.
            int second_longest = 0;
            // explore every neighbor of the current node.
            for (int child : adj[curr]) {
                // skip the parent to avoid revisiting it.
                if (child == parent_node) {
                    continue;
                }
                // calculate the longest valid downward path starting at this child.
                int child_longest_length = DFS(child, curr);
                // edge between curr and child can be included only when their characters are different.
                if (s[child] == s[curr]) {
                    continue;
                }
                // update the two longest valid downward paths.
                if (child_longest_length > second_longest) {
                    second_longest = child_longest_length;
                }
                // keep longest >= second_longest.
                if (second_longest > longest) {
                    swap(longest, second_longest);
                }
            }
            // CASE 1: longest valid downward path including curr only one child branch can be used.
            int longest_valid_downward = max(longest, second_longest) + 1;
            // CASE 2: path containing only the current node.
            int path_containing_current_node = 1;
            // CASE 3: longest valid path passing through curr and extending into two different child subtrees.
            int longest_valid_path_passing = longest + second_longest + 1;
            // update the global answer with the best path found.
            result = max({result, longest_valid_path_passing, longest_valid_downward, path_containing_current_node});
            // return the longest valid downward path from curr the parent can extend only one branch through curr.
            return max(longest_valid_downward, path_containing_current_node);
        };
        // start DFS from node 0, the root since it has no parent, use -1.
        DFS(0, -1);
        // return the longest valid path found anywhere in the tree.
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)