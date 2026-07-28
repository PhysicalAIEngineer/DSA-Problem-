# Brute Force Code & Optimal Code
class Solution:
    # perfrom BFS to find the minimum number of jumps
    def solve_BFS(self, arr: list[int], n: int) -> int:
        # track whether each index has alredy been visited
        visited = [False] * n
        # dictionary to store : value -> list of indices having that values
        value_to_indices = defaultdict(list)
        # bulid the dictonary
        for i in range(n):
            value_to_indices[arr[i]].append(i)
        # queue for BFS
        queue = deque()
        # start from index 0
        queue.append(0)
        visited[0] = True
        # number of jump takens
        steps = 0
        # perfrom BFS
        while queue:
            # number of indices at the current BFS level
            level_size = len(queue)
            # process all indices reachables in the current number of jumps
            for _ in range(level_size):
                # get the current index
                current = queue.popleft()
                # if the last index is reached return the minimum jumps
                if current == n - 1:
                    return steps
                # adjacent indices
                left = current - 1
                right = current + 1
                # jump to the left index
                if left >= 0 and not visited[left]:
                    queue.append(left)
                    visited[left] = True
                # jump to the right index
                if right < n and not visited[right]:
                    queue.append(right)
                    visited[right] = True
                # jump to every index having the same values
                for idx in value_to_indices[arr[current]]:
                    if not visited[idx]:
                        queue.append(idx)
                        visited[idx] = True
                # remove this values from the dictionary so its is processed only once avoiding repeated work
                del value_to_indices[arr[current]]
            # one BFS level one jump has been completed
            steps += 1
        # destination cannot be reached
        return -1
    # return the minimum number of jumps requied to reach the last index
    def minJumps(self, arr: list[int]):
        # total number of elements
        n = len(arr)
        # already at destination
        if n == 1:
            return 0 
        # solve using BFS
        return self.solve_BFS(arr, n)

 # Time Complexity : O(N^2)
 # Space Complexity : O(N)