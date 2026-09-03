// Brute Force Code & Optimal Code
class Solution {
public:
    void inOrder(TreeNode* root, vector<string>& s) {
        // if the current node is NULL, there is nothing to process
        if (root == NULL) {
            return;
        }
        // check if the current node is a leaf node leaf node has no left and right children
        if (root->left == NULL && root->right == NULL) {
            // store the leaf node's value in the list convert the value to string and add "_" as a separator
            s.push_back(to_string(root->val) + "_");
            // no need to visit children because a leaf node does not have any children
            return;
        }
        // recursively traverse the left subtree
        inOrder(root->left, s);
        // recursively traverse the right subtree
        inOrder(root->right, s);
    }
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        // store the leaf values of the first tree
        vector<string> s1;
        // store the leaf values of the second tree
        vector<string> s2;
        // collect all leaf nodes from the first tree
        inOrder(root1, s1);
        // collect all leaf nodes from the second tree
        inOrder(root2, s2);
        // compare the two leaf-value sequences if they are exactly the same, return true otherwise, return false
        return s1 == s2;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)