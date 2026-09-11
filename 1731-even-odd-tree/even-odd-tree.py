# Brute Force Code & Optimal Code
class Solution:
    def __init__(self):
        # store the previous value of each level
        self.levelPrev = []
    def solve(self, root, level):
        # if node is None, tree is valid so far
        if root is None:
            return True
        # even level -> value must be odd
        # odd level -> value must be even
        if ((level % 2 == 0 and root.val % 2 == 0) or (level % 2 != 0 and root.val % 2 != 0)):
            return False
        # add a new entry for this level if needed
        if level >= len(self.levelPrev):
            self.levelPrev.append(0)
        # check increasing & decreasing order at this level
        if self.levelPrev[level] != 0:
            # even level -> values must be strictly increasing
            if ((level % 2 == 0 and root.val <= self.levelPrev[level]) or
                # odd level -> values must be strictly decreasing
                (level % 2 != 0 and root.val >= self.levelPrev[level])):
                return False
        # store current value as the previous value for this level
        self.levelPrev[level] = root.val
        # check left and right subtrees
        return (self.solve(root.left, level + 1) and self.solve(root.right, level + 1))
    def isEvenOddTree(self, root):
        # reset previous values for every new tree
        self.levelPrev = []
        # start DFS from root at level 0
        return self.solve(root, 0)

# Time Complexity : O(N)
# Space Complexity : O(N)