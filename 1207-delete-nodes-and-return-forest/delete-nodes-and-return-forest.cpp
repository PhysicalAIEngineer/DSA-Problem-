// Brute Force Code & Optimal Code
class Solution {
public:
    TreeNode* deletehelper(TreeNode* root, unordered_set<int>& st, vector<TreeNode*>& result) {
        // if the current node is NULL, there is nothing to process
        if (root == NULL) {
            return NULL;
        }
        // first process the left subtree this ensures children are handled before the current node
        root->left = deletehelper(root->left, st, result);
        // process the right subtree
        root->right = deletehelper(root->right, st, result);
        // check if the current node needs to be deleted
        if (st.find(root->val) != st.end()) {
            // if the left child exists it becomes the root of a new separated tree
            if (root->left != NULL) {
                result.push_back(root->left);
            }
            // if the right child exists it becomes the root of a new separated tree
            if (root->right != NULL) {
                result.push_back(root->right);
            }
            // current node is deleted
            return NULL;
        }
        else {
            // current node does not need to be deleted so keep it in the tree
            return root;
        }
    }
    vector<TreeNode*> delNodes(TreeNode* root, vector<int>& to_delete) {
        // list will store the root of all remaining trees
        vector<TreeNode*> result;
        // convert to_delete into a set so checking whether a node should be deleted is O(1) average
        unordered_set<int> st(to_delete.begin(), to_delete.end());
        // recursively delete all required nodes
        deletehelper(root, st, result);
        // deletehelper() only adds children of deleted nodes to result. Therefore, if the original root itself is not deleted, add it manually.
        if (root != NULL && st.find(root->val) == st.end()) {
            result.push_back(root);
        }
        // return the root of all remaining trees
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)