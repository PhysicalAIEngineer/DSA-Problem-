# Brute Force Code & Optimal Code
class Solution: 
    def __init__(self): 
        # store the maximum width of the binary tree
        self.maxWidth = 1 
    def DFS(self, root, d, level, arr, maxWidth): 
        # if the current node is empty there is nothing to process
        if root is None: 
            return 
        # if this is the first node visit at this level, store its position arr[level] = position of the first node at this level
        if level == len(arr): 
            arr.append(d) 
        # otherwise, calculate the width between the current node and the first node at this level
        else: 
            maxWidth[0] = max(maxWidth[0],  d - arr[level] + 1) 
        # go to the left child for a node at position d: left child position = 2*d + 1
        self.DFS(root.left,2 * d + 1,level + 1,arr,maxWidth) 
        # go to the right child for a node at position d: right child position = 2*d + 2
        self.DFS(root.right,2 * d + 2,level + 1,arr,maxWidth) 
    def widthOfBinaryTree(self, root): 
        # if the tree is empty its width is 0
        if root is None: 
            return 0 
        # use a list so that DFS can modify the maximum width inside the function
        maxWidth = [1] 
        # arr[level] stores the position of the first node at that level
        arr = [] 
        # start DFS from the root
        # root position = 0
        # root level = 0
        self.DFS(root, 0, 0, arr, maxWidth)  
        # return the maximum width found
        return maxWidth[0]

# Time Complexity : O(N)
# Space Complexity : O(N)
        