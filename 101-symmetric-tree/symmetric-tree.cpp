// Brute Force Code & Optimal Code
class Solution {
public:
    bool check(TreeNode* l, TreeNode* r) {
        // if both nodes are NULL both sides have ended at the same position so they are symmetric
        if (l == NULL && r == NULL) {
            return true;
        }
        // if only one node is NULL, the tree structures are different
        if (l == NULL || r == NULL) {
            return false;
        }
        // For the tree to be symmetric:
        // 1. current node values must be equal
        // 2. left subtree of l must match the right subtree of r
        // 3. right subtree of l must match the left subtree of r
        // notice that we compare in opposite directions because we are checking mirror symmetry.
        if (l->val == r->val && check(l->left, r->right) && check(l->right, r->left)) {
            // both sides are mirror images
            return true;
        }
        // if any of the above conditions fails the tree is not symmetric
        return false;
    }
    bool isSymmetric(TreeNode* root) {
        // if the tree is empty it is considered symmetric
        if (root == NULL) {
            return true;
        }
        // compare the left and right subtrees of the root as mirror images
        return check(root->left, root->right);
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)