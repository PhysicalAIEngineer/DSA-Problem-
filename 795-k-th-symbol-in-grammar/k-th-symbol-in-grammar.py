class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # start with the assumption that the first symbol is always 0
        current = 0
        # define the range of possible position in the nth row (1 to 2^(n-1))
        left = 1
        right = 2 ** (n - 1)
        # iterate though n - 1 times
        for _ in range(n - 1):
            # midpoints splits the row into two halves
            mid = (right + left) // 2
            # if k in left half, symbol remain same as parent
            if k <= mid:
                right = mid
            else:
                # if k is the right half symbol is flipped from parent
                left = mid + 1
                # flip between 0 and 1
                current = 0 if current else 1
        # return the final symbol from for row n, position k
        return current 

# Time Complexity : O(N)
# Space Complexity : O(1)
        