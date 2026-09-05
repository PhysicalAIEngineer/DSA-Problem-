class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        // if the tree is empty return empty list
        if (root == nullptr) {
            return {};
        }
        // stack is used to simulate recursion start with the root node
        stack<TreeNode*> stack;
        // store the preorders traversal result
        vector<int> result;
        // push root node 
        stack.push(root);
        // continue until there are no nodes left to process
        while (!stack.empty()) {
            // pop the top node from the stack    
            TreeNode* node = stack.top();
            stack.pop();
            // visit the node (preorder : node -> left -> right)
            result.push_back(node->val);
            // push right child first so the left child is processed first since stack is LIFO
            if (node->right != nullptr) {
                stack.push(node->right);
            }
            // push the left child after right child
            if (node->left != nullptr) {
                stack.push(node->left);
            }
        }
        // return the preorders traversal result
        return result;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(H)