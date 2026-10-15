# Brute Force Code & Optimal Code
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
        farthestnode = source
        # BFS traversal
        while queue:
            # number of nodes in current level
            size = len(queue)
            while size:
                # remove current node from queue
                current = queue.popleft()
                # last node processed in this level
                farthestnode = current
                # visit all neighbours
                for neighbour in adj.get(current, []):
                    if not visited.get(neighbour, False):
                        visited[neighbour] = True
                        queue.append(neighbour)
                size -= 1
            # increase distance if another level exists
            if queue:
                distance += 1
        # return farthest node and its distance
        return farthestnode, distance
    def finddiameter(self, adj):
        # first BFS: find one endpoint of the diameter
        farthestnode, dist = self.BFS(adj, 0) 
        # second BFS: find the diameter
        otherendnode, diameter = self.BFS(adj, farthestnode)
        return diameter
    def bulidadj(self, edges):
        # build adjacency list
        adj = {}
        for u, v in edges:
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
        adj1 = self.bulidadj(edges1)
        adj2 = self.bulidadj(edges2)
        # find diameter for both trees
        diameter_1 = self.finddiameter(adj1)
        diameter_2 = self.finddiameter(adj2)
        # minimum possible diameter after merging
        combined = ((diameter_1 + 1) // 2 + (diameter_2 + 1) // 2 + 1)
        # return maximum of all three possibilities
        return max(diameter_1, diameter_2, combined)

# Time Complexity : O(N)
# Space Complexity : O(N)