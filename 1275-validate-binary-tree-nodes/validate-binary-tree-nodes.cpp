// Brute Force Code & Optimal Code
class Solution {
public:
    bool validateBinaryTreeNodes(int n, vector<int>& leftChild,
                                 vector<int>& rightChild) {
        // store the children of every parent node
        unordered_map<int, vector<int>> parent_to_children;
        // store the parent of every child node
        unordered_map<int, int> child_to_parent;
        // process every node
        for (int i = 0; i < n; i++) {
            // current node
            int node = i;
            // get its left and right children
            int leftC = leftChild[i];
            int rightC = rightChild[i];
            // process left child -1 means there is no left child
            if (leftC != -1) {
                // create an empty list for this parent if it does not exist
                if (parent_to_children.find(node) ==
                parent_to_children.end()) {parent_to_children[node] = {};
                }
                // store the left child
                parent_to_children[node].push_back(leftC);
                // child cannot have two different parents if this child already has a parent the tree is invalid
                if (child_to_parent.find(leftC) !=
                    child_to_parent.end()) {
                    return false;
                }
                // store the parent of the left child
                else {
                    child_to_parent[leftC] = node;
                }
            }
            // process right child -1 means there is no right child
            if (rightC != -1) {
                // create an empty list for this parent if it does not exist
                if (parent_to_children.find(node) ==
                parent_to_children.end()) {parent_to_children[node] = {};
                }
                // store the right child
                parent_to_children[node].push_back(rightC);
                // child cannot have two different parents
                if (child_to_parent.find(rightC) !=
                    child_to_parent.end()) {
                    return false;
                }
                // store the parent of the right child
                else {
                    child_to_parent[rightC] = node;
                }
            }
        }
        // find the root initially, no root is found
        int root = -1;
        // root is a node which has no parent
        for (int i = 0; i < n; i++) {
            // node is not present as a child so it does not have a parent
            if (child_to_parent.find(i) == child_to_parent.end()) {
                // there must be exactly one root if another root is already found the structure has multiple roots
                if (root != -1) {
                    return false;
                }
                // store this node as the root
                else {
                    root = i;
                }
            }
        }
        // if no root exists there is a cycle or invalid structure
        if (root == -1) {
            return false;
        }
        // check connectivity using BFS keep track of visited nodes
        vector<bool> visited(n, false);
        // queue for BFS
        queue<int> que;
        // start with the root
        int count = 1;
        que.push(root);
        visited[root] = true;
        // perform BFS
        while (!que.empty()) {
            // next node
            int node = que.front();
            que.pop();
            // visit all children of this node
            if (parent_to_children.find(node) != parent_to_children.end()) {
                for (int child : parent_to_children[node]) {
                    // if the child has not been visited
                    if (!visited[child]) {
                        // mark it as visited
                        visited[child] = true;
                        // increase the number of reachable nodes
                        count++;
                        // add the child to the queue
                        que.push(child);
                    }
                }
            }
        }
        // valid binary tree must contain all n nodes and be connected
        return count == n;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)