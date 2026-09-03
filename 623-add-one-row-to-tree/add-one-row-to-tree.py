# Brute Force Code & Optimal Code
class Solution:
    def add(self, root, val, depth, curr):
        # if the current node is none there is no node to process
        if root is None:
            return None
        # if are at the level just above the target depth need to insert new nodes below the current node
        if curr == depth - 1:
            # save the original left and right children because they must not be lost
            lTemp = root.left
            rTemp = root.right
            # create new nodes with the given value and make them the new left and right children
            root.left = TreeNode(val)
            root.right = TreeNode(val)
            # connect the original left subtree to the left child of the new left node
            root.left.left = lTemp
            # connect the original right subtree to the right child of the new right node
            root.right.right = rTemp
            # return the current node after inserting the new row
            return root
        # recursively move to the left subtree increase the current depth by 1
        root.left = self.add(root.left, val, depth, curr + 1)
        # recursively move to the right subtree increase the current depth by 1
        root.right = self.add(root.right, val, depth, curr + 1)
        # return the current root
        return root
    def addOneRow(self, root, val, depth):
        # if the required depth is 1 the new nodes must become the new root
        if depth == 1:
            # create a new root with the given value
            newRoot = TreeNode(val)
            # make the original tree the left child of the new root
            newRoot.left = root
            # return the new root
            return newRoot
        # start recursion from the original root root is considered to be at depth 1
        return self.add(root, val, depth, 1)

# Time Complexity : O(N)
# Space Complexity : O(N)