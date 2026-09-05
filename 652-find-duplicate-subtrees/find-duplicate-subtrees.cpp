// Brute Force Code & Optimal Code
class Solution {
public:
    string DFS(TreeNode* root, unordered_map<string, int>& mp,vector<TreeNode*>& res) {
        // if the node is empty return "NULL" to represent an empty subtree need this so that different tree structures do not produce the same string.
        if (root == NULL) {
            return "NULL";
        }
        // create a unique string representation of the current subtree format: root value + left subtree + right subtree
        string s = (to_string(root->val) + "," + DFS(root->left, mp, res) + "," + DFS(root->right, mp, res));
        // check how many times this subtree has already appeared if frequency is exactly 1, this is the second occurrence of the same subtree.
        if (mp[s] == 1) {
            // store the root of this duplicate subtree in the result.
            res.push_back(root);
        }
        // increase the frequency of this subtree.
        mp[s]++;
        // return the string representation so the parent node can use it to build its own subtree representation.
        return s;
    }
    vector<TreeNode*> findDuplicateSubtrees(TreeNode* root) {
        // dictionary to store: subtree representation -> frequency
        unordered_map<string, int> mp;
        // stores the roots of duplicate subtrees.
        vector<TreeNode*> res;
        // start DFS from the root to generate representations of all subtrees.
        DFS(root, mp, res);
        // return all duplicate subtree roots.
        return res;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)