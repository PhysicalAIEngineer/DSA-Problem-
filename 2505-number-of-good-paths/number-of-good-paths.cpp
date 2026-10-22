// Brute Force Code & Optimal Code
class Solution {
public:
    vector<int> parent;
    vector<int> rank;
    // find the representative (root) of the component containing node x.
    int find(int x) {
        // if x is its own parent, it is the root of its component.
        if (x == parent[x]) {
            return x;
        }
        // path compression: connect x directly to the root.
        parent[x] = find(parent[x]);
        return parent[x];
    }
    // merge the components containing nodes x and y.
    void Union(int x, int y) {
        // find the roots of both components.
        int x_parent = find(x);
        int y_parent = find(y);
        // if both nodes already have the same root they are already in the same component.
        if (x_parent == y_parent) {
            return;
        }
        // union by rank: attach the shorter tree under the taller tree.
        if (rank[x_parent] > rank[y_parent]) {
            parent[y_parent] = x_parent;
        }
        else if (rank[x_parent] < rank[y_parent]) {
            parent[x_parent] = y_parent;
        }
        else {
            // if both trees have equal rank, attach one root beneath the other root.
            parent[x_parent] = y_parent;
            // resulting tree's rank increases by one.
            rank[y_parent]++;
        }
    }
    int numberOfGoodPaths(vector<int>& vals, vector<vector<int>>& edges) {
        // total number of nodes in the tree.
        int n = vals.size();
        // DSU initialization initially, every node belongs to a separate component.
        parent.resize(n);
        iota(parent.begin(), parent.end(), 0);
        // rank estimates the height of each DSU tree initially, every component contains one node.
        rank.assign(n, 1);
        // build the adjacency list for the undirected tree.
        vector<vector<int>> adj(n);
        for (auto& edge : edges) {
            int u = edge[0];
            int v = edge[1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        // group nodes by their values processing nodes in increasing value order allows us to activate nodes gradually while maintaining the rule that every active node has value <= the current value.
        map<int, vector<int>> val_to_nodes;
        for (int i = 0; i < n; i++) {
            val_to_nodes[vals[i]].push_back(i);
        }
        // every individual node forms a good path of length one.
        int result = n;
        // is_active[u] indicates whether node u has been activated.
        vector<bool> is_active(n, false);
        // process distinct node values in increasing order.
        for (auto& [value, nodes] : val_to_nodes) {
            // activate and connect each node with its active neighbors.
            for (int u : nodes) {
                // merge u with every neighbor that has already been activated. These neighbors have values <= the current value.
                for (int v : adj[u]) {
                    if (is_active[v]) {
                        Union(u, v);
                    }
                }
                // mark u as active after processing its neighbors.
                is_active[u] = true;
            }
            // find the DSU representative of every node whose value equals the current value.
            vector<int> parents;
            for (int u : nodes) {
                parents.push_back(find(u));
            }
            // sort representatives so nodes in the same component appear consecutively.
            sort(parents.begin(), parents.end());
            // count how many current-value nodes belong to each connected component.
            int current_values = parents.size();
            int j = 0;
            while (j < current_values) {
                // representative of the current component.
                int cur_parent = parents[j];
                // number of current-value nodes in this component.
                int count = 0;
                // count consecutive occurrences of this root.
                while (j < current_values &&
                       parents[j] == cur_parent) {
                    j++;
                    count++;
                }
                // any two distinct nodes with the current value in the same component form a good path. Number of unordered pairs = count * (count - 1) / 2.
                result += (count * (count - 1)) / 2;
            }
        }
        // return the total number of good paths including all single-node paths.
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)