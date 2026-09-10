# Brute Force Code & Optimal Code
class Solution: 
    def convert(self, current, parent, adj): 
        # if the current node is None there is nothing to process
        if current is None: 
            return 
        # add parent as a neighbor this allows us to move up in the tree
        if parent != -1: 
            adj[current.val].append(parent) 
        # add left child as a neighbor
        if current.left is not None: 
            adj[current.val].append(current.left.val) 
        # add right child as a neighbor
        if current.right is not None: 
            adj[current.val].append(current.right.val) 
        # recursively process the left subtree
        self.convert(current.left, current.val, adj) 
        # recursively process the right subtree
        self.convert(current.right, current.val, adj) 
    def amountOfTime(self, root, start): 
        # create an adjacency list tree normally allows movement: parent -> child here also need child -> parent so convert the tree into an undirected graph
        adj = defaultdict(list) 
        # build the adjacency list
        self.convert(root, -1, adj) 
        # start BFS from the infected node
        que = deque([start]) 
        # keep track of visited nodes to avoid infecting the same node again
        visited = {start} 
        # store the number of minutes passed
        minutes = 0 
        # continue BFS while there are infected nodes that can infect their neighbours
        while que: 
            # number of nodes infected at the current minute
            n = len(que) 
            # process all nodes infected at this level
            while n > 0: 
                # remove one infected node
                curr = que.popleft() 
                # check all neighbours of the current node
                for ngbr in adj[curr]: 
                    # if this neighbour is not infected yet
                    if ngbr not in visited: 
                        # infect the neighbour
                        que.append(ngbr) 
                        # mark it as visited
                        visited.add(ngbr) 
                # process the next node of this level
                n -= 1 
            # one complete BFS level = one minute
            minutes += 1 
        # last BFS level increases minutes once extra so subtract 1
        return minutes - 1

# Time Complexity : O(N)
# Space Complexity : O(N)