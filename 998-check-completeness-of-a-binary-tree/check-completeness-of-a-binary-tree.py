# Brute Force Code & Optimal Code 
class Solution:
    def countnodes(self, root):
        # base case : if the current node is full this subtree contain 0 nodes
        if root is None:
            return 0
        # count the current node as 1 then recursively count : 1. all node in the left subtree & 2. all node is the right subtree so, total = current node + left subtree + right subtree
        return (1 + self.countnodes(root.left) + self.countnodes(root.right))
    def DFS(self , root, i, totalnodes):
        # if the current node is null, there is no invalid node on this path therefore this path is valid
        if root is None:
            return True
        # in complete binary tree nodes are assigned positions using array indexing if node has index i : left child -> 2 * i & right child -> 2 * i + 1 so if nodes get as index greater than the total number of nodes there must be missing position before this node that mean the tree is not complete
        if i > totalnodes:
            return False
        # recusively check both subtree : 1. left child index (2 * i) and 2. right child index (2 * i + 1) so both subtrees must satisfy the indexing rules
        return (self.DFS(root.left, 2 * i, totalnodes) and self.DFS(root.right, 2 * i + 1, totalnodes))
    def isCompleteTree(self, root):
        # first count the total number of nodes present in the trees
        totalnodes = self.countnodes(root)
        # assign index 1 to the root
        i = 1
        # start DFS from the root every exisiting nodes must have as index less than or equal to totalnodes
        return self.DFS(root, i, totalnodes)

# Time Complexity : O(N)
# Space Complexity : O(N)

        