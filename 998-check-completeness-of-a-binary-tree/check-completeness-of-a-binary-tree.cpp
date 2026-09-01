// Brute Force Code & Optimal Code
class Solution {
public:
    int countnodes(TreeNode* root) {
        // base case: if the current node is NULL this subtree contains 0 nodes.
        if (root == nullptr) {
            return 0;
        }
        // count the current node as 1 then recursively count:
        // 1. all nodes in the left subtree
        // 2. all nodes in the right subtree
        // Total = current node + left subtree + right subtree
        return 1 + countnodes(root->left) + countnodes(root->right);
    }
    bool DFS(TreeNode* root, int i, int totalnodes) {
        // if the current node is NULL there is no invalid node on this path therefore this path is valid.
        if (root == nullptr) {
            return true;
        }
        // in a complete binary tree, nodes are assigned positions using array indexing.
        // if a node has index i:
        //  left child  -> 2 * i
        //  right child -> 2 * i + 1
        // if a node gets an index greater than the total number of nodes, there must be a missing position before this node therefore, the tree is not complete.
        if (i > totalnodes) {
            return false;
        }
        // recursively check both subtrees:
        //  1. left child index  -> 2 * i
        //  2. right child index -> 2 * i + 1
        // both subtrees must satisfy the indexing rules.
        return DFS(root->left, 2 * i, totalnodes) && DFS(root->right, 2 * i + 1, totalnodes);
    }
    bool isCompleteTree(TreeNode* root) {
        // first count the total number of nodes present in the tree.
        int totalnodes = countnodes(root);
        // assign index 1 to the root.
        int i = 1;
        // start DFS from the root every existing node must have an index less than or equal to totalnodes.
        return DFS(root, i, totalnodes);
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)