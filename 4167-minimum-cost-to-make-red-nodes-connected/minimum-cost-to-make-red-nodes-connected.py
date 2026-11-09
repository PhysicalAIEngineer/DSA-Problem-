class Solution:
    def minCost(self, n: int, colors: str, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        parent = [-1] * n
        parent[0] = 0
        order = [0]
        for u in order:
            for v in adj[u]:
                if v != parent[u]:
                    parent[v] = u
                    order.append(v)
        size = [1] * n
        dp = [0] * n
        base_cost = 0 
        max_saving = 0
        for u in reversed(order):
            w = size[u]
            if colors[u] == "R":
                base_cost += w
                dp[u] += w
            else:
                dp[u] -= w
            max_saving = max(max_saving, dp[u])
            if u != 0:
                p = parent[u]
                size[p] += w
                dp[p] += max(0, dp[u])
        return base_cost - max_saving 