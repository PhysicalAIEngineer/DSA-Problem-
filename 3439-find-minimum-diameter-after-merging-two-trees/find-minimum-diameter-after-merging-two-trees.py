from collections import deque 
class Solution: 
    def BFS(self, adj, source): 
        # queue for BFS
        queue = deque() 
        queue.append(source) 
        # track visited nodes
        visited = {} 
        visited[source] = True 
        # distance from source
        distance = 0 
        # farthest node found so far
        farthestNode = source 
        # BFS traversal
        while queue: 
            # number of nodes in current level
            size = len(queue) 
            while size: 
                # remove current node from queue
                current = queue.popleft() 
                # last node processed in this level becomes the farthest node
                farthestNode = current 
                # visit all neighbours
                for neighbours in adj.get(current, []): 
                    if visited.get(neighbours, False) == False: 
                        visited[neighbours] = True 
                        queue.append(neighbours) 
                size -= 1 
            # if next level exists increase distance by 1
            if queue: 
                distance += 1 
        # return farthest node and its distance
        return farthestNode, distance  
    def findDiameter(self, adj): 
        # start BFS from any node (0) find the farthest node from it
        farthestNode, dist = self.BFS(adj, 0) 
        # farthest node is one end of the diameter start BFS from farthestNode its farthest distance is the diameter
        otherEndNode, diameter = self.BFS(adj, farthestNode) 
        return diameter 
    def buildAdj(self, edges): 
        # build adjacency list
        adj = {} 
        for edge in edges: 
            u = edge[0] 
            v = edge[1]
            # create empty list for u
            if u not in adj: 
                adj[u] = []
            # create empty list for v
            if v not in adj: 
                adj[v] = []
            # tree is undirected so add edge in both directions
            adj[u].append(v) 
            adj[v].append(u) 
        return adj 
    def minimumDiameterAfterMerge(self, edges1, edges2): 
        # build adjacency lists for both trees
        adj1 = self.buildAdj(edges1) 
        adj2 = self.buildAdj(edges2) 
        # find diameter of first tree
        diameter_1 = self.findDiameter(adj1) 
        # find diameter of second tree
        diameter_2 = self.findDiameter(adj2) 
        # radius of first tree = ceil(diameter_1 / 2) and  radius of second tree = ceil(diameter_2 / 2) + 1 is the new edge used to connect both trees
        combined = (diameter_1 + 1) // 2 + (diameter_2 + 1) // 2 + 1 
        # final diameter can be: diameter of tree1 &  diameter of tree2 & path passing through the new connecting edge take the maximum of all three
        return max(diameter_1, diameter_2, combined)

# Time Complexity : O(N)
# Space Complexity : O(N)