# Brute Force Code & Optimal Code
class Solution: 
    def __init__(self): 
        # dictionary to store the parent of each node
        self.parent = {}  
    def addParent(self, root): 
        # if the current node is None there is nothing to process
        if root is None: 
            return 
        # if the current node has a left child store the current node as its parent
        if root.left: 
            self.parent[root.left] = root 
        # recursively store parents for the left subtree
        self.addParent(root.left) 
        # if the current node has a right child store the current node as its parent
        if root.right: 
            self.parent[root.right] = root 
        # recursively store parents for the right subtree
        self.addParent(root.right) 
    def collectKDistanceNodes(self, target, k, result): 
        # queue is used for BFS start BFS from the target node
        que = deque() 
        que.append(target) 
        # keep track of already visited nodes to avoid visiting the same node again
        visited = set() 
        visited.add(target.val) 
        # perform BFS until the queue becomes empty
        while que: 
            # number of nodes at the current distance
            n = len(que) 
            # if k becomes 0 all nodes currently in the queue are exactly k distance away
            if k == 0: 
                break 
            # process all nodes at the current distance
            while n > 0: 
                # remove the first node from the queue
                curr = que.popleft() 
                # move to the left child if it exists and is not visited
                if curr.left and curr.left.val not in visited: 
                    que.append(curr.left) 
                    visited.add(curr.left.val) 
                # move to the right child if it exists and is not visited
                if curr.right and curr.right.val not in visited: 
                    que.append(curr.right) 
                    visited.add(curr.right.val) 
                # move to the parent node if the current node has a parent
                if curr in self.parent: 
                    parentNode = self.parent[curr] 
                    # add the parent if it is not visited
                    if parentNode.val not in visited: 
                        que.append(parentNode) 
                        visited.add(parentNode.val) 
                # process the next node at this distance
                n -= 1 
            # move one level farther from the target
            k -= 1 
        # all nodes remaining in the queue are exactly k distance away from target
        while que: 
            temp = que.popleft() 
            result.append(temp.val) 
    def distanceK(self, root, target, k):
        # store the final answer
        result = [] 
        # clear the parent dictionary in case the same Solution object is reused
        self.parent.clear() 
        # store the parent of every node
        self.addParent(root) 
        # use BFS to find all nodes exactly k distance away from target
        self.collectKDistanceNodes(target, k, result) 
        # return the answer
        return result

# Time Complexity : O(N)
# Space Complexity : O(N)