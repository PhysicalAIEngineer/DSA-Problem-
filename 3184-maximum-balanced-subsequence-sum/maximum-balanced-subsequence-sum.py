# Brute Force Code & Optimal Code
from typing import List
from bisect import bisect_left
class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        n = len(nums)
        keys = [nums[i] - i for i in range(n)]
        sorted_keys = sorted(set(keys))
        size = len(sorted_keys)
        bit = [0] * (size + 1)
        def query(i: int) -> int:
            best = 0
            while i > 0:
                best = max(best, bit[i])
                i -= i & -i
            return best
        def update(i: int, value: int) -> None:
            while i <= size:
                bit[i] = max(bit[i], value)
                i += i & -i
        answer = float("-inf")
        for i, num in enumerate(nums):
            rank = bisect_left(sorted_keys, keys[i]) + 1
            dp = num + query(rank)
            update(rank, dp)
            answer = max(answer, dp)
        return answer

# Time Complexity : O(N)
# Space Complexity : O(N)