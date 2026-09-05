# Brute Force Code & Optimal Code
class Solution: 
    def DFS(self, root, mp, res): 
        # if the node is empty return "NULL" to represent an empty subtree need this so that different tree structures do not produce the same string.
        if root is None: 
            return "NULL" 
        # create a unique string representation of the current subtree. format: root value + left subtree + right subtree
        s = (str(root.val) + ","  + self.DFS(root.left, mp, res) + "," + self.DFS(root.right, mp, res)) 
        # check how many times this subtree has already appeared if frequency is exactly 1 this is the second occurrence of the same subtree.
        if mp.get(s, 0) == 1: 
            # store the root of this duplicate subtree in the result.
            res.append(root) 
        # increase the frequency of this subtree.
        mp[s] = mp.get(s, 0) + 1 
        # return the string representation so the parent node can use it to build its own subtree representation.
        return s 
    def findDuplicateSubtrees(self, root): 
        # dictionary to store: subtree representation -> frequency
        mp = {} 
        # stores the roots of duplicate subtrees.
        res = [] 
        # start DFS from the root to generate representations of all subtrees.
        self.DFS(root, mp, res) 
        # return all duplicate subtree roots.
        return res

# Time Complexity : O(N)
# Space Complexity : O(N)