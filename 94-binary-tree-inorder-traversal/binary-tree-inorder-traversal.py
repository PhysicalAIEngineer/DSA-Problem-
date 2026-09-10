# Brute Force Code & Optimal Code
class Solution: 
    def inorderTraversal(self, root): 
        # store the inorder traversal
        result = [] 
        # start from the root
        curr = root 
        # store the predecessor node
        pre = None 
        # continue until all nodes are processed
        while curr is not None: 
            # if there is no left child visit the current node directly
            if curr.left is None: 
                # add current node to the result
                result.append(curr.val) 
                # move to the right subtree
                curr = curr.right 
            else: 
                # find the rightmost node in the current node's left subtree
                pre = curr.left 
                while pre.right is not None: 
                    pre = pre.right 
                # connect the predecessor to the current node this creates a temporary link so that can come back to curr after processing its left subtree
                pre.right = curr 
                # store the current node temporarily
                temp = curr 
                # move to the left subtree
                curr = curr.left 
                # remove the original left link this prevents going back to the left subtree again and helps create the Morris traversal
                temp.left = None 
        # return the inorder traversal
        return result

# Time Complexity : O(N)
# Space Complexity : O(N)