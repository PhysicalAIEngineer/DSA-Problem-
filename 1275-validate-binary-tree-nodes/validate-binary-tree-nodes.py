# Brute Force Code & Optimal Code
from collections import deque 
class Solution: 
    def validateBinaryTreeNodes(self, n, leftChild, rightChild): 
        # store the children of every parent node
        parent_to_children = {} 
        # store the parent of every child node
        child_to_parent = {} 
        # process every node
        for i in range(n): 
            # current node
            node = i 
            # get its left and right children
            leftC = leftChild[i] 
            rightC = rightChild[i] 
            # process left child -1 means there is no left child
            if leftC != -1: 
                # create an empty list for this parent if it does not exist
                if node not in parent_to_children: 
                    parent_to_children[node] = [] 
                # store the left child
                parent_to_children[node].append(leftC) 
                # child cannot have two different parents if this child already has a parent the tree is invalid
                if leftC in child_to_parent: 
                    return False 
                # store the parent of the left child
                else: 
                    child_to_parent[leftC] = node 
            # process right child -1 means there is no right child
            if rightC != -1: 
                # create an empty list for this parent if it does not exist
                if node not in parent_to_children: 
                    parent_to_children[node] = [] 
                # store the right child
                parent_to_children[node].append(rightC) 
                # child cannot have two different parents
                if rightC in child_to_parent: 
                    return False 
                # store the parent of the right child
                else: 
                    child_to_parent[rightC] = node 
        # find the root initially, no root is found
        root = -1 
        # root is a node which has no parent
        for i in range(n): 
            # node is not present as a child so it does not have a parent
            if i not in child_to_parent: 
                # there must be exactly one root if another root is already found the structure has multiple roots
                if root != -1: 
                    return False 
                # store this node as the root
                else: 
                    root = i 
        # if no root exists there is a cycle or invalid structure
        if root == -1: 
            return False 
        # check connectivity using BFS keep track of visited nodes
        visited = [False] * n 
        # queue for BFS
        que = deque() 
        # start with the root
        count = 1 
        que.append(root) 
        visited[root] = True 
        # perform BFS
        while que: 
            # next node
            node = que.popleft() 
            # visit all children of this node
            for child in parent_to_children.get(node, []): 
                # if the child has not been visited
                if not visited[child]: 
                    # mark it as visited
                    visited[child] = True 
                    # increase the number of reachable nodes
                    count += 1 
                    # add the child to the queue
                    que.append(child) 
        # valid binary tree must contain all n nodes and be connected
        return count == n


# Time Complexity : O(N)
# Space Complexity : O(N)