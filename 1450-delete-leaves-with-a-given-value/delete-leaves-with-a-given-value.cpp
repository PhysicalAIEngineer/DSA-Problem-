// Brute Force Code & Optimal Code
class Solution {
public:
    TreeNode* removeLeafNodes(TreeNode* root, int target) {
        // if current node is NULL, nothing to remove
        if (root == NULL) {
            return NULL;
        }
        // first process the left subtree
        root->left = removeLeafNodes(root->left, target);
        // then process the right subtree
        root->right = removeLeafNodes(root->right, target);
        // after deleting children, check if current node has become a leaf and its value is equal to target
        if (root->left == NULL && root->right == NULL && root->val == target) {
            // remove this leaf node
            return NULL;
        }
        // keep the current node
        return root;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)