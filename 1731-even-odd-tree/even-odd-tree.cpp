// Brute Force Code & Optimal Code
class Solution {
public:
    // store the previous value of each level
    vector<int> levelPrev;
    bool solve(TreeNode* root, int level) {
        // if node is NULL, tree is valid so far
        if (root == NULL) {
            return true;
        }
        // even level -> value must be odd
        // odd level -> value must be even
        if ((level % 2 == 0 && root->val % 2 == 0) || (level % 2 != 0 && root->val % 2 != 0)) {
            return false;
        }
        // add a new entry for this level if needed
        if (level >= levelPrev.size()) {
            levelPrev.push_back(0);
        }
        // check increasing & decreasing order at this level
        if (levelPrev[level] != 0) {
            // even level -> values must be strictly increasing
            if ((level % 2 == 0 && root->val <= levelPrev[level]) ||
                // odd level -> values must be strictly decreasing
                (level % 2 != 0 && root->val >= levelPrev[level])) {
                return false;
            }
        }
        // store current value as the previous value for this level
        levelPrev[level] = root->val;
        // check left and right subtrees
        return solve(root->left, level + 1) && solve(root->right, level + 1);
    }
    bool isEvenOddTree(TreeNode* root) {
        // reset previous values for every new tree
        levelPrev.clear();
        // start DFS from root at level 0
        return solve(root, 0);
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)