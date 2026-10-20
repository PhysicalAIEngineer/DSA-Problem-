# Brute Force Code & Optimal Code
from collections import deque, defaultdict
class Solution:
    def isBipartite(self, adjacent, node, color) -> bool:
        # create queue for BFS traversal
        queue = deque([node])
        # assign color 1 to the starting nodes
        color[node] = 1  
        # add the starting node to the queue
        queue.append(node)
        # perfrom BFS to check whether the graph is bipartite
        while queue:
            # remove the front node from the queue
            u = queue.popleft()
            # visit all neighboring nodes
            for v in adjacent.get(u, []):
                # if adjacent nodes have the same color, the graph is not bipartite
                if color[v] == color[u]:
                    return False
                # if the neighbor is uncolored (-1), assign the opposite color (3 - color[u])
                if color[v] == -1:
                    color[v] = 3 - color[u]
                    # add the neighbours to the queue
                    queue.append(v)
        # return true if no coloring confict is found
        return True
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        # use defaultdict(list) instead of a list to support .append() and avoid errors
        adjacent = defaultdict(list)
        # build the undirected graph using dislike relationships
        for vec in dislikes:
            u = vec[0]
            v = vec[1]
            # add an edge from u to v
            adjacent[u].append(v)
            # add an edge from v to u
            adjacent[v].append(u)
        # initialize all people as uncolored (-1)
        color = [-1] * (n + 1)
        # check every connected component of the graph
        for i in range(1, n + 1):
            # start BFS if the current person is not yet colored
            if color[i] == -1:
                # return false if the components cannot be colored with zero colors
                if not self.isBipartite(adjacent, i, color):
                    return False
        # return True if the enitre graph is bipartite
        return True

# Time Complexity : O(N)
# Space Complexity : O(N)