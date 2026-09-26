# Brute Force Code & Optimal Code [BFS Method]
from collections import deque
class Solution:
    def __init__(self):
        # store total number of cities
        self.totalnumberofcities = 0
    def BFS(self, adj, vertices, visited):
        # queue for BFS traversal
        queue = deque()
        # start BFS traversal
        queue.append(vertices)
        # mark starting city as visited 
        visited[vertices] = True
        # continue until queue becomes empty
        while queue:
            # remove one city from queue
            current_vertex = queue.popleft()
            # visit all possible neighbours
            for neighbour in range(self.totalnumberofcities):
                # if connected and the neighbour is not visited
                if adj[current_vertex][neighbour] == 1 and not visited[neighbour]:
                    # mark the NEIGHBOUR as visited
                    visited[neighbour] = True
                    # add the NEIGHBOUR to the queue
                    queue.append(neighbour)
    def findCircleNum(self, isConnected):
        # number of cities
        self.totalnumberofcities = len(isConnected)
        # keep track of visited cities
        visited = [False] * self.totalnumberofcities
        # count total number of provinces
        count_totalnumberprovinces = 0
        # check every city
        for i in range(self.totalnumberofcities):
            # if city is not visited it belongs to a new province
            if not visited[i]:
                # visit all cities connected to this city
                self.BFS(isConnected, i, visited)
                # one complete connected province found
                count_totalnumberprovinces += 1
        # return total number of provinces
        return count_totalnumberprovinces

# Time Complexity : O(N)
# Space Complexity : O(N)