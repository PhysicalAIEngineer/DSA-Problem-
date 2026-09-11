// Brute Force Code & Optimal Code
class Solution {
public:
    // store the maximum depth found so far
    int maxDepth = -1;
    // store the leftmost value at the deepest level
    int bottomLeft = 0;
    void solve(TreeNode* root, int currDepth) {
        // if node is NULL, stop
        if (root == NULL) {
            return;
        }
        // if reached a new maximum depth
        if (currDepth > maxDepth) {
            // update the maximum depth
            maxDepth = currDepth;
            // since DFS visits left first this is the leftmost node at this depth
            bottomLeft = root->val;
        }
        // first visit the left subtree
        solve(root->left, currDepth + 1);
        // then visit the right subtree
        solve(root->right, currDepth + 1);
    }
    int findBottomLeftValue(TreeNode* root) {
        // reset maximum depth for a fresh traversal
        maxDepth = -1;
        // start DFS from root at depth 0
        solve(root, 0);
        // return the leftmost value at the deepest level
        return bottomLeft;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)