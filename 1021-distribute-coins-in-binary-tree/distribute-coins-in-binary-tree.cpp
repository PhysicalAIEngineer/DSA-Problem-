// Brute Force Code & Optimal Code
class Solution {
public:
    int solve(TreeNode* root, vector<int>& moves) {
        // if the node is NULL there are no coins or nodes to process
        if (root == NULL) {
            return 0;
        }
        // calculate the extra coins coming from the left subtree
        int l = solve(root->left, moves);
        // calculate the extra coins coming from the right subtree
        int r = solve(root->right, moves);
        // calculate the extra coins that this subtree can send to its parent
        // root->val = coins at current node
        // l         = extra coins from left subtree
        // r         = extra coins from right subtree
        // every node should finally have exactly 1 coin
        int total_extra_candies = (l + r + root->val) - 1;
        // |l| = number of moves needed between current node and left subtree
        // |r| = number of moves needed between current node and right subtree
        // add both to the total number of moves
        moves[0] += abs(l) + abs(r);
        // Return the extra coins:
        // positive -> extra coins available
        // negative -> coins are needed
        return total_extra_candies;
    }
    int distributeCoins(TreeNode* root) {
        // use a vector so that the recursive function can update the same moves value
        vector<int> moves = {0};
        // if the tree has only one node that node already has the required coin
        if (root->left == NULL && root->right == NULL) {
            return 0;
        }
        // start DFS from the root
        solve(root, moves);
        // return the minimum number of moves
        return moves[0];
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)