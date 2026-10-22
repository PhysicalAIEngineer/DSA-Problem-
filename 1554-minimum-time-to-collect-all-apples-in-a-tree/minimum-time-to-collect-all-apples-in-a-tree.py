# Brute Force Code & Optimal Code
from collections import defaultdict
from typing import List
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # adjacency list to represent the undirected tree adj[u] contains all the neighbors of node u.
        adj = defaultdict(list)
        # build the adjacency list from the given edges since the tree is undirected, add both directions.
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        # DFS calculates the minimum time required to collect all apples in the subtree rooted at 'curr' and return to 'curr' after collecting them 'parent' is the node from which arrived at 'curr' it prevents DFS from moving backward in the tree.
        def DFS(curr, parent):
            # total time required to collect all apples in the subtree of the current node and return to curr.
            time = 0
            # explore every neighbor of the current node.
            for child in adj[curr]:
                # skip the parent node to avoid traversing backward.
                if child == parent:
                    continue
                # recursively calculate the time needed to collect apples in the child's subtree and return to child.
                time_from_child = DFS(child, curr)
                # we need to visit this child's subtree if: 1. time_from_child > 0: there is at least one apple somewhere deeper in the child's subtree, so we must visit it. 2. hasApple[child] is True: child itself has an apple, so we must visit it if neither condition is true, there are no apples in this child's subtree, so we can skip it.
                if time_from_child or hasApple[child]:
                    # add the time required to visit this subtree. +2 represents: 1 second to travel from curr to child &  1 second to return from child to curr. time_from_child represents the time needed to collect apples deeper in the subtree and return to child.
                    time += 2 + time_from_child
            # return the total time needed to collect all apples in curr's subtree and return to curr.
            return time
        # start DFS from node 0, the root of the tree the root has no parent, so use -1 do not need to return to node 0 after collecting apples but this DFS calculates a cost that includes returning to node 0 this is still optimal because the root is the starting point, and every necessary edge is traversed out and back.
        return DFS(0, -1)

# Time Complexity : O(N)
# Space Complexity : O(N)