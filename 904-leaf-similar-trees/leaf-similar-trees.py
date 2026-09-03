# Brute Force Code & Optimal Code
class Solution:
    def inOrder(self, root, s):
        # if the current node is None there is nothing to process
        if root is None:
            return
        # check if the current node is a leaf node leaf node has no left and right children
        if root.left is None and root.right is None:
            # store the leaf node's value in the list convert the value to string and add "_" as a separator
            s.append(str(root.val) + "_")
            # no need to visit children because a leaf node does not have any children
            return
        # recursively traverse the left subtree
        self.inOrder(root.left, s)
        # recursively traverse the right subtree
        self.inOrder(root.right, s)
    def leafSimilar(self, root1, root2):
        # store the leaf values of the first tree
        s1 = []
        # store the leaf values of the second tree
        s2 = []
        # collect all leaf nodes from the first tree
        self.inOrder(root1, s1)
        # collect all leaf nodes from the second tree
        self.inOrder(root2, s2)
        # compare the two leaf-value sequences if they are exactly the same, return True otherwise, return False
        return s1 == s2

# Time Complexity : O(N)
# Space Complexity : O(N)