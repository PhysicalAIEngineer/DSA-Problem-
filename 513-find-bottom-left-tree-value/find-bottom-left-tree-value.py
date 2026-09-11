# Brute Force Code & Optimal Code
class Solution:
    def __init__(self):
        # store the maximum depth found so far
        self.maxDepth = -1
        # store the leftmost value at the deepest level
        self.bottomLeft = 0
    def solve(self, root, currDepth):
        # if node is None, stop
        if root is None:
            return
        # if reached a new maximum depth
        if currDepth > self.maxDepth:
            # update the maximum depth
            self.maxDepth = currDepth
            # since DFS visits left first this is the leftmost node at this depth
            self.bottomLeft = root.val
        # first visit the left subtree
        self.solve(root.left, currDepth + 1)
        # then visit the right subtree
        self.solve(root.right, currDepth + 1)
    def findBottomLeftValue(self, root):
        # reset maximum depth for a fresh traversal
        self.maxDepth = -1
        # start DFS from root at depth 0
        self.solve(root, 0)
        # return the leftmost value at the deepest level
        return self.bottomLeft

# Time Complexity : O(N)
# Space Complexity : O(N)