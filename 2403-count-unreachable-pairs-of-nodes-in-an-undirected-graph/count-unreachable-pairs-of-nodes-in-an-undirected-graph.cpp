// Brute Force Code & Optimal Code
class Solution {
public:
    vector<int> parent;
    vector<int> rank;
    int find(int x) {
        // path compression if x is not the root, recursively find the root
        if (x == parent[x]) {
            return x;
        }
        // make x directly point to the root
        parent[x] = find(parent[x]);
        return parent[x];
    }
    void Union(int x, int y) {
        // find the roots of both nodes
        int x_parent = find(x);
        int y_parent = find(y);
        // already in the same component
        if (x_parent == y_parent) {
            return;
        }
        // union by rank attach the smaller-rank tree under the larger-rank tree
        if (rank[x_parent] > rank[y_parent]) {
            parent[y_parent] = x_parent;
        }
        else if (rank[x_parent] < rank[y_parent]) {
            parent[x_parent] = y_parent;
        }
        else {
            // both have same rank
            parent[x_parent] = y_parent;
            // increase the rank of the new root
            rank[y_parent]++;
        }
    }
    long long countPairs(int n, vector<vector<int>>& edges) {
        // parent and rank arrays for DSU
        parent = vector<int>(n);
        rank = vector<int>(n, 0);
        // initially every node is its own parent so every node is a separate component
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
        // build connected components using DSU
        for (auto& vec : edges) {
            int u = vec[0];
            int v = vec[1];
            // connect u and v
            Union(u, v);
        }
        // count the size of every connected component
        unordered_map<int, long long> count_size;
        // iterate through every node
        for (int i = 0; i < n; i++) {
            // find the root of node i
            int root = find(i);
            // increase the size of that component
            count_size[root]++;
        }
        // store the result
        long long result = 0;
        // number of nodes not processed yet
        long long remainingNodes = n;
        // count pairs belonging to different components
        for (auto& [root, size] : count_size) {
            // current component has 'size' nodes remainingNodes - size = nodes in other components every node in current component can pair with every node in other components
            result += size * (remainingNodes - size);
            // remove current component from remaining nodes
            remainingNodes -= size;
        }
        // return the result
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)