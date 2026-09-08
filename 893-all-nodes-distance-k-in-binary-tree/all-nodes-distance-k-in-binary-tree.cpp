// Brute Force Code & Optimal Code
class Solution {
public:
    // dictionary to store the parent of each node
    unordered_map<TreeNode*, TreeNode*> parent;
    void addParent(TreeNode* root) {
        // if the current node is None there is nothing to process
        if (root == NULL) {
            return;
        }
        // if the current node has a left child store the current node as its parent
        if (root->left) {
            parent[root->left] = root;
        }
        // recursively store parents for the left subtree
        addParent(root->left);
        // if the current node has a right child store the current node as its parent
        if (root->right) {
            parent[root->right] = root;
        }
        // recursively store parents for the right subtree
        addParent(root->right);
    }
    void collectKDistanceNodes(TreeNode* target, int k, vector<int>& result) {
        // queue is used for BFS start BFS from the target node
        queue<TreeNode*> que;
        que.push(target);
        // keep track of already visited nodes to avoid visiting the same node again
        unordered_set<int> visited;
        visited.insert(target->val);
        // perform BFS until the queue becomes empty
        while (!que.empty()) {
            // number of nodes at the current distance
            int n = que.size();
            // if k becomes 0 all nodes currently in the queue are exactly k distance away
            if (k == 0) {
                break;
            }
            // process all nodes at the current distance
            while (n > 0) {
                // remove the first node from the queue
                TreeNode* curr = que.front();
                que.pop();
                // move to the left child if it exists and is not visited
                if (curr->left &&
                    visited.find(curr->left->val) == visited.end()) {
                    que.push(curr->left);
                    visited.insert(curr->left->val);
                }
                // move to the right child if it exists and is not visited
                if (curr->right &&
                    visited.find(curr->right->val) == visited.end()) {
                    que.push(curr->right);
                    visited.insert(curr->right->val);
                }
                // move to the parent node if the current node has a parent
                if (parent.find(curr) != parent.end()) {
                    TreeNode* parentNode = parent[curr];
                    // add the parent if it is not visited
                    if (visited.find(parentNode->val) == visited.end()) {
                        que.push(parentNode);
                        visited.insert(parentNode->val);
                    }
                }
                // process the next node at this distance
                n--;
            }
            // move one level farther from the target
            k--;
        }
        // all nodes remaining in the queue are exactly k distance away from target
        while (!que.empty()) {
            TreeNode* temp = que.front();
            que.pop();
            result.push_back(temp->val);
        }
    }
    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        // store the final answer
        vector<int> result;
        // clear the parent dictionary in case the same Solution object is reused
        parent.clear();
        // store the parent of every node
        addParent(root);
        // use BFS to find all nodes exactly k distance away from target
        collectKDistanceNodes(target, k, result);
        // return the answer
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)