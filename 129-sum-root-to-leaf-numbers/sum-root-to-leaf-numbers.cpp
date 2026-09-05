// Brute Force Code & Optimal Code
class Solution {
public:
    int find(TreeNode* root, int curr) {
        // if the current node is empty there is no number to form from this path
        if (root == NULL) {
            return 0;
        }
        // add the current digit to the number
        // example: curr = 12, root->val = 3
        // new curr = 12 * 10 + 3 = 123
        curr = curr * 10 + root->val;
        // if this is a leaf node the complete root-to-leaf number is formed
        if (root->left == NULL && root->right == NULL) {
            return curr;
        }
        // recursively find the number formed from the left subtree
        int left_num = find(root->left, curr);
        // recursively find the number formed from the right subtree
        int right_num = find(root->right, curr);
        // add numbers formed from both paths
        return left_num + right_num;
    }
    int sumNumbers(TreeNode* root) {
        // start DFS from root with current number = 0 the function returns the sum of all root-to-leaf numbers
        return find(root, 0);
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)