// Brute Force Code & Optimal Code
class Solution {
public:
    // store the number of subtrees whose average is equal to the root value
    int result = 0;
    int sum(TreeNode* root, int& count) {
        // if the node is None its sum is 0
        if (root == NULL) {
            return 0;
        }
        // count the current node
        count++;
        // find the sum of the left subtree
        int l = sum(root->left, count);
        // find the sum of the right subtree
        int r = sum(root->right, count);
        // return the sum of left subtree + right subtree + current node
        return l + r + root->val;
    }
    void solve(TreeNode* root) {
        // if the node is None there is nothing to process
        if (root == NULL) {
            return;
        }
        // store the number of nodes in the current subtree
        int count = 0;
        // calculate the sum of the current subtree and count all its nodes
        int totalSum = sum(root, count);
        // calculate the average of the subtree if average is equal to root value this subtree satisfies the condition
        if (totalSum / count == root->val) {
            result++;
        }
        // check the left subtree
        solve(root->left);
        // check the right subtree
        solve(root->right);
    }
    int averageOfSubtree(TreeNode* root) {
        // reset the result
        result = 0;
        // start checking from the root
        solve(root);
        // return the number of valid subtrees
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)