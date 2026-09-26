# Brute Force Code & Optimal Code [BFS Method]
from collections import deque  
class Solution: 
    def checkBipartiteBFS(self, adj, curr, color, currColor): 
        # give the starting node its color
        color[curr] = currColor  
        # queue for BFS traversal
        que = deque() 
        que.append(curr) 
        # continue BFS while queue is not empty
        while que: 
            # remove the front node from the queue
            u = que.popleft() 
            # visit all adjacent nodes of u
            for v in adj[u]: 
                # if adjacent node already has the same color then graph is not bipartite
                if color[v] == color[u]: 
                    return False 
                # if adjacent node is not colored yet
                elif color[v] == -1: 
                    # give opposite color to the adjacent node 1 -> 0 & 0 -> 1
                    color[v] = 1 - color[u] 
                    # add the node to queue for further BFS
                    que.append(v) 
        # no color conflict found in this component
        return True 
    def isBipartite(self, adj): 
        V = len(adj) 
        # -1 means node is not colored yet
        color = [-1] * V 
        # so, 1 = red &  0 = green check every connected component because graph can be disconnected
        for i in range(V): 
            # if node is not colored start BFS from this node
            if color[i] == -1: 
                # start this component with color 1
                if self.checkBipartiteBFS(adj, i, color, 1) == False: 
                    return False 
        # all components are successfully 2-colored
        return True

# Time Complexity : O(N)
# Space Complexity : O(N)