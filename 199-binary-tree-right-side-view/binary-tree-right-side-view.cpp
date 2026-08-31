// Brute Force Code & Optimal Code
class Solution {
public:
    void preorder(TreeNode* root, int level, vector<int>& result) {
        // base case: if the current node is null there is nothing to process.
        if (root == nullptr) {
            return;
        }
        // if are visiting this level for the first time store the current node visit the right subtree first, so the first node encountered at each level is the rightmost visible node.
        if (result.size() < level) {
            result.push_back(root->val);
        }
        // visit the right subtree first since this is the right side view the right child should be processed before the left child.
        preorder(root->right, level + 1, result);
        // after completely processing the right subtree visit the left subtree.
        preorder(root->left, level + 1, result);
    }
    vector<int> rightSideView(TreeNode* root) {
        // if the tree is empty there is no right side view.
        if (root == nullptr) {
            return {};
        }
        // store the nodes visible from the right side of the tree.
        vector<int> result;
        // start the modified preorder traversal from the root at level 1.
        preorder(root, 1, result);
        // return the right side view.
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)