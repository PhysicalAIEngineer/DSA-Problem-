# Brute Force Code & Optimal Code
class Solution:
    def __init__(self):
        # stores the maximum path sum found anywhere in the tree
        self.maxSum = float('-inf')
    def solve(self, root):
        # if the current node is None there is no path to contribute
        if root is None:
            return 0
        # recursively find the maximum path sum that can be extended from the left subtree
        left = self.solve(root.left)
        # recursively find the maximum path sum
        # that can be extended from the right subtree
        right = self.solve(root.right)
        # case 1: path passes through the current root and uses both left and right subtrees
        neeche_hi_milgaya_answer = left + right + root.val
        # case 2: path uses the current root and only ONE of the two subtrees choose whichever side gives the larger sum
        koi_ek_acha = max(left, right) + root.val
        # case 3: path contains only the current root
        only_root_acha = root.val
        # update the global maximum path sum using all three possible cases
        self.maxSum = max(self.maxSum, neeche_hi_milgaya_answer, koi_ek_acha, only_root_acha)
        # return a path that can be extended by the parent can connect to the current root from only one side so we cannot return a path containing both left and right
        return max(koi_ek_acha, only_root_acha)
    def maxPathSum(self, root):
        # reset the global maximum in case the same Solution object is reused
        self.maxSum = float('-inf')
        # start DFS from the root
        self.solve(root)
        # return the maximum path sum found
        return self.maxSum

# Time Complexity : O(N)
# Space Complexity : O(N)