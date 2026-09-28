# Brute Force Code & Optimal Code 
import heapq
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # build the directed weighted graph
        adj = {}
        # iterate though diffrent times 
        for u, v, w in times:
            # create an empty list for u if it does not exists
            if u not in adj:
                adj[u] = []
            # add directed edge u --> v with weight w
            adj[u].append((v, w))
        # min heap stores (distance, node)
        min_heap = []
        # initially distance of every node is infinity
        result = [float("inf")] * (n + 1)
        # distance of source node k from itself is 0
        result[k] = 0
        # push source node into the min heap
        heapq.heappush(min_heap, (0, k))
        # run dijkstra algorithm
        while min_heap:
            # get the node having the smallest distance
            smallest_distance, node = heapq.heappop(min_heap)
            # skip processing if a shorter path to this node was already found
            if smallest_distance > result[node]:
                continue
            # visit all neighbours of the current node
            for neighbours in adj.get(node, []):
                adjnode = neighbours[0]
                distance = neighbours[1]  
                # check if a shorter path is found
                if smallest_distance + distance < result[adjnode]:
                    result[adjnode] = smallest_distance + distance
                    # push 2 elements (new_distance, adjnode) instead of 3
                    heapq.heappush(min_heap, (result[adjnode], adjnode))
        # find the maximum shortest distance
        answer = 0  
        for i in range(1, n + 1):
            answer = max(answer, result[i])
        # if any node is unreachable return -1, otherwise return max distance
        return -1 if answer == float("inf") else answer

# Time Complexity : O(N)
# Space Complexity : O(N)