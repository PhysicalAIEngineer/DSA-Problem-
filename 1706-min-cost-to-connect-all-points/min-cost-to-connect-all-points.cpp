// Brute Force Code & Optimal Code
class Solution {
public:
    int minkey(vector<bool>& inMST, vector<int>& key, int v) {
        // initially, minimum index is -1
        int min_index = -1;
        // initially, minimum key value is infinity
        int min_val = INT_MAX;
        // find the vertex with minimum key which is not already included in MST
        for (int i = 0; i < v; i++) {
            // if vertex is not in MST and its key value is smaller
            if (!inMST[i] && key[i] < min_val) {
                min_val = key[i];
                min_index = i;
            }
        }
        // return vertex having minimum key
        return min_index;
    }
    int MinimumSpanningTree(vector<vector<int>>& graph, int v) {
        // key[i] = minimum cost needed to connect vertex i to the MST
        vector<int> key(v, INT_MAX);
        // track which vertices are already included in the MST
        vector<bool> inMST(v, false);
        // start MST from vertex 0
        key[0] = 0;
        // process all v vertices
        for (int count = 0; count < v; count++) {
            // find the unvisited vertex with minimum key
            int u = minkey(inMST, key, v);
            // include vertex u in MST
            inMST[u] = true;
            // check all possible neighbouring vertices
            for (int neighbor = 0; neighbor < v; neighbor++) {
                // check: 1. there is an edge between u and neighbor and 2. neighbor is not already in MST and 3. edge u-neighbor is cheaper than current key
                if (graph[u][neighbor] > 0 && !inMST[neighbor] && graph[u][neighbor] < key[neighbor]) {
                    // update the minimum cost to connect neighbor to the MST
                    key[neighbor] = graph[u][neighbor];
                }
            }
        }
        // return total weight of MST
        return accumulate(key.begin(), key.end(), 0);
    }
    int minCostConnectPoints(vector<vector<int>>& points) {
        // number of points
        int n = points.size();
        // create the complete graph every point can be connected to every other point
        vector<vector<int>> graph(n, vector<int>(n, 0));
        // build complete adjacency matrix using Manhattan distance
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                // calculate Manhattan distance |x1 - x2| + |y1 - y2|
                int manhattan_distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]);
                graph[i][j] = manhattan_distance;
                graph[j][i] = manhattan_distance;
            }
        }
        // find the minimum spanning tree and return its total cost
        return MinimumSpanningTree(graph, n);
    }
};

// Time Complexity : O(N^2)
// Space Complexity : O(N^2)