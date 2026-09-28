# Brute Force Code & Optimal Code
class Solution:  
    def find(self, x): 
        # path compression if x is not the root, recursively find the root
        if x == self.parent[x]: 
            return x 
        # make x directly point to the root
        self.parent[x] = self.find(self.parent[x]) 
        return self.parent[x] 
    def union(self, x, y): 
        # find the roots of both nodes
        x_parent = self.find(x) 
        y_parent = self.find(y) 
        # already in the same component
        if x_parent == y_parent: 
            return 
        # union by rank attach the smaller-rank tree under the larger-rank tree
        if self.rank[x_parent] > self.rank[y_parent]: 
            self.parent[y_parent] = x_parent 
        elif self.rank[x_parent] < self.rank[y_parent]: 
            self.parent[x_parent] = y_parent 
        else: 
            # both have same rank
            self.parent[x_parent] = y_parent 
            self.rank[y_parent] += 1 
    def countPairs(self, n, edges): 
        # parent and rank arrays for DSU
        self.parent = [0] * n 
        self.rank = [0] * n 
        # initially every node is its own parent so every node is a separate component
        for i in range(n): 
            self.parent[i] = i 
        # build connected components using DSU
        for vec in edges: 
            u = vec[0] 
            v = vec[1] 
            # connect u and v
            self.union(u, v) 
        # count the size of every connected component
        count_size = {} 
        # iterate though every valeus 
        for i in range(n): 
            # find the root of node i
            root = self.find(i) 
            # increase the size of that component
            count_size[root] = count_size.get(root, 0) + 1 
        # assign values of result
        result = 0 
        # assign values of remainingNodes
        remainingNodes = n 
        # count pairs belonging to different components
        for size in count_size.values(): 
            # current component has 'size' nodes remainingNodes - size = nodes in other components every node in current component can pair with every node in other components
            result += size * (remainingNodes - size) 
            # Remove current component from remaining nodes
            remainingNodes -= size 
        # return the result values 
        return result

# Time Complexity : O(N)
# Space Complexity : O(N) 