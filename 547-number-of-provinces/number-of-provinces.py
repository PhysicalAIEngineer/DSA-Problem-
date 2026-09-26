# Brute Force Code & Optimal Code [DFS Method]
class Solution:
    def DFS(self, adj, vertices, visited):
        # mark the current node as visited
        visited[vertices] = True
        # visit all possible neighbours
        for neighbours in range(self.numberofcities):
            # if there is a connection and the neighbour has not been visited
            if adj[vertices][neighbours] == 1 and not visited[neighbours]: 
                # continue DFS from the neighbour's vertex
                self.DFS(adj, neighbours, visited) 
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        # number of cities
        self.numberofcities = len(isConnected)
        # keep track of visited cities
        visited = [False] * self.numberofcities
        # count total number of provinces
        counttotalnumberprovinces = 0
        # check every city 
        for i in range(self.numberofcities):
            # if this city is not visited it belongs to a new province
            if not visited[i]:
                # found one new province
                counttotalnumberprovinces += 1
                # visit all cities connected to this province
                self.DFS(isConnected, i, visited) 
        # return the total number of provinces
        return counttotalnumberprovinces 


# Time Complexity : O(N)
# Space Complexity : O(N)