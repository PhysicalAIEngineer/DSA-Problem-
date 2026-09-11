# Brute Force Code & Optimal Code
class Solution:
    def diameter(self, root, result):
        # if node is None, its height is 0
        if root is None:
            return 0
        # find height of the left subtree
        left = self.diameter(root.left, result)
        # find height of the right subtree
        right = self.diameter(root.right, result)
        # fiameter passing through current node: left subtree height + right subtree height
        result[0] = max(result[0], left + right)
        # return height of current node to its parent parent can use only one side: left or right
        return max(left, right) + 1
    def diameterOfBinaryTree(self, root):
        # empty tree has diameter 0
        if root is None:
            return 0
        # list is used so recursive function can update the result
        result = [float('-inf')]
        # start calculating diameter from root
        self.diameter(root, result)
        # return the maximum diameter found
        return result[0]

# Time Complexity : O(N)
# Space Complexity : O(N)