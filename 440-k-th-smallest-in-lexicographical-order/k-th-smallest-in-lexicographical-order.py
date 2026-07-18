# Brute Force Code & Optimal Code
class Solution:
    # count how many numbers exist between two consecutive prefixes  current and next_prefix in lexicographical order
    def Count(self, current: int, next_prefix: int, n: int) -> int:
        # store the total number of valid integers under the current prefix
        count_numbers = 0
        # continue while the current prefix is within the range
        while current <= n:
            # count all numbers between the current prefix and the next prefix at this tree level
            count_numbers += next_prefix - current
            # move one level deeper in the lexicographical tree
            current *= 10
            next_prefix *= 10
            # ensure the next prefix does not exceed n
            next_prefix = min(next_prefix, n + 1)
        # return the number of integers under the current prefix
        return count_numbers
    # return the k-th smallest number in lexicographical order
    def findKthNumber(self, n: int, k: int) -> int:
        # start from the smallest lexicographical number
        current = 1
        # already standing at the first number so only k - 1 more moves are needed
        k -= 1
        # continue until the k-th number is reached
        while k > 0:
            # count how many numbers belong to the current prefix subtree
            count = self.Count(current, current + 1, n)
            # if the entire subtree can be skipped
            if count <= k:
                # move to the next sibling prefix
                current += 1
                # skip all numbers in this subtree
                k -= count
            else:
                # otherwise move to the first child of the current prefix
                current *= 10
                # one number the child itself is visited
                k -= 1
        # return the k-th lexicographical number
        return current

# Time Complexity : O(N)
# Space Complexity : O(N)