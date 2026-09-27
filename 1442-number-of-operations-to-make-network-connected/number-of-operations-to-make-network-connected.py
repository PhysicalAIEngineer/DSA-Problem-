# Brute Force Code & Optimal Code
class Solution:
    def find(self, x):
        # if x is its own parent then x is the root of its componets
        if x == self.parent[x]:
            return x
        # path compression make x directly point to the root
        self.parent[x] = self.find(self.parent[x])
        # return the root
        return self.parent[x]
    def union(self, x, y):
        # find the roots of both nodes
        x_parent = self.find(x)
        y_parent = self.find(y)
        # if both nodes already belong to the same component nothing to merge
        if x_parent == y_parent:
            return
        # union by rank attacj the smaller tree under the larger tree
        if self.rank[x_parent] > self.rank[y_parent]:
            self.parent[y_parent] = x_parent
        elif self.rank[x_parent] < self.rank[y_parent]:
            self.parent[x_parent] = y_parent
        else:
            # both trees have the same rank attacj x tree under y tree
            self.parent[x_parent] = y_parent
            # increse the rank of the new root
            self.rank[y_parent] += 1
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        # to connect n computer at least n - 1 cables are required
        if len(connections) < n - 1:
            return -1
        # parent array of DSU
        self.parent = [0] * n
        # rank array for union by rank
        self.rank = [0] * n
        # intially every computer is its own parent so every computer is separate component
        for i in range(n):
            self.parent[i] = i
        # intially there are n separete componets
        components = n
        # process every available connection
        for vec in connections:
            # if both computer belongs to different components this connection can merge the two components
            if self.find(vec[0]) != self.find(vec[1]):
                # two componets become new so decreses componets count by 1
                components -= 1 
                # merge the two compents
                self.union(vec[0], vec[1])
        # if there  are components separate componets need componets - 1 connections to connect them all
        return components - 1
