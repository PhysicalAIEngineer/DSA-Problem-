# Brute Force Code & Optimal Code [BFS Method]
from collections import defaultdict, deque 
class Solution: 
    def topologicalSortCheck(self, adj, n, indegree): 
        # queue for nodes whose indegree becomes 0
        que = deque() 
        # count how many nodes we can process
        count = 0 
        # add all nodes having indegree = 0 these nodes have no pending prerequisites
        for i in range(n): 
            if indegree[i] == 0: 
                count += 1 
                que.append(i) 
        # BFS using Kahn's Algorithm
        while que: 
            # take a course with no remaining prerequisite
            u = que.popleft() 
            # visit all courses that depend on course u
            for v in adj[u]: 
                # one prerequisite of v is now completed
                indegree[v] -= 1 
                # if all prerequisites of v are completed
                if indegree[v] == 0:
                    # v can now be completed
                    count += 1 
                    que.append(v) 
        # if were able to process all courses then there is no cycle
        if count == n: 
            return True 
        # some courses could not be processed which means a cycle is present
        return False 
    def canFinish(self, numCourses, prerequisites): 
        # adjacency list adj[b] contains courses that can be taken after b
        adj = defaultdict(list) 
        # indegree[i] = number of prerequisites for course i
        indegree = [0] * numCourses 
        # process every prerequisite pair
        for vec in prerequisites:
            # 'a' is the course we want to take
            a = vec[0] 
            # 'b' is the prerequisite course
            b = vec[1] 
            # create edge: b ---> a must complete b before taking a
            adj[b].append(a) 
            # one prerequisite is going into course a
            indegree[a] += 1 
        # check whether all courses can be processed if a cycle is present, not possible
        return self.topologicalSortCheck(adj, numCourses, indegree)

# Time Complexity : O(N)
# Space Complexity : O(N)