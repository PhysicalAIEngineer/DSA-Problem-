# Brute Force Code & Optimal Code
class Solution:
    def findWinners(self, matches):
        # dictionary to store how many matches each player has lost.
        lost = {}
        # step 1: count the losses of every player.
        # process every match.
        for match in matches:
            # match[0] = winner
            # match[1] = loser
            lose = match[1]
            # increase the loss count of the losing player if the player is not already present get(lose, 0) returns 0.
            lost[lose] = lost.get(lose, 0) + 1
        # store players who have never lost a match.
        notLost = []
        # store players who have lost exactly one match.
        oneLos = []
        # step 2: find players with 0 or 1 loss.
        # process every match again.
        for match in matches:
            # player who lost this match.
            lose = match[1]
            # player who won this match.
            win = match[0]
            # if the losing player has lost exactly once add them to the one-loss list this player may appear as a loser only once so duplicates are not added.
            if lost[lose] == 1:
                oneLos.append(lose)
            # if the winning player is not present in lost they have never lost any match.
            if win not in lost:
                # add the player to the no-loss list.
                notLost.append(win)
                # mark this player as already processed the value 2 is only used as a marker it does not represent the actual loss count.
                lost[win] = 2
        # sort players in ascending order as required.
        notLost.sort()
        oneLos.sort()
        # return: [0- not loss players, 1-loss players]
        return [notLost, oneLos]

# Time Complexity : O(Nlog)
# Space Complexity : O(N)