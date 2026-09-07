# Brute Force Code & Optimal Code
class Solution: 
    def buildBT(self, inorder, postorder, inStart, inEnd, postStart, postEnd): 
        # if the inorder range is empty there is no node to create
        if inStart > inEnd: 
            return None 
        # in postorder traversal, the last element is always the root of the current subtree
        root = TreeNode(postorder[postEnd]) 
        # store the root value
        root_candidate = root.val 
        # search for the root value in inorder
        i = inStart 
 
        # find the position of root in inorder and  everything before root belongs to the left subtree and everything after root belongs to the right subtree
        while i <= inEnd: 
            if inorder[i] == root_candidate: 
                break 
            i += 1 
        # number of nodes in the left subtree
        leftSize = i - inStart 
        # number of nodes in the right subtree
        rightSize = inEnd - i 
        # build the left subtree so, in inorder: left subtree = inStart to i - 1 and in postorder: left subtree contains leftSize nodes starting from postStart
        root.left = self.buildBT(inorder,postorder,inStart,i - 1,postStart,postStart + leftSize - 1) 
        # build the right subtree in inorder: right subtree = i + 1 to inEnd in postorder: right subtree comes after all left subtree nodes
        root.right = self.buildBT(inorder,postorder,i + 1,inEnd,postEnd - rightSize,postEnd - 1) 
        # return the root of the current subtree
        return root 
    def buildTree(self, inorder, postorder): 
        # initially, there is no root
        root = None 
        # number of nodes in the tree
        n = len(postorder) 
        # initial range for inorder
        inStart = 0 
        inEnd = n - 1 
        # initial range for postorder
        postStart = 0 
        postEnd = n - 1 
        # build the complete binary tree
        root = self.buildBT(inorder,postorder,inStart,inEnd,postStart,postEnd) 
        # Return the constructed tree
        return root

# Time Complexity : O(N)
# Space Complexity : O(N)