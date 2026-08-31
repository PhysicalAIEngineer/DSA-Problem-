# Brute Force Code & Optimal Code 
class Solution:
    def solve(self, preorder, inorder, start, end, idx):
        # base case : if the inorder range is invalid there are no nodes left to create 
        if start > end:
            return None
        # preorder traversal : root -> left -> right threfore preorder[idx[0]] is always the root of the current subtree
        rootval = preorder[idx[0]]
        # find the position of the root values inside the current inorder range
        i = start
        while i <= end:
            # stop when find the root in inorder
            if inorder[i] == rootval:
                break
            i += 1
        # move the next pointer element will be the root of the left subtree if it exists
        idx[0] += 1
        # create the treenode using the current preorder values
        root = TreeNode(rootval)
        # inorder traversal : left subtree -> root -> right subtree thefore all element before the root belong to the left subtree
        root.left = self.solve(preorder, inorder, start, i - 1, idx)
        # all element after the root is inorder belong to the right subtree
        root.right = self.solve(preorder, inorder, i + 1, end, idx)
        # return the root of the current subtree
        return root
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]: 
        # number fo nodes in the tree
        n = len(preorder)
        # store the current index of preorder 
        idx = [0]
        # start buliding the tree using the complete inorder range (0 to n -1)
        return self.solve(preorder, inorder, 0, n - 1, idx)

# Time Complexity : O(N^2)
# Space Complexity : O(N)
        