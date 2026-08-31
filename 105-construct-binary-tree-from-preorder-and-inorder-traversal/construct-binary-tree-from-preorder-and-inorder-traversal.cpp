// Brute Force Code & Optimal Code
class Solution {
public:
    TreeNode* solve(vector<int>& preorder, vector<int>& inorder,
                    int start, int end, int& idx) {
        // base case: if the inorder range is invalid there are no nodes left to create.
        if (start > end) {
            return nullptr;
        }
        // preorder traversal: root -> left -> right therefore preorder[idx] is always the root of the current subtree.
        int rootval = preorder[idx];
        // find the position of the root value inside the current inorder range.
        int i = start;
        while (i <= end) {
            // stop when we find the root in inorder.
            if (inorder[i] == rootval) {
                break;
            }
            i++;
        }
        // move to the next preorder element the next element will be the root of the left subtree if it exists.
        idx++;
        // create the TreeNode using the current preorder value.
        TreeNode* root = new TreeNode(rootval);
        // inorder traversal: left subtree -> root -> right subtree therefore, all elements before the root belong to the left subtree.
        root->left = solve(preorder, inorder, start, i - 1, idx);
        // all elements after the root in inorder belong to the right subtree.
        root->right = solve(preorder, inorder, i + 1, end, idx);
        // return the root of the current subtree.
        return root;
    }
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        // number of nodes in the tree.
        int n = preorder.size();
        // store the current index of preorder.
        int idx = 0;
        // start building the tree using the complete inorder range (0 to n - 1).
        return solve(preorder, inorder, 0, n - 1, idx);
    }
};

// Time Complexity : O(N^2)
// Space Complexity : O(N)