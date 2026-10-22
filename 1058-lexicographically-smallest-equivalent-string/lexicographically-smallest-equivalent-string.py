# Brute Force Code & Optimal Code
from collections import defaultdict
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # build an adjacency list to represent character equivalences if s1[i] and s2[i] are equivalent, add an edge between them since equivalence is bidirectional, add both directions characters connected through a path belong to the same equivalence group.
        adj = defaultdict(list)
        for u, v in zip(s1, s2):
            adj[u].append(v)
            adj[v].append(u)
        # DFS explores all characters equivalent to 'curr' and returns the lexicographically smallest character in the connected component containing 'curr'. 'visited' prevents revisiting characters and entering an infinite loop because the graph contains cycles.
        def DFS(curr, visited):
            # convert the current character to an index from 0 to 25 and mark it as visited.
            # ord('a') - ord('a') = 0
            # ord('b') - ord('a') = 1
            # ...
            # ord('z') - ord('a') = 25
            visited[ord(curr) - ord('a')] = 1
            # initially, assume the current character is the smallest character in its equivalence group.
            minChar = curr
            # explore every character directly equivalent to curr.
            for v in adj[curr]:
                # visit a neighboring character only if it has not already been explored.
                if visited[ord(v) - ord('a')] == 0:
                    # recursively explore the neighbor's connected component and get its smallest character compare that character with minChar and keep the lexicographically smaller one.
                    minChar = min(minChar, DFS(v, visited))
            # after exploring all reachable characters, return the smallest character found in this component.
            return minChar
        # stores the final answer, one character at a time.
        result = []
        # replace each character in baseStr with the smallest character from its equivalence group.
        for ch in baseStr:
            # create a fresh visited array for this DFS traversal each character in baseStr can belong to a different equivalence group, so we independently explore the component for each character.
            visited = [0] * 26
            # find the smallest character equivalent to ch and append it to the result.
            result.append(DFS(ch, visited))
        # join the list of characters into the final string.
        return ''.join(result)

# Time Complexity : O(N)
# Space Complexity : O(N)