// Brute Force Code & Optimal Code
class Solution {
public:
    int minDepth(TreeNode* root) {
        // if the tree is empty there is no root-to-leaf path
        if (root == NULL) {
            return 0;
        }
        // if the current node is a leaf its depth is 1
        if (root->left == NULL && root->right == NULL) {
            return 1;
        }
        // find the minimum depth of the left subtree if the left child does not exist use infinity so that it is not selected as the minimum depth
        int left = root->left ? minDepth(root->left): INT_MAX;
        // find the minimum depth of the right subtree
        // if the right child does not exist use infinity
        // so that it is not selected as the minimum depth
        int right = root->right ? minDepth(root->right): INT_MAX;
        // add the current node to the minimum depth found from the left or right subtree
        return 1 + min(left, right);
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)