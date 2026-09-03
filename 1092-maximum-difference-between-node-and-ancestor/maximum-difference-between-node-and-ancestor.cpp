// Brute Force Code & Optimal Code
class Solution {
public:
    int findMaxDiff(TreeNode* root, int minV, int maxV) {
        // if reach beyond a leaf node return the difference between the minimum and maximum values found on this path
        if (root == NULL) {
            return abs(minV - maxV);
        }
        // update the minimum value seen so far on the current root-to-node path
        minV = min(root->val, minV);
        // update the maximum value seen so far on the current root-to-node path
        maxV = max(root->val, maxV);
        // recursively find the maximum difference in the left subtree
        int l = findMaxDiff(root->left, minV, maxV);
        // recursively find the maximum difference in the right subtree
        int r = findMaxDiff(root->right, minV, maxV);
        // return the larger difference from the left and right subtrees
        return max(l, r);
    }
    int maxAncestorDiff(TreeNode* root) {
        // initially, the root is both the minimum and maximum value on the path
        int minV = root->val;
        int maxV = root->val;
        // start DFS from the root and find the maximum ancestor-descendant difference
        return findMaxDiff(root, minV, maxV);
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)