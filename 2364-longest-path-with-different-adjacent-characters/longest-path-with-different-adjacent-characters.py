# Brute Force Code & Optimal Code
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        # total number of nodes in the tree.
        n = len(parent)
        # stores the maximum valid path length found anywhere in the tree a valid path is one where every pair of adjacent nodes has different characters.
        self.result = 0
        # build an adjacency list to represent the undirected tree.
        adj = defaultdict(list)
        # parent[i] gives the parent of node i node 0 is the root, so start from node 1.
        for i in range(1, n):
            u = i
            v = parent[i]
            # add the parent-child relationship in both directions.
            adj[u].append(v)
            adj[v].append(u)
        # DFS returns the length of the longest valid downward path starting at curr and extending into at most one subtree parent_node is the node from which we arrived at curr it prevents us from traversing backward in the tree.
        def DFS(curr, parent_node):
            # length of the longest valid downward path found among the children processed so far.
            longest = 0
            # length of the second-longest valid downward path need two paths because the longest path passing through curr may extend into two different subtrees.
            second_longest = 0
            # explore every neighbor of the current node.
            for child in adj[curr]:
                # skip the parent to avoid revisiting it.
                if child == parent_node:
                    continue
                # recursively calculate the longest valid downward path starting at this child.
                child_longest_length = DFS(child, curr)
                # edge between curr and child can be included only when their characters are different. if both characters are equal, this child's path cannot be connected to curr, so ignore its length for the current node note that DFS(child, curr) has already updated self.result, so valid paths entirely inside the child's subtree are still considered.
                if s[child] == s[curr]:
                    continue
                # if this child's path is longer than the current second-longest path, update second_longest.
                if child_longest_length > second_longest:
                    second_longest = child_longest_length
                # keep the two largest valid downward path lengths in descending order: longest >= second_longest if second_longest is larger than longest swap them.
                if second_longest > longest:
                    longest, second_longest = second_longest, longest
            # CASE 1: longest valid downward path including curr longest is the longest valid path from one child. second_longest is the second-best child path. downward path can use only ONE child branch because a downward path cannot split into two branches add 1 to count curr itself.
            longest_valid_downward = max(longest, second_longest) + 1
            # CASE 2: path containing only the current node this is always a valid path of length 1, even if no child can be connected because of equal characters.
            path_containing_current_node = 1
            # CASE 3: longest valid path passing through curr and extending into two different child subtrees one branch contributes 'longest' nodes beyond curr the other branch contributes 'second_longest' nodes add 1 for curr itself. the two branches can be joined because each selected child has a character different from s[curr].
            longest_valid_path_passing = (longest + second_longest + 1)
            # update the global answer with the best path found:
            # 1. path passing through two child branches.
            # 2. path extending into one child branch.
            # 3. path containing only curr.
            # this also preserves answers found deeper in the tree.
            self.result = max(self.result,longest_valid_path_passing,longest_valid_downward, path_containing_current_node)
            # return the longest valid downward path from curr to its descendants the parent can extend this path through curr, so  return only ONE branch, not two.
            return max(longest_valid_downward, path_containing_current_node)
        # start DFS from node 0, the root since it has no parent, use -1.
        DFS(0, -1)
        # return the longest valid path found anywhere in the tree.
        return self.result

# Time Complexity : O(N)
# Space Complexity : O(N)