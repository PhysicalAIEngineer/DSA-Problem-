# Brute Force Code 
class Solution:
    # check whether the given subtree contains at least one node with values 1
    def checkone(self, root):
        # if the subtree is empty it does not contain 1
        if root is None:
            return False
        # if the current node is 1 found node with value 1
        if root.val == 1:
            return True
        # search in the left and right subtrees if either side contains 1 return true
        return self.checkone(root.left) or self.checkone(root.right)
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if the current node is node there is nothing to prune
        if root is None:
            return None
        # first recursively prune the right subtree
        self.pruneTree(root.right)
        # then recursively prune the left subtree      
        self.pruneTree(root.left)
        # check whehter the left subtree contain any node with value 1 if if does not contain 1 remove the entire left subtree
        if not self.checkone(root.left):
            root.left = None
        # check whether the right subtree contain any node with value 1 if the does not contain 1 remove the entire right subtree
        if not self.checkone(root.right):
            root.right = None
        # if the current node is 0 and has no children it does not contain any 1 so remove this node
        if root.left is None and root.right is None and root.val == 0:
            return None
        # keep the current node
        return root 

# Time Complexity : O(N^2)
# Space Complexity : O(N) 