# Brute Force Code & Optimal Code
class Solution: 
    def validArrangement(self, pairs): 
        # build adjacency list adj[u] contains all nodes v such that edge u -> v exists
        adj = {} 
        # store indegree and outdegree of every node
        indegree = {} 
        outdegree = {} 
        # build the graph
        for edge in pairs: 
            u = edge[0] 
            v = edge[1] 
            # add directed edge: u -> v
            if u not in adj: 
                adj[u] = [] 
            adj[u].append(v) 
            # increase outdegree of u
            outdegree[u] = outdegree.get(u, 0) + 1 
            # increase indegree of v
            indegree[v] = indegree.get(v, 0) + 1 
        # start from the first pair's starting node
        startNode = pairs[0][0] 
        # find the start node of euler Path for euler path: outdegree - indegree = 1
        for node in adj: 
            if outdegree.get(node, 0) - indegree.get(node, 0) == 1: 
                startNode = node 
                break 
        # stack is used to simulate DFS eulerPath will store the final euler path
        EulerPath = [] 
        stack = [] 
        # start DFS from the starting node
        stack.append(startNode) 
        while stack: 
            # look at the top node of the stack
            curr = stack[-1] 
            # if current node still has unused outgoing edges
            if adj.get(curr, []): 
                # take the last neighbour remove this edge so it is used only once
                neighour = adj[curr].pop() 
                # Move to the neighbour
                stack.append(neighour) 
            else: 
                # no outgoing edge is left from curr add curr to Euler path
                EulerPath.append(curr) 
                # remove curr from stack
                stack.pop() 
        # nodes are collected in reverse order so reverse them to get the correct Euler path
        EulerPath.reverse() 
        # build result pairs from consecutive nodes
        result = [] 
        for i in range(len(EulerPath) - 1): 
            result.append([EulerPath[i], EulerPath[i + 1]]) 
        # return the valid arrangement of pairs
        return result

# Time Complexity : O(N)
# Space Complexity : O(N)