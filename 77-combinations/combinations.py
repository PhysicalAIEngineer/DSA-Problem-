# Brute Force Code & Optimal Code
class Solution:
    def __init__(self):
        # store all combinations
        self.result = []
    def solve(self, start, n, k, temp):
        # if have selected k numbers store the current combination.
        if k == 0:
            self.result.append(temp.copy())
            return
        # try every number from start to n.
        for i in range(start, n + 1):
            # choose i
            temp.append(i)
            # choose the remaining k - 1 numbers from the numbers after i.
            self.solve(i + 1, n, k - 1, temp)
            # backtrack remove i from the current combination.
            temp.pop()
    def combine(self, n: int, k: int) -> list[list[int]]:
        # current combination
        temp = []
        # start selecting numbers from 1.
        self.solve(1, n, k, temp)
        return self.result

# Time Complexity : O(N)
# Space Complexity : O(N)