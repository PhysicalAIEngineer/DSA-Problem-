# Brute Force Code & Optimal Code [DFS Method]
from collections import defaultdict
class Solution:
    def isCycleDFS(self, adj, vertices, visited, inRecursion):
        # mark current node as visited
        visited[vertices] = True
        # mark current node as the part of the current DFS path
        inRecursion[vertices] = True
        # visit all neighbours 
        for neighbour in adj[vertices]:
            # if neighbour is not visited continue DFS from neighbour
            if not visited[neighbour]:
                if self.isCycleDFS(adj, neighbour, visited, inRecursion):
                    return True
            # if neighbour is already in the current DFS path then found cycle
            elif inRecursion[neighbour]:
                return True
        # DFS of neighbours is already in the current DFS path then found cycle
        inRecursion[vertices] = False
        # no cycle found from neighbour
        return False 
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # adjacency list
        adj = defaultdict(list)
        # visited[i] = True if course i was visited before
        visited = [False] * numCourses
        # inRecursion[i] = True if course i is currently present in the DFS path
        inRecursion = [False] * numCourses
        # bulid the directed graph
        for vec in prerequisites:
            # "a" = course to be taken
            a = vec[0]
            # "b" = prerequisite course
            b = vec[1]
            # create edge : b ---> a
            adj[b].append(a)
        # check every course 
        for i in range(numCourses):
            # start DFS only if course is not visited
            if not visited[i]:
                # if DFS detect a cycle courses cannot be completed
                if self.isCycleDFS(adj, i, visited, inRecursion):
                    return False
        # no cycle found so all courses can be completed
        return True

# Time Complexity : O(N)
# Space Complexity : O(N)