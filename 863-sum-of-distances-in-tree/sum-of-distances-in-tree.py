# Brute Force Code & Optimal Code
from collections import defaultdict
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: list[list[int]]) -> list[int]:
        # adjaceny list to represents the undirected tree
        adj = defaultdict(list)
        # stores the total number of nodes in the tree
        self.N = n 
        # count[i] stores the size of the subtree rooted at node i subtree include node i itself and all its descendants
        self.count = [0] * n
        # stores the sum of distance from node zero to every other node this will be caculated during the first DFS traversal
        self.result_base_node = 0
        # bulid the adjacency list from the given edges
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        # first DFS : calculate subtree sizes and answer for node 0
        def DFSBase(curr_node, prev_node, curr_depth):
            # count the current node as part of its own subtree
            total_node = 1
            # add the current node distance from node 0 since start DFS from node 0 at depth 0 curr_depth represents the distance from node 0 to curr_node summing all depths gives the sum of distances from node 0  to every node in the tree
            self.result_base_node += curr_depth
            # visit all neighboring nodes
            for child in adj[curr_node]:
                # skip the parent to avoid traversing backward
                if child == prev_node:
                    continue
                # recusively calculate the size of the child subtree and add it to the current subtree size
                total_node += DFSBase(child, curr_node, curr_depth + 1)
            # after processing all children store the complete subtree size of the current node
            self.count[curr_node] = total_node
            # return this subtree size to the parent call
            return total_node
        # second DFS : reroot the tree and calculaute all answer
        def DFS(parent_node, prev_node, result):
            # visit all each child of the current node
            for child in adj[parent_node]:
                # skip the parent to avoid going backward
                if child == prev_node:
                    continue
                # rerooting formula : result[child] = result[parent_node] - count[child] + (n - count[child]) explanation : when moving the root from parent_node to child : 1. nodes inside child subtree becomes one edge closer to new root their total distance decreases by count[child] 2. all nodes outside child subtree becomes one edges farther from the new root their names is n - count[child] threfore : new answer = old answer - subtree size + nodes outside subtree
                result[child] = (result[parent_node] - self.count[child] + (self.N - self.count[child]))
                # recursively calculate answer for the descendansts using the newly calculated result of this child
                DFS(child, parent_node, result)
        # run the first DFS starting from node 0 this calculates : 1. subtree size of every node 2. sum of distance from node 0 to all nodes
        DFSBase(0, -1, 0)
        # result[i] will store the sum of distance from node i to every other node in the tree
        result = [0] * n
        # first DFS has already calculated the answer for node 0
        result[0] = self.result_base_node
        # run the second DFS to calcaulte the answer for all remaining nodes using the rerooting formula
        DFS(0, -1, result)
        # return the answer for every nodes
        return result 

# Time Complexity : O(N)
# Space Complexity : O(N)