# Brute Force Code & Optimal Code
class Solution:
    def pathSum(self, root, sum, curr):
        # if the current node is None there is no path to check
        if root is None:
            return False
        # check if the current node is a leaf node
        if root.left is None and root.right is None:
            # add the current node's value to the path sum and check whether it equals the target sum
            return (curr + root.val) == sum
        # recursively check the left subtree add the current node's value to the running sum
        left = self.pathSum(root.left, sum, curr + root.val)
        # recursively check the right subtree add the current node's value to the running sum
        right = self.pathSum(root.right, sum, curr + root.val)
        # return True if a valid path is found in either the left or right subtree
        return left or right
    def hasPathSum(self, root, sum):
        # start the recursive process from the root initial path sum is 0
        return self.pathSum(root, sum, 0)

# Time Complexity : O(N)
# Space Complexity : O(N)