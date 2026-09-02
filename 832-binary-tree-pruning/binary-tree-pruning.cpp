// Brute Force Code
class Solution {
public:
    // check whether the given subtree contains at least one node with value 1
    bool checkone(TreeNode* root) {
        // if the subtree is empty, it does not contain 1
        if (root == NULL) {
            return false;
        }
        // if the current node is 1 found a node with value 1
        if (root->val == 1) {
            return true;
        }
        // search in the left and right subtrees if either side contains 1, return true
        return checkone(root->left) || checkone(root->right);
    }
    TreeNode* pruneTree(TreeNode* root) {
        // if the current node is null there is nothing to prune
        if (root == NULL) {
            return NULL;
        }
        // first recursively prune the right subtree
        pruneTree(root->right);
        // then recursively prune the left subtree
        pruneTree(root->left);
        // check whether the left subtree contains any node with value 1 if it does not contain 1, remove the entire left subtree
        if (!checkone(root->left)) {
            root->left = NULL;
        }
        // check whether the right subtree contains any node with value 1 if it does not contain 1, remove the entire right subtree
        if (!checkone(root->right)) {
            root->right = NULL;
        }
        // if the current node is 0 and has no children it does not contain any 1, so remove this node
        if (root->left == NULL &&
            root->right == NULL &&
            root->val == 0) {
            return NULL;
        }
        // keep the current node
        return root;
    }
};

// Time Complexity : O(N^2)
// Space Complexity : O(N)