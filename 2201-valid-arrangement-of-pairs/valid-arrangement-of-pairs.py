# Brute Force Code & Optimal Code
class Solution:
    def validArrangement(self, pairs):
        # Build adjacency list adj[u] contains all nodes v such that edge u -> v
        adj = {}
        # store indegree and outdegree of each node
        indegree = {}
        outdegree = {}
        # build directed graph
        for u, v in pairs:
            # add directed edge : u -> v
            if u not in adj:
                adj[u] = []
            adj[u].append(v)
            # increase outdegree of u
            outdegree[u] = outdegree.get(u, 0) + 1
            # increase indegre of v
            indegree[v] = indegree.get(v, 0) + 1
        # start from the first pairs starting node
        startnode = pairs[0][0]
        # find the start node of euler Path for euler path: outdegree - indegree = 1
        for node in outdegree:
            if outdegree.get(node, 0) - indegree.get(node, 0) == 1:
                startnode = node
                break
        # stack is used to simulate DFS eulerPath will store the final euler path
        eulerpath = []
        stack = [startnode]
        while stack:
            # look at the top node of the stack
            current = stack[-1]
            # if current node still has unused outgoing edges
            if adj.get(current, []):
                # take the last neighbour remove this edge so it is used only once
                neighbour = adj[current].pop()
                # move current from stack
                stack.append(neighbour)
            else:
                #  no outgoing edge is left from curr add curr to euler path
                eulerpath.append(stack.pop())
        # nodes are collected in reverse order so reverse them to get the correct euler path
        eulerpath.reverse()
        # build result pairs from consecutive nodes
        result = []
        for i in range(len(eulerpath) - 1):
            result.append([eulerpath[i], eulerpath[i + 1]])
        # return the valid arrangement of pairs
        return result

# Time Complexity : O(N)
# Space Complexity : O(N)
