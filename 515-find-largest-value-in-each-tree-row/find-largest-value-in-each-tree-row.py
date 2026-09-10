# Brute Force Code & Optimal Code
class Solution: 
    def __init__(self): 
        # store the maximum value of each level
        self.result = [] 
    def DFS(self, root, depth): 
        # if the current node is None there is nothing to process
        if root is None: 
            return 
        # if this is the first node are visiting at this depth, add its value to the result
        if depth == len(self.result): 
            self.result.append(root.val) 
        # otherwise, a value already exists for this level
        else: 
            # keep the maximum value between current stored value and current node value
            self.result[depth] = max(self.result[depth], root.val) 
        # visit the left subtree
        self.DFS(root.left, depth + 1) 
        # visit the right subtree
        self.DFS(root.right, depth + 1) 
    def largestValues(self, root): 
        # clear the result list in case the same object is reused
        self.result.clear() 
        # start DFS from the root is at depth 0
        self.DFS(root, 0) 
        # return the maximum value from each level
        return self.result

# Time Complexity : O(N)
# Space Complexity : O(N)