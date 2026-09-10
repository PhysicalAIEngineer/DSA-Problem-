// Brute Force Code & Optimal Code
class Solution {
public:
    void convert(TreeNode* current, int parent, unordered_map<int, vector<int>>& adj) {
        // if the current node is NULL there is nothing to process
        if (current == NULL) {
            return;
        }
        // add parent as a neighbor this allows us to move up in the tree
        if (parent != -1) {
            adj[current->val].push_back(parent);
        }
        // add left child as a neighbor
        if (current->left != NULL) {
            adj[current->val].push_back(current->left->val);
        }
        // add right child as a neighbor
        if (current->right != NULL) {
            adj[current->val].push_back(current->right->val);
        }
        // recursively process the left subtree
        convert(current->left, current->val, adj);
        // recursively process the right subtree
        convert(current->right, current->val, adj);
    }
    int amountOfTime(TreeNode* root, int start) {
        // create an adjacency list tree normally allows movement: parent -> child here also need child -> parent so convert the tree into an undirected graph
        unordered_map<int, vector<int>> adj;
        // build the adjacency list
        convert(root, -1, adj);
        // start BFS from the infected node
        queue<int> que;
        que.push(start);
        // keep track of visited nodes to avoid infecting the same node again
        unordered_set<int> visited;
        visited.insert(start);
        // store the number of minutes passed
        int minutes = 0;
        // continue BFS while there are infected nodes that can infect their neighbours
        while (!que.empty()) {
            // number of nodes infected at the current minute
            int n = que.size();
            // process all nodes infected at this level
            while (n > 0) {
                // remove one infected node
                int curr = que.front();
                que.pop();
                // check all neighbours of the current node
                for (int ngbr : adj[curr]) {
                    // if this neighbour is not infected yet
                    if (visited.find(ngbr) == visited.end()) {
                        // infect the neighbour
                        que.push(ngbr);
                        // mark it as visited
                        visited.insert(ngbr);
                    }
                }
                // process the next node of this level
                n--;
            }
            // one complete BFS level = one minute
            minutes++;
        }
        // last BFS level increases minutes once extra so subtract 1
        return minutes - 1;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)