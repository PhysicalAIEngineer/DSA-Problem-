# Brute Force Code & Optimal Code
class Solution:
    def minkey(self, inMST: list[bool], key: list[int], v: int) -> int:
        # initially, minimum index is 0
        min_index = -1
        # initially, minimum key value is infinity
        min_val = float("inf")
        # find the vertex with minimum key which is not already included in MST
        for i in range(v):
            # if vertex is not in MST and its key value is smaller
            if not inMST[i] and key[i] < min_val:
                min_val = key[i]
                min_index = i
        # return vertex having minimum key
        return min_index  
    def MinimumSpanningTree(self, graph: list[list[int]], v: int) -> int:
        # key[i] = minimum cost needed to connect vertex i to the MST
        key = [float("inf")] * v
        # track which vertices are already included in the MST
        inMST = [False] * v
        # start MST from vertex 0
        key[0] = 0
        # process all v vertices
        for _ in range(v):  
            # find the unvisited vertex with minimum key
            u = self.minkey(inMST, key, v) 
            inMST[u] = True
            # check all possible neighbouring vertices
            for neighbor in range(v):
                # Check: 1. there is an edge between u and v and 2. v is not already is MST and 3. edge u-v is cheaper than current key[v]
                if graph[u][neighbor] > 0 and not inMST[neighbor] and graph[u][neighbor] < key[neighbor]:
                    # update the minimum cost to connect v to the MST
                    key[neighbor] = graph[u][neighbor]
        # Return total weight of MST
        return sum(key)
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        # number of points
        n = len(points)
        # create the complete graph every points can be connected to every other points
        graph = [[0] * n for _ in range(n)]
        # Build complete adjacency matrix using Manhattan distance
        for i in range(n - 1):
            for j in range(i + 1, n):
                # calcualte manhatttan distance |x1 - x2| + |y1 - y2|
                manhattan_distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                graph[i][j] = manhattan_distance
                graph[j][i] = manhattan_distance
        # find the minimum spanning tree and return its total cost
        return self.MinimumSpanningTree(graph, n)

# Time Complexity : O(N)
# Space Complexity : O(N)