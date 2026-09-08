# Brute Force Code & Optimal Code
class Solution: 
    def minDepth(self, root): 
        # if the tree is empty there is no root-to-leaf path
        if root is None: 
            return 0 
        # if the current node is a leaf its depth is 1
        if root.left is None and root.right is None: 
            return 1 
        # find the minimum depth of the left subtree if the left child does not exist use infinity so that it is not selected as the minimum depth
        left = self.minDepth(root.left) if root.left else float('inf') 
        # find the minimum depth of the right subtree if the right child does not exist use infinity so that it is not selected as the minimum depth
        right = self.minDepth(root.right) if root.right else float('inf') 
        # add the current node to the minimum depth found from the left or right subtree
        return 1 + min(left, right) 

# Time Complexity : O(N)
# Space Complexity : O(N)