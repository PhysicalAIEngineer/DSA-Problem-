// Brute Force Code & Optimal Code
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        // base case: if the current node is NULL, there is nothing to search
        if (root == nullptr) {
            return nullptr;
        }
        // if the current node is either p or q this node could be the lowest common ancestor
        if (root->val == p->val || root->val == q->val) {
            return root;
        }
        // recursively search for p and q in the left subtree
        TreeNode* left = lowestCommonAncestor(root->left, p, q);
        // recursively search for p and q in the right subtree
        TreeNode* right = lowestCommonAncestor(root->right, p, q);
        // if one target is found in the left subtree and the other is found in the right subtree the current root is their lowest common ancestor
        if (left != nullptr && right != nullptr) {
            return root;
        }
        // if only the left subtree contains p or q, return left otherwise, return the node found in the right subtree.
        return (left != nullptr) ? left : right;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)
