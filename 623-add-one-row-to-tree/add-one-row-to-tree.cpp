// Brute Force Code & Optimal Code
class Solution {
public:
    TreeNode* add(TreeNode* root, int val, int depth, int curr) {
        // if the current node is NULL, there is no node to process
        if (root == NULL) {
            return NULL;
        }
        // If are at the level just above the target depth need to insert new nodes below the current node
        if (curr == depth - 1) {
            // save the original left and right children because they must not be lost
            TreeNode* lTemp = root->left;
            TreeNode* rTemp = root->right;
            // create new nodes with the given value and make them the new left and right children
            root->left = new TreeNode(val);
            root->right = new TreeNode(val);
            // connect the original left subtree to the left child of the new left node
            root->left->left = lTemp;
            // connect the original right subtree to the right child of the new right node
            root->right->right = rTemp;
            // return the current node after inserting the new row
            return root;
        }
        // recursively move to the left subtree increase the current depth by 1
        root->left = add(root->left, val, depth, curr + 1);
        // recursively move to the right subtree increase the current depth by 1
        root->right = add(root->right, val, depth, curr + 1);
        // return the current root
        return root;
    }
    TreeNode* addOneRow(TreeNode* root, int val, int depth) {
        // if the required depth is 1 the new node must become the new root
        if (depth == 1) {
            // create a new root with the given value
            TreeNode* newRoot = new TreeNode(val);
            // make the original tree the left child of the new root
            newRoot->left = root;
            // return the new root
            return newRoot;
        }
        // start recursion from the original root is considered to be at depth 1
        return add(root, val, depth, 1);
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)