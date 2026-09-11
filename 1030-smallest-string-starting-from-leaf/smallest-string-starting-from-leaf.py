# Brute Force Code & Optimal Code
class Solution:
    def __init__(self):
        # store the smallest string found so far
        self.result = ""
    def solve(self, root, curr):
        # if node is None, stop
        if root is None:
            return
        # convert node value to character 0 -> 'a', 1 -> 'b', ..., 25 -> 'z' add it to the front because need leaf-to-root string
        curr = chr(root.val + ord('a')) + curr
        # if current node is a leaf
        if root.left is None and root.right is None:
            # update result if this is the first string or if current string is lexicographically smaller
            if self.result == "" or self.result > curr:
                self.result = curr
            return
        # explore left subtree
        self.solve(root.left, curr)
        # explore right subtree
        self.solve(root.right, curr)
    def smallestFromLeaf(self, root):
        # reset result for a fresh traversal
        self.result = ""
        # start DFS with an empty string
        self.solve(root, "")
        # return the smallest leaf-to-root string
        return self.result

# Time Complexity : O(N)
# Space Complexity : O(N)