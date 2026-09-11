// Brute Force Code & Optimal Code
class Solution {
public:
    int diameter(TreeNode* root, vector<int>& result) {
        // if node is NULL, its height is 0
        if (root == NULL) {
            return 0;
        }
        // find height of the left subtree
        int left = diameter(root->left, result);
        // find height of the right subtree
        int right = diameter(root->right, result);
        // diameter passing through current node: left subtree height + right subtree height
        result[0] = max(result[0], left + right);
        // return height of current node to its parent can use only one side: left or right
        return max(left, right) + 1;
    }
    int diameterOfBinaryTree(TreeNode* root) {
        // empty tree has diameter 0
        if (root == NULL) {
            return 0;
        }
        // vector is used so recursive function can update the result
        vector<int> result = {INT_MIN};
        // start calculating diameter from root
        diameter(root, result);
        // return the maximum diameter found
        return result[0];
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)