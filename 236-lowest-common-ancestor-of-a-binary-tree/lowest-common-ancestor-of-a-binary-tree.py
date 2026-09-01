# Brute Force Code & Optimal Code
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # base case : if the current node is none, there is nothing to search
        if root is None:
            return None
        # if the current node is either p or q then this node could be the lowest common ancestor
        if root.val == p.val or root.val == q.val:
            return root
        # recursively search for p and q in the left subtree
        left = self.lowestCommonAncestor(root.left, p, q)
        # recursively search for p and 1 in the right subtree
        right = self.lowestCommonAncestor(root.right, p, q)
        # if one target node is found in the left subtree and the other target node is found in the right subtree then the current root is their lowest common ancestor
        if left is not None and right is not None:
            return root
        # if only the left subtree contain p or q return that node otherwise return the node found in the right subtree
        return left if left is not None else right 

# Time Complexity : O(N)
# Space Complexity : O(N)        