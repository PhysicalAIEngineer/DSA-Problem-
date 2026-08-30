# Brute Force Code & Optimal Code
class Solution:
    def __init__(self):
        # store the restored original array.
        self.result = []
    def solve(self, u, prev, adj):
        # add the current node to the answer DFS visits nodes in the same order as they appear in the original array.
        self.result.append(u)
        # visit every node connected to the current node.
        for v in adj[u]:
            # do not move back to the node from which we came.
            if v != prev:
                # continue DFS from the next node.
                self.solve(v, u, adj)
    def restoreArray(self, adjacentPairs):
        # create an adjacency list adj[u] contains all numbers that are directly adjacent to u in the original array.
        adj = {}
        # build the undirected graph using all adjacent pairs.
        for pair in adjacentPairs:
            # extract the two adjacent numbers.
            u = pair[0]
            v = pair[1]
            # add v to u's list of neighbors.
            if u not in adj:
                adj[u] = []
            adj[u].append(v)
            # add u to v's list of neighbors.
            if v not in adj:
                adj[v] = []
            adj[v].append(u)
        # find an endpoint of the original array.
        # in the graph:
        # - two endpoints have degree 1.
        # - every middle element has degree 2.
        startPoint = -1
        # check every node in the graph.
        for node in adj:
            # node with only one neighbor must be an endpoint.
            if len(adj[node]) == 1:
                # use this endpoint as the starting point for DFS.
                startPoint = node
                break
        # start DFS from the endpoint.
        # - prev = None because the starting node does not have a previous node.
        self.solve(startPoint, None, adj)
        # return the restored original array.
        return self.result

# Time Complexity : O(N)
# Space Complexity : O(N)