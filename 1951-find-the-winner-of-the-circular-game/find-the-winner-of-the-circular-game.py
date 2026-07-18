# Brute Force Code
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # create a list containing all players numbered from 1 to n.
        players = [i for i in range(1, n + 1)]
        # start counting from the first player index 0
        index = 0
        # continue eliminating players until only one player remains.
        while len(players) > 1:
            # move (k - 1) steps from the current position modulo is used to wrap around the circular list.
            index = (index + k - 1) % len(players)
            # remove the player at the calculated index the next round automatically starts from the player immediately after the removed player.
            players.pop(index)
        # only remaining player is the winner.
        return players[0]

# Time Complexity : O(N)
# Space Complexity : O(N)