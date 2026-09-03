// Optimal Code
class Solution {
public:
    TreeNode* pruneTree(TreeNode* root) {
        // if the current node is NULL, there is nothing to prune
        if (root == NULL) {
            return NULL;
        }
        // recursively prune the left subtree the returned value becomes the new left child
        root->left = pruneTree(root->left);
        // recursively prune the right subtree the returned value becomes the new right child
        root->right = pruneTree(root->right);
        // if the current node is 0 and both children are NULL then this subtree does not contain any 1 so delete the current node by returning NULL
        if (root->left == NULL && root->right == NULL && root->val == 0) {
            return NULL;
        }
        // otherwise, keep the current node
        return root;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)