// Brute Force Code & Optimal Code
class Solution {
public:
    // store the smallest string found so far
    string result = "";
    void solve(TreeNode* root, string curr) {
        // if node is NULL, stop
        if (root == NULL) {
            return;
        }
        // convert node value to character 0 -> 'a', 1 -> 'b', ..., 25 -> 'z' add it to the front because need leaf-to-root string
        curr = char(root->val + 'a') + curr;
        // if current node is a leaf
        if (root->left == NULL && root->right == NULL) {
            // update result if this is the first string or if current string is lexicographically smaller
            if (result == "" || result > curr) {
                result = curr;
            }
            return;
        }
        // explore left subtree
        solve(root->left, curr);
        // explore right subtree
        solve(root->right, curr);
    }
    string smallestFromLeaf(TreeNode* root) {
        // reset result for a fresh traversal
        result = "";
        // start DFS with an empty string
        solve(root, "");
        // return the smallest leaf-to-root string
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)