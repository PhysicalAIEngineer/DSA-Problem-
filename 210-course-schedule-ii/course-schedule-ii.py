# Brute Force Code & Optimal Code [DFS Method]
from collections import defaultdict, deque  
class Solution: 
    # using Kahn's Algorithm (BFS)
    def topologicalSortCheck(self, adj, n, indegree): 
        # queue stores nodes whose indegree becomes 0
        que = deque() 
        # count how many courses we can process
        count = 0 
        # store the valid course order
        result = [] 
        # add all courses having indegree = 0 these courses have no prerequisites
        for i in range(n): 
            if indegree[i] == 0: 
                # add course to result
                result.append(i) 
                # one course is processed
                count += 1 
                # add course to queue
                que.append(i) 
        # BFS
        while que: 
            # take a course whose prerequisites are completed
            u = que.popleft() 
            # visit all courses dependent on u
            for v in adj[u]: 
                # one prerequisite of v is completed
                indegree[v] -= 1 
                # if all prerequisites of v are completed
                if indegree[v] == 0: 
                    # add v to the course order
                    result.append(v) 
                    # one more course is processed
                    count += 1 
                    # process v later
                    que.append(v) 
        # if all courses are not processed then a cycle is present
        if count != n: 
            return [] 
        # return valid course order
        return result 
    def findOrder(self, numCourses, prerequisites): 
        # adjacency list
        adj = defaultdict(list) 
        # indegree[i] = number of prerequisites of course i
        indegree = [0] * numCourses 
        # build the directed graph
        for vec in prerequisites: 
            # 'a' = course to be taken
            a = vec[0] 
            # 'b' = prerequisite course
            b = vec[1] 
            # create edge: b ---> a
            adj[b].append(a) 
            # one prerequisite is going into course a
            indegree[a] += 1 
        # find the topological order if cycle is present, return []
        return self.topologicalSortCheck(adj, numCourses, indegree)

# Time Complexity : O(N)
# Space Complexity : O(N)