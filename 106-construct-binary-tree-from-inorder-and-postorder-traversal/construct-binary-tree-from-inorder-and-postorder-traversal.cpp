// Brute Force Code & Optimal Code
class Solution {
public:
    TreeNode* buildBT(vector<int>& inorder, vector<int>& postorder,int inStart, int inEnd,int postStart, int postEnd) {
        // if the inorder range is empty there is no node to create
        if (inStart > inEnd) {
            return NULL;
        }
        // in postorder traversal, the last element is always the root of the current subtree
        TreeNode* root = new TreeNode(postorder[postEnd]);
        // store the root value
        int root_candidate = root->val;
        // search for the root value in inorder
        int i = inStart;
        // find the position of root in inorder everything before root belongs to the left subtree and everything after root belongs to the right subtree
        while (i <= inEnd) {
            if (inorder[i] == root_candidate) {
                break;
            }
            i++;
        }
        // number of nodes in the left subtree
        int leftSize = i - inStart;
        // number of nodes in the right subtree
        int rightSize = inEnd - i;
        // build the left subtree in inorder: left subtree = inStart to i - 1 in postorder: left subtree contains leftSize nodes starting from postStart
        root->left = buildBT(inorder, postorder, inStart, i - 1, postStart,postStart + leftSize - 1);
        // build the right subtree
        // in inorder: right subtree = i + 1 to inEnd
        // in postorder: right subtree comes after all left subtree nodes
        root->right = buildBT(inorder,postorder,i + 1,inEnd,postEnd - rightSize,postEnd - 1);
        // return the root of the current subtree
        return root;
    }
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        // initially, there is no root
        TreeNode* root = NULL;
        // number of nodes in the tree
        int n = postorder.size();
        // initial range for inorder
        int inStart = 0;
        int inEnd = n - 1;
        // initial range for postorder
        int postStart = 0;
        int postEnd = n - 1;
        // build the complete binary tree
        root = buildBT(inorder,postorder,inStart,inEnd,postStart,postEnd);
        // return the constructed tree
        return root;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)