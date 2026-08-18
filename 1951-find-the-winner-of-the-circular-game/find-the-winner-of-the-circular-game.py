# Optimal Code
class Solution:
    # recursive function to find the winner's index (0-based)
    def findWinnerIdx(self, n: int, k: int) -> int:
        # base case: if only one player is left its index is 0.
        if n == 1:
            return 0
        # recursively find the winner's index when there are n - 1 players.
        index = self.findWinnerIdx(n - 1, k)
        # convert the winner's index from the smaller circle (n - 1 players) to the current circle of n players using the Josephus formula.
        index = (index + k) % n
        # return the winner's index for n players.
        return index
    # return the winner's number (1-based)
    def findTheWinner(self, n: int, k: int) -> int:
        # find the winner's index (0-based).
        result_index = self.findWinnerIdx(n, k)
        # convert the 0-based index into the required 1-based player number
        return result_index + 1

# Time Complexity : O(N)
# Space Complexity : O(1)