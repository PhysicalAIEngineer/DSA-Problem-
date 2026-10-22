# Brute Force Code & Optimal Code
from collections import defaultdict
from typing import List
class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        # total number of nodes in the tree.
        n = len(vals)
        # DSU (Disjoint Set Union) initialization parent[i] stores the parent of node i in the DSU initially, every node is its own parent, meaning every node belongs to a separate component.
        self.parent = list(range(n))
        # rank[i] estimates the height of the DSU tree rooted at i initially, every component contains one node union by rank attaches the shorter tree under the taller tree to keep operations efficient.
        self.rank = [1] * n
        # find the representative (root) of the component containing node x.
        def find(x):
            # if x is its own parent, it is the root of its component.
            if x == self.parent[x]:
                return x
            # path compression recursively find the root and directly connect x to that root, making future find operations faster.
            self.parent[x] = find(self.parent[x])
            return self.parent[x]
        # merge the components containing nodes x and y.
        def Union(x, y):
            # find the roots of both components.
            x_parent = find(x)
            y_parent = find(y)
            # if both nodes already have the same root they are already in the same component.
            if x_parent == y_parent:
                return
            # union by rank attach the root of the shorter tree under the root of the taller tree.
            if self.rank[x_parent] > self.rank[y_parent]:
                self.parent[y_parent] = x_parent
            elif self.rank[x_parent] < self.rank[y_parent]:
                self.parent[x_parent] = y_parent
            else:
                # if both trees have equal rank, choose one root and attach the other root beneath it.
                self.parent[x_parent] = y_parent
                # resulting tree's rank increases by one because the two trees had equal rank.
                self.rank[y_parent] += 1
        # build the adjacency list for the undirected tree.
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        # group nodes by their values processing nodes in increasing value order allows us to activate nodes gradually while maintaining the rule that every active node has value <= the current value.
        val_to_nodes = defaultdict(list)
        for i in range(n):
            val_to_nodes[vals[i]].append(i)
        # every individual node forms a good path of length one therefore initialize the answer to n.
        result = n
        # is_active[u] indicates whether node u has been activated a node becomes active when its value is reached in the sorted processing order only active neighbors are merged into the current node connected component.
        is_active = [False] * n
        # process distinct node values in increasing order.
        for value in sorted(val_to_nodes):
            # all nodes whose value equals the current value.
            nodes = val_to_nodes[value]
            # activate and connect each node with its active neighbors.
            for u in nodes:
                # merge u with every neighbor that has already been activated such neighbors have values <= the current value therefore every node in the resulting component satisfies the maximum-value constraint for paths whose endpoints have the current value.
                for v in adj[u]:
                    if is_active[v]:
                        Union(u, v)
                # mark u as active after processing its neighbors.
                is_active[u] = True
            # find the DSU representative of every node whose value equals the current value nodes with the same representative belong to the same active connected component.
            parents = [find(u) for u in nodes]
            # sort the representatives so nodes in the same component appear consecutively.
            parents.sort()
            # count how many current-value nodes belong to each connected component.
            current_values = len(parents)
            j = 0
            while j < current_values:
                # representative of the current component.
                cur_parent = parents[j]
                # number of nodes with the current value in this connected component.
                count = 0
                # count consecutive occurrences of this root.
                while j < current_values and parents[j] == cur_parent:
                    j += 1
                    count += 1
                # if a component contains 'count' nodes with the current value, any two distinct such nodes form a good path number of unordered pairs: count * (count - 1) // 2 add these paths to the answer.
                result += (count * (count - 1)) // 2
        # return the total number of good paths, including all single-node paths.
        return result

# Time Complexity : O(N)
# Space Complexity : O(N)