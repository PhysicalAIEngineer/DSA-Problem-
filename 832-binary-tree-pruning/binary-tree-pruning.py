# Optimal Code
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if the current node is none there is nothing to prune
        if root is None:
            return None
        # recursively prune the left substree the returned values becomes the new left child
        root.left = self.pruneTree(root.left)
        # recursively prune the right subtree the returned values becomes the new right child
        root.right = self.pruneTree(root.right)
        # if the current node is 0 and both children are none then this subtree does not contain any 1 so delete the current node by returning none
        if root.left is None and root.right is None and root.val == 0:
            return None
        # otherwise keep the current node
        return root

# Time Complexity : O(N)
# Space COmlexity : O(N)