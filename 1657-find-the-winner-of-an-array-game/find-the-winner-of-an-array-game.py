# Optimal Code
class Solution:
    def getWinner(self, arr: list[int], k: int) -> int:
        # number of elements in the array
        n = len(arr)
        # find the maximum element maximum element can never lose a comparison.
        max_el = max(arr)
        # if k is greater than or equal to n the maximum element will eventually get enough consecutive wins.
        if k >= n:
            return max_el
        # initially, the first element is the winner
        winner = arr[0]
        # number of consecutive wins by the current winner
        wins = 0
        # compare the current winner with every remaining element
        for i in range(1, n):
            # current winner is larger than arr[i] so the winner gets another consecutive win
            if winner > arr[i]:
                wins += 1
            else:
                # arr[i] is larger so it becomes the new winner
                winner = arr[i]
                # new winner has won one round
                wins = 1
            # if the current winner has won k consecutive rounds, return the winner the maximum element can never lose so once we reach it it is guaranteed to be the final winner.
            if wins == k or winner == max_el:
                return winner
        # return the winner if the loop finishes
        return winner

# Time Complexity : O(N)
# Space Complexity : O(N)