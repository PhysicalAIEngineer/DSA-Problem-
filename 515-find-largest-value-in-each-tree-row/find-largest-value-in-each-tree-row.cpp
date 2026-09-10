// Brute Force Code & Optimal Code
class Solution {
public:
    // store the maximum value of each level
    vector<int> result;
    void DFS(TreeNode* root, int depth) {
        // if the current node is None there is nothing to process
        if (root == NULL) {
            return;
        }
        // if this is the first node we are visiting at this depth add its value to the result
        if (depth == result.size()) {
            result.push_back(root->val);
        }
        // otherwise, a value already exists for this level
        else {
            // keep the maximum value between current stored value and current node value
            result[depth] = max(result[depth], root->val);
        }
        // visit the left subtree
        DFS(root->left, depth + 1);
        // visit the right subtree
        DFS(root->right, depth + 1);
    }
    vector<int> largestValues(TreeNode* root) {
        // clear the result list in case the same object is reused
        result.clear();
        // start DFS from the root at depth 0
        DFS(root, 0);
        // return the maximum value from each level
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)