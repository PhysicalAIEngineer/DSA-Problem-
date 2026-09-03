// Brute Force Code & Optimal Code
class Solution {
public:
    // stores the maximum path sum found anywhere in the tree
    int maxSum = INT_MIN;
    int solve(TreeNode* root) {
        // if the current node is NULL there is no path to contribute
        if (root == NULL) {
            return 0;
        }
        // recursively find the maximum path sum that can be extended from the left subtree
        int left = solve(root->left);
        // recursively find the maximum path sum that can be extended from the right subtree
        int right = solve(root->right);
        // case 1: path passes through the current root and uses both left and right subtrees
        int neeche_hi_milgaya_answer =
            left + right + root->val;
        // case 2: path uses the current root and only one of the two subtrees choose whichever side gives the larger sum
        int koi_ek_acha =
            max(left, right) + root->val;
        // case 3: path contains only the current root
        int only_root_acha = root->val;
        // update the global maximum path sum using all three possible cases
        maxSum = max({maxSum, neeche_hi_milgaya_answer, koi_ek_acha,only_root_acha});
        // return a path that can be extended by the parent parent can connect to the current root from only one side so cannot return a path containing both left and right
        return max(koi_ek_acha, only_root_acha);
    }
    int maxPathSum(TreeNode* root) {
        // reset the global maximum in case the same Solution object is reused
        maxSum = INT_MIN;
        // Start DFS from the root
        solve(root);
        // return the maximum path sum found
        return maxSum;
    }
};

// Time Complexity : O(N)
// Space COmplexity : O(N)