# Brute Force Code & Optimal Code
from collections import defaultdict
from typing import List
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        # build an adjacency list to represent the undirected tree adj[u] contains all the neighbors of node u.
        adj = defaultdict(list)
        for u, v in edges:
            # since the tree is undirected, add both directions.
            adj[u].append(v)
            adj[v].append(u)
        # result[u] stores the number of nodes in the subtree rooted at u that have the same label as node u.
        result = [0] * n
        # frequency array for the 26 lowercase English letters.
        # count[0]  -> frequency of 'a'
        # count[1]  -> frequency of 'b'
        # count[25] -> frequency of 'z'
        # Initially, no nodes have been counted.
        count = [0] * 26
        # DFS explores the subtree rooted at node u parent is the node from which we arrived at u.
        def DFS(u, parent):
            # get the label of the current node.
            current_label = labels[u]
            # convert the character into an index from 0 to 25.
            # wxample:
            # 'a' -> ord('a') - ord('a') = 0
            # 'b' -> ord('b') - ord('a') = 1
            # 'c' -> ord('c') - ord('a') = 2
            index = ord(current_label) - ord('a')
            # record the frequency of the current node's label before counting this node and its descendants this gives us a baseline to calculate how many matching labels are present in this subtree.
            count_before = count[index]
            # count the current node itself its label must be included in its own subtree.
            count[index] += 1
            # explore every neighbor of the current node.
            for v in adj[u]:
                # skip the parent to avoid moving backward through the undirected tree.
                if v == parent:
                    continue
                # recursively explore the child's subtree the shared count array is passed implicitly through the enclosing DFS function each visited node increments its label's frequency.
                DFS(v, u)
            # all descendants of u have now been explored read the frequency of u's label again.
            count_after = count[index]
            # difference gives the number of nodes whose label matches labels[u] in u's subtree. it includes: 1. current node u. & 2. all descendants of u with the same label. counts from nodes visited before entering this subtree are removed by subtracting count_before.
            result[u] = count_after - count_before
        # we do not decrement count when returning the cumulative frequency array is maintained throughout the DFS traversal. difference between the two snapshots isolates this subtree's contribution for the current node start DFS at node 0, the root of the tree root has no parent, so use -1.
        DFS(0, -1)
        # return the answer for every node.
        return result

# Time Complexity : O(N)
# Space Complexity : O(N)