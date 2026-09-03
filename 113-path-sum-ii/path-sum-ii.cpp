// Brute Force Code & Optimal Code
class Solution {
public:
    void collectpaths(TreeNode* root, int curr, vector<int>& temp,vector<vector<int>>& result) {
        // if the current node is null, there is no path to process
        if (root == NULL) {
            return;
        }
        // add the current node value to the current path
        temp.push_back(root->val);
        // check if the current node is a leaf node and its value is equal to the remaining required sum
        if (root->left == NULL &&
            root->right == NULL &&
            root->val == curr) {
            // valid root-to-leaf path is found make a copy of temp and store it in result
            result.push_back(temp);
        }
        // move to the left subtree subtract the current node value from the remaining sum
        collectpaths(root->left, curr - root->val, temp,result);
        // move to the right subtree subtract the current node value from the remaining sum
        collectpaths(root->right, curr - root->val, temp,result);
        // backtrack: remove the current node after returning to the parent
        temp.pop_back();
    }
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        // list stores all valid paths
        vector<vector<int>> result;
        // temporary vector used to build the current path
        vector<int> temp;
        // start DFS traversal from the root sum is the required target sum
        collectpaths(root, sum, temp, result);
        // return all root-to-leaf paths whose sum equals the target
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)