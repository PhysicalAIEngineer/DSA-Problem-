# Brute Force Code & Optimal Code
class Solution: 
    def __init__(self): 
        # store the maximum ZigZag path length found
        self.maxPath = 0 
    def solve(self, root, left, right): 
        # if the current node is empty there is no ZigZag path to continue
        if root is None: 
            return 
        # update the maximum ZigZag path found so far
        # 1. 'left'  = zigZag length when the previous move was left
        # 2. 'right' = zigZag length when the previous move was right
        self.maxPath = max(self.maxPath, left, right) 
        # move to the left child if move left now, the next move must be right
        # so: right + 1 becomes the new left-side length 0 resets the right-side length
        self.solve(root.left, right + 1, 0) 
        # move to the right child if move right now, the next move must be left so: 0 resets the left-side length left + 1 becomes the new right-side length
        self.solve(root.right, 0, left + 1) 
    def longestZigZag(self, root):
        # reset the answer
        self.maxPath = 0 
        # start DFS from the root initially, no direction has been taken so both lengths are 0
        self.solve(root, 0, 0) 
        # return the longest ZigZag path found
        return self.maxPath

# Time Complexity : O(N)
# Space Complexity : O(N)