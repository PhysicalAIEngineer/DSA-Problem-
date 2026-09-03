# Brute Force Code & Optimal Code
class Solution:
    def collectpaths(self, root, curr, temp, result):
        # if the current node is none there is no path to process 
        if root is None:
            return 
        # add the current node values to current path
        temp.append(root.val)
        # check if the current node is leaf node and its values is equal to the remaining required sum
        if root.left is None and root.right is None and root.val == curr:
            # valid root to leaf path is found make copy of temp and store it in result
            result.append(temp.copy())
        # move to the left subtree subtract the current node value from the remaining sum
        self.collectpaths(root.left, curr - root.val, temp, result)
        # move to the right subtree subtract the current node value from the remaining sum
        self.collectpaths(root.right, curr - root.val, temp, result)
        # backtrack remove the current node after returning to the present
        temp.pop()
    def pathSum(self, root, sum):
        # list store all valid paths
        result = []
        # temporary list used to bulid the current path
        temp = []
        # start DFS traversal from the root sum is the required target sum
        self.collectpaths(root, sum, temp, result)
        # return all root to leaf paths whose sum equal target
        return result 

# Time Complexity : O(N)
# Space Complexity : O(N)