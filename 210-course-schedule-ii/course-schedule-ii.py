# Brute Force Code & Optimal Code [DFS Method]
from collections import defaultdict  
class Solution: 
    def __init__(self): 
        # flag to indicate whether a cycle exists
        self.hasCycle = False 
    def DFS(self, adj, u, visited, st, inRecursion): 
        # mark current node as visited
        visited[u] = True 
        # mark current node as part of current DFS path
        inRecursion[u] = True 
        # first process all neighbours of u then add u to stack
        for v in adj[u]: 
            # if v is already in the current DFS path then a cycle is present
            if inRecursion[v]: 
                self.hasCycle = True 
                return 
            # if v is not visited, perform DFS
            if not visited[v]: 
                self.DFS(adj, v, visited, st, inRecursion) 
        # add current node after all its neighbours are processed
        st.append(u) 
        # DFS of u is completed so remove u from current recursion path
        inRecursion[u] = False 
    def findOrder(self, numCourses, prerequisites):
        # create adjacency list
        adj = defaultdict(list) 
        # track whether each course has been visited
        visited = [False] * numCourses 
        # track nodes currently present in DFS recursion path
        inRecursion = [False] * numCourses 
        # reset cycle flag
        self.hasCycle = False 
        # stack to store DFS finishing order
        st = [] 
        # build the directed graph
        for vec in prerequisites:
            # 'a' = course to be taken
            a = vec[0] 
            # 'b' = prerequisite course
            b = vec[1] 
            # create edge: b ---> a
            adj[b].append(a) 
        # perform DFS for every courses because graph may have multiple components
        for i in range(numCourses): 
            if not visited[i]: 
                self.DFS(adj, i, visited, st, inRecursion) 
        # Final topological ordering
        result = [] 
        # If cycle is present valid course order is not possible
        if self.hasCycle: 
            return [] 
        # Reverse DFS finishing order
        while st: 
            result.append(st.pop()) 
        # Return valid course order
        return result

# Time Complexity : O(N)
# Space Complexity : O(N)