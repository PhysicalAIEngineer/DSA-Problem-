using namespace std;
class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k
    ) {
        // build the directed weighted graph
        vector<vector<pair<int, int>>> adj(n + 1);
        // iterate through different times
        for (auto& time : times) {
            int u = time[0];
            int v = time[1];
            int w = time[2];
            // add directed edge u --> v with weight w
            adj[u].push_back({v, w});
        }
        // min heap stores (distance, node)
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> min_heap;
        // initially distance of every node is infinity
        vector<int> result(n + 1, INT_MAX);
        // distance of source node k from itself is 0
        result[k] = 0;
        // push source node into the min heap
        min_heap.push({0, k});
        // run Dijkstra algorithm
        while (!min_heap.empty()) {
            // get the node having the smallest distance
            auto [smallest_distance, node] = min_heap.top();
            min_heap.pop();
            // skip processing if a shorter path to this node was already found
            if (smallest_distance > result[node]) {
                continue;
            }
            // visit all neighbours of the current node
            for (auto& neighbours : adj[node]) {
                int adjnode = neighbours.first;
                int distance = neighbours.second;
                // check if a shorter path is found
                if (smallest_distance + distance < result[adjnode]) {
                    result[adjnode] = smallest_distance + distance;
                    // push (new_distance, adjnode) into the min heap
                    min_heap.push({result[adjnode], adjnode
                    });
                }
            }
        }
        // find the maximum shortest distance
        int answer = 0;
        for (int i = 1; i <= n; i++) {
            answer = max(answer, result[i]);
        }
        // if any node is unreachable return -1 otherwise return maximum shortest distance
        return answer == INT_MAX ? -1 : answer;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)