# Brute Force Code & Optimal Code
class Solution:
    def deletehelper(self, root, st, result):
        # if the current node is none there is nothing to process
        if root is None:
            return None
        # first process the left subtrees this ensures children are handled before the current node
        root.left = self.deletehelper(root.left, st, result)
        # process the right subtree
        root.right = self.deletehelper(root.right, st, result)
        # checke if the current node needs to be deleted
        if root.val in st:
            # if the left child exists, if becomes the root of new seprated trees
            if root.left is not None:
                result.append(root.left)
            # if right child exists, if becomes the root of new seprated trees
            if root.right is not None:
                result.append(root.right)
        else:
            # current node does not need to be delected so keep it in the tree
            return root
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        # list will store the root of all remaining trees
        result = []
        # convert to_delete into set so checking whether node should be deleted 
        st = set(to_delete)
        # recurively delete all required nodes
        self.deletehelper(root, st, result)
        # deletehelper() only adds children of deleted nodes to result therefore if the original root ifself is not deleted, need to add it manually
        if root.val not in st:
            result.append(root)
        # return the root of all remaining trees
        return result 

# Time Complexity : O(N)
# Space Complexity : O(N)