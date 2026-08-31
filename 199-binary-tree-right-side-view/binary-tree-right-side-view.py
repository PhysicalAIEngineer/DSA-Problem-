class Solution:
    def preorder(self, root, level, result):
        # base case : if the current node is null there is nothing to process
        if not root:
            return 
        # if are visiting this level for the first time store the current node because visit right subtree first the first node encountered at each level is the rightmost visible node
        if len(result) < level:
            result.append(root.val)
        # visit the right subtree first since right side view the right child should be processed before the left child
        self.preorder(root.right, level + 1, result)
        # after completely processing the right subtree visit the left subtree
        self.preorder(root.left, level + 1, result)
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # if tree is empty there is no right side view
        if not root:
            return []
        # store the nodes visible from the right side of the tree
        result = []
        # start the modified preorder traversal from the root at level 1
        self.preorder(root, 1, result)
        # return the right side view
        return result 

# Time Complexity : O(N)
# Space Complexity : O(N)