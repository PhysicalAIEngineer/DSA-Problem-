// Brute Force Code & Optimal Code
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        // if both nodes are NULL both trees have no node at this position so they are the same
        if (p == NULL && q == NULL) {
            return true;
        }
        // if only one node is NULL the tree structures are different
        if (p == NULL || q == NULL) {
            return false;
        }
        // if the values of the current nodes are different then the trees cannot be the same
        if (p->val != q->val) {
            return false;
        }
        // recursively compare:
        // 1. left subtree of p with left subtree of q
        // 2. right subtree of p with right subtree of q
        // both subtrees must be the same
        return (isSameTree(p->left, q->left) && isSameTree(p->right, q->right)
        );
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)