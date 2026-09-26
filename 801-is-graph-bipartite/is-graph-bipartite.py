# Brute Force Code & Optimal Code [DFS Method]
class Solution:  
    def checkBipartiteDFS(self, adj, curr, color, currColor): 
        # give the current node its color
        color[curr] = currColor  
        # visit all adjacent nodes
        for v in adj[curr]: 
            # if adjacent node has the same color then graph cannot be bipartite
            if color[v] == color[curr]: 
                return False 
            # if adjacent node is not colored yet
            if color[v] == -1: 
                # give the opposite color to the adjacent node 1 -> 0 &  0 -> 1
                colorOfV = 1 - currColor 
                # recursively check the remaining graph
                if self.checkBipartiteDFS(adj, v, color, colorOfV) == False: 
                    return False 
        # no conflict found in this DFS
        return True 
    def isBipartite(self, adj): 
        V = len(adj) 
        # -1 means the node is not colored yet
        color = [-1] * V 
        # so 1 = red & 0 = green check every node because the graph can contain multiple disconnected components
        for i in range(V):
            # if node is not visited/colored start a new DFS from this node
            if color[i] == -1:
                # start coloring this component with color 1
                if self.checkBipartiteDFS(adj, i, color, 1) == False: 
                    return False 
        # all nodes are colored without any conflict
        return True

# Time Complexity : O(N)
# Space Complexity : O(N)