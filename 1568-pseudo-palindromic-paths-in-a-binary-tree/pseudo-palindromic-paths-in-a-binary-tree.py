# Brute Force Code & Optimal Code
class Solution:
    def __init__(self):
        # store the total number of valid pseudo-palindromic paths
        self.result = 0
    def solve(self, root, temp):
        # continue only if the current node exists
        if root is not None:
            # count the frequency of the current node's value
            temp[root.val] += 1
            # check only at leaf nodes
            if root.left is None and root.right is None:
                # count how many values have odd frequency
                oddFreq = 0
                # check frequencies of values 1 to 9
                for i in range(1, 10):
                    if temp[i] % 2 != 0:
                        oddFreq += 1
                # path can form a palindrome if at most one value has an odd frequency
                if oddFreq <= 1:
                    self.result += 1
            # move to the left subtree
            self.solve(root.left, temp)
            # move to the right subtree
            self.solve(root.right, temp)
            # backtracking: remove the current node's value before going back
            temp[root.val] -= 1
    def pseudoPalindromicPaths(self, root):
        # frequency array for values 1 to 9
        temp = [0] * 10
        # reset the result
        self.result = 0
        # start DFS traversal from the root
        self.solve(root, temp)
        # return the total valid paths
        return self.result

# Time Complexity : O(N)
# Space Complexity : O(N)