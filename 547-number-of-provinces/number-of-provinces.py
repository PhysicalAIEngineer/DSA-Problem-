# Brute Force Code & Optimal Code
class Solution:
    def DFS(self, adj, u, visited):
        # mark the current node as visited
        visited[u] = True
        # visit all possible neighbours
        for v in range(self.n):
            # if there is a connection between u and v not been visited 
            if adj[u][v] == 1 and not visited[v]:
                # continue DFS from neighbours v
                self.DFS(adj, v, visited)
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # number of cities
        self.n = len(isConnected)
        # keep track of visited citied
        visited = [False] * self.n
        # count total number of provinces
        count = 0
        # check every city
        for i in range(self.n):
            # if this city is not visited it belongs to new provinces
            if not visited[i]:
                # found one new provinces
                count += 1
                # visit all cities connected to this provices
                self.DFS(isConnected, i, visited)
        # return the total number of provinces 
        return count 

# Time Complexity : O(N)
# Space Complexity : O(N)        