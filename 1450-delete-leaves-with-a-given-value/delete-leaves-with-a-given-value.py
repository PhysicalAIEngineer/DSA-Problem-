# Brute Force Code & Optimal Code
class Solution:
    def removeLeafNodes(self, root, target):
        # if current node is None, nothing to remove
        if root is None:
            return None
        # first process the left subtree
        root.left = self.removeLeafNodes(root.left, target)
        # then process the right subtree
        root.right = self.removeLeafNodes(root.right, target)
        # after deleting children, check if current node has become a leaf and its value is equal to target
        if (root.left is None and root.right is None and root.val == target):
            # remove this leaf node
            return None
        # keep the current node
        return root

# Time Complexity : O(N)
# Space Complexity : O(N)