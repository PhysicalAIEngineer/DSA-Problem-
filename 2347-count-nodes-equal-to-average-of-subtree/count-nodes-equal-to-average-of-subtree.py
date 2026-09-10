# Brute Force Code & Optimal Code
class Solution: 
    def __init__(self): 
        # store the number of subtrees whose average is equal to the root value
        self.result = 0 
    def sum(self, root, count): 
        # if the node is None its sum is 0
        if root is None: 
            return 0 
        # count the current node
        count[0] += 1 
        # find the sum of the left subtree
        l = self.sum(root.left, count) 
        # find the sum of the right subtree
        r = self.sum(root.right, count) 
        # return the sum of: left subtree + right subtree + current node
        return l + r + root.val 
    def solve(self, root):
        # if the node is None there is nothing to process
        if root is None: 
            return 
        # store the number of nodes in the current subtree
        count = [0] 
        # calculate the sum of the current subtree and count all its nodes
        totalSum = self.sum(root, count) 
        # calculate the average of the subtree if average is equal to root value this subtree satisfies the condition
        if totalSum // count[0] == root.val: 
            self.result += 1 
        # check the left subtree
        self.solve(root.left) 
        # check the right subtree
        self.solve(root.right) 
    def averageOfSubtree(self, root):
        # reset the result
        self.result = 0 
        # start checking from the root
        self.solve(root) 
        # return the number of valid subtrees
        return self.result

# Time Complexity : O(N)
# Space Complexity : O(N)