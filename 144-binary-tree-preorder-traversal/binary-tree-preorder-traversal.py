# Brute Force & Optimal Code
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # if the tree is empty return empty list
        if not root:
            return []
        # stack is used to simulate start with the root node
        stack = [root]
        # store the preorders traversal result
        result = []
        # continue until there are no nodes left to process
        while stack:
            # pop the top node from the stack
            node = stack.pop()
            #  visit the node (preorder : node -> left -> right)
            result.append(node.val)
            # push right child first so the left child is processed first since stack is LIFO 
            if node.right:
                stack.append(node.right)
            # push the left child after right
            if node.left:
                stack.append(node.left)
        # return the preorders traversal result
        return result

# Time Complexity : O(N)
# Space Complexity : O(1)