# Brute Force Code & Optimal Code
class Solution:  
    def find(self, x): 
        # path compression if x is not the root, recursively find the root
        if x == self.parent[x]: 
            return x 
 
        # Make x directly point to the root
        self.parent[x] = self.find(self.parent[x]) 
        return self.parent[x] 
 
    def Union(self, x, y): 
        # Find the roots of both nodes
        x_parent = self.find(x) 
        y_parent = self.find(y) 
 
        # Already in the same component
        if x_parent == y_parent: 
            return 
 
        # Union by rank:
        # Attach the smaller-rank tree under the larger-rank tree
        if self.rank[x_parent] > self.rank[y_parent]: 
            self.parent[y_parent] = x_parent 
 
        elif self.rank[x_parent] < self.rank[y_parent]: 
            self.parent[x_parent] = y_parent 
 
        else: 
            # Both have same rank
            self.parent[x_parent] = y_parent 
            self.rank[y_parent] += 1 
 
    def countPairs(self, n, edges): 
 
        # Parent and rank arrays for DSU
        self.parent = [0] * n 
        self.rank = [0] * n 
 
        # Initially every node is its own parent
        # So, every node is a separate component
        for i in range(n): 
            self.parent[i] = i 
 
        # Build connected components using DSU
        for vec in edges: 
            u = vec[0] 
            v = vec[1] 
 
            # Connect u and v
            self.Union(u, v) 
 
        # Count the size of every connected component
        mp = {} 
 
        for i in range(n): 
            # Find the root/representative of node i
            papa = self.find(i) 
 
            # Increase the size of that component
            mp[papa] = mp.get(papa, 0) + 1 
 
        result = 0 
        remainingNodes = n 
 
        # Count pairs belonging to different components
        for size in mp.values(): 
 
            # Current component has 'size' nodes
            # remainingNodes - size = nodes in other components
            # Every node in current component can pair
            # with every node in other components
            result += size * (remainingNodes - size) 
 
            # Remove current component from remaining nodes
            remainingNodes -= size 
 
        return result

# Time Complexity : O(N)
# Space Complexity : O(N) 