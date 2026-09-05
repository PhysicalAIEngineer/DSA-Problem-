# Brute Force Code & Optimal Code
class Solution: 
    def isSameTree(self, p, q): 
        # if both nodes are None both trees have no node at this position so they are the same
        if p is None and q is None: 
            return True 
        # if only one node is None the tree structures are different
        if p is None or q is None: 
            return False 
        # if the values of the current nodes are different then the trees cannot be the same
        if p.val != q.val: 
            return False 
        # Recursively compare:
        # 1. Left subtree of p with left subtree of q
        # 2. Right subtree of p with right subtree of q
        # Both subtrees must be the same
        return ( self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)) 

# Time Complexity : O(N)
# Space Complexity : O(N)