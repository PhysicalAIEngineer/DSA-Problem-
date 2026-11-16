class Solution:
    def maxScore(self, parent: list[int], op: list[int], score: list[int]) -> int:
        n = len(parent)
        remaining = [0] * n
        for i in range(1, n):
            remaining[parent[i]] += 1
        queue = [i for i in range(n) if remaining[i] == 0]
        head = 0
        child_sum = [0] * n
        child_min = [float("inf")] * n
        while head < len(queue):
            node = queue[head]
            head += 1
            minimum = child_min[node]
            if minimum == float("inf"):
                value = score[node]
            else:
                total = child_sum[node]
                if op[node] == 1 or minimum < 0:
                    total -= minimum
                value = score[node] + total
            p = parent[node]
            if p == -1:
                return value
            child_sum[p] += value
            if value < child_min[p]:
                child_min[p] = value
            remaining[p] -= 1
            if remaining[p] == 0:
                queue.append(p)
        return 0 