# Brute Force Code & Optimal Code
class Solution: 
    def check(self, l, r): 
        # if both nodes are None both sides have ended at the same position so they are symmetric
        if l is None and r is None: 
            return True 
        # if only one node is None the tree structures are different
        if l is None or r is None: 
            return False 
        # For the tree to be symmetric:
        # 1. current node values must be equal
        # 2. left subtree of l must match the right subtree of r
        # 3. right subtree of l must match the left subtree of r
        # notice that we compare in opposite directions because we are checking mirror symmetry.
        if (l.val == r.val  and self.check(l.left, r.right)  and self.check(l.right, r.left)): 
            # both sides are mirror images
            return True 
        # if any of the above conditions fails the tree is not symmetric
        return False 
    def isSymmetric(self, root): 
        # if the tree is empty it is considered symmetric
        if root is None: 
            return True 
        # compare the left and right subtrees of the root as mirror images
        return self.check(root.left, root.right)

# Time Complexity : O(N)
# Space Complexity : O(N)