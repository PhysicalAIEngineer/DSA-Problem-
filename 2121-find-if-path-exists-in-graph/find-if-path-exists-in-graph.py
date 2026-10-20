# Brute Force Code & Optimal Code [BFS Method]
from collections import deque
class Solution:
    def validPath(self, n, edges, source, destination):
        # create an adjacency list to represent the graph
        mp = {}
        # build the undirected graph
        for vec in edges:
            u = vec[0]
            v = vec[1]
            # add an edge from u to v
            mp.setdefault(u, []).append(v)
            # add an edge from v to u
            mp.setdefault(v, []).append(u)
        # track visited nodes to avoid revisiting them
        visited = [False] * n
        # create a queue for BFS and add the source node
        queue = deque()
        queue.append(source)
        # mark the source as visited
        visited[source] = True
        # perform BFS until the queue becomes empty
        while queue:
            # remove the front node from the queue
            node = queue.popleft()
            # if the destination is reached, a path exists
            if node == destination:
                return True
            # visit all unvisited neighboring nodes
            for it in mp.get(node, []):
                if not visited[it]:
                    # Mark the neighbor as visited
                    visited[it] = True
                    # add the neighbor to the queue
                    queue.append(it)
        # return False if the destination is unreachable
        return False

# Time Complexity : O(N)
# Space Complexity : O(N)