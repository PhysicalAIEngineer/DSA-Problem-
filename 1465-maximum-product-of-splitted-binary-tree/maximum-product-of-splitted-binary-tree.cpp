// Brute Force Code & Optimal Code
class Solution {
public:
    // modulo value used in the final answer
    long long M = 1000000007;
    // stores the total sum of all nodes in the tree
    long long totalSum = 0;
    // stores the maximum product found
    long long maxP = 0;
    long long findTotalSum(TreeNode* root) {
        // if the current node is NULL its subtree sum is 0
        if (root == NULL) {
            return 0;
        }
        // recursively calculate the sum of the left subtree
        long long leftSubtreeSum = findTotalSum(root->left);
        // recursively calculate the sum of the right subtree
        long long rightSubtreeSum = findTotalSum(root->right);
        // calculate the sum of the current subtree = current node + left subtree + right subtree
        long long total = root->val + leftSubtreeSum + rightSubtreeSum;
        // if cut the edge above this subtree one part has sum 'total' and the other part has sum 'totalSum - total'
        long long product = (totalSum - total) * total;
        // update the maximum product found so far
        maxP = max(maxP, product);
        // return the sum of the current subtree
        return total;
    }
    int maxProduct(TreeNode* root) {
        // if the tree is empty, return 0
        if (root == NULL) {
            return 0;
        }
        // reset maximum product
        maxP = 0;
        // first traversal calculates the total sum of the entire tree at this point totalSum is 0 so the products calculated during this traversal are ignored.
        totalSum = findTotalSum(root);
        // second traversal: now that we know the total sum calculate the product for every possible split
        findTotalSum(root);
        // return the maximum product modulo 10^9 + 7
        return maxP % M;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)