# Brute Force Code & Optimal Code
class Solution:
    def findMaxDiff(self, root, minV, maxV):
        # if reach beyond a leaf node return the difference between the minimum and maximum values found on this path
        if root is None:
            return abs(minV - maxV)
        # update the minimum value seen so far on the current root-to-node path
        minV = min(root.val, minV)
        # update the maximum value seen so far on the current root-to-node path
        maxV = max(root.val, maxV)
        # recursively find the maximum difference in the left subtree
        l = self.findMaxDiff(root.left, minV, maxV)
        # recursively find the maximum difference in the right subtree
        r = self.findMaxDiff(root.right, minV, maxV)
        # return the larger difference from the left and right subtrees
        return max(l, r)
    def maxAncestorDiff(self, root):
        # initially, the root is both the minimum and maximum value on the path
        minV = root.val
        maxV = root.val
        # start DFS from the root and find the maximum ancestor-descendant difference
        return self.findMaxDiff(root, minV, maxV)

# Time Complexity : O(N)
# Space Complexity : O(N)