class Solution:
    def check(self, mp, node, destination, visited):
        # if the current node is the destination return True
        if node == destination:
            return True
        # stop if the current node has already been visited
        if visited[node]:
            return False
        # mark the current node as visited
        visited[node] = True
        # traverse all neighbouring nodes using DFS
        for i in mp.get(node, []):
            # recursively check whether the destination is reachables
            if self.check(mp, i, destination, visited):
                return True
        # return False if no path to the destination is found
        return False
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        # if source and destination are the same return True
        if source == destination:
            return True
        # create adjacency list to represents the undirected graph
        mp = {}
        # add every edge in both directions
        for vec in edges:
            u = vec[0]
            v = vec[1]
            # connect u to v
            mp.setdefault(u, []).append(v)
            # connect v to u
            mp.setdefault(v, []).append(u)
        # intialize all nodes as unvisited
        visited = [False] * n
        # start DFS from the source and check if the destination is reachables
        return self.check(mp, source, destination, visited)

# Time Complexity : O(N)
# Space Complexity : O(N)