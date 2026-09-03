// Brute Force Code & Optimal Code
class Solution {
public:
    bool pathSum(TreeNode* root, int sum, int curr) {
        // if the current node is NULL, there is no path to check
        if (root == NULL) {
            return false;
        }
        // check if the current node is a leaf node
        if (root->left == NULL && root->right == NULL) {
            // add the current node's value to the path sum and check whether it equals the target sum
            return (curr + root->val) == sum;
        }
        // recursively check the left subtree add the current node's value to the running sum
        bool left = pathSum(root->left, sum, curr + root->val);
        // recursively check the right subtree add the current node's value to the running sum
        bool right = pathSum(root->right, sum, curr + root->val);
        // return true if a valid path is found in either the left or right subtree
        return left || right;
    }
    bool hasPathSum(TreeNode* root, int sum) {
        // start the recursive process from the root initial path sum is 0
        return pathSum(root, sum, 0);
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)