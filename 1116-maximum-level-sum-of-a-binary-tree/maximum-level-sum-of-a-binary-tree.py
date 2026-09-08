# Brute Force Code & Optimal Code
class Solution: 
    def __init__(self): 
        # dictionary to store: level -> sum of all node values at that level
        self.mp = {} 
    def DFS(self, root, currLevel): 
        # if the current node is empty there is nothing to process
        if root is None: 
            return 
        # if this level is not present in the dictionary initialize its sum as 0
        if currLevel not in self.mp: 
            self.mp[currLevel] = 0 
        # add the current node's value to the sum of this level
        self.mp[currLevel] += root.val 
        # Visit the left subtree and move to the next level
        self.DFS(root.left, currLevel + 1) 
        # Visit the right subtree and move to the next level
        self.DFS(root.right, currLevel + 1) 
    def maxLevelSum(self, root):
        # clear the dictionary in case the same Solution object is reused
        self.mp.clear() 
        # start DFS from level 1
        self.DFS(root, 1) 
        # store the largest level sum found so far start with negative infinity because node values can be negative
        maxSum = float('-inf') 
        # store the level having the maximum sum
        result = 0 
        # check the sum of every level
        for level, sum in self.mp.items(): 
            # if this level has a larger sum than the current maximum
            if sum > maxSum:
                # update the maximum sum
                maxSum = sum 
                # store this level as the answer
                result = level 
        # return the level with the maximum sum
        return result

# Time Complexity : O(N)
# Space Complexity : O(N)