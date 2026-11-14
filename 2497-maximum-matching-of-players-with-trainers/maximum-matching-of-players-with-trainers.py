# Brute Force Code & Optimal Code
class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        # store the total number of players and trainers.
        # 1. m = number of players.
        # 2. n = number of trainers.
        m = len(players)
        n = len(trainers)
        # sort both arrays in ascending order sorting allows us to match the weakest player with the weakest trainer who is capable of training that player this strategy helps maximize the total number of successful matches.
        players.sort()
        trainers.sort()
        # initialize the count of successful player-trainer matches every successful assignment increases this count by one.
        count = 0
        # initialize pointer i for the players array.
        i = 0
        # initialize pointer j for the trainers array.
        j = 0
        # continue matching while:
        # 1. i < m means there are still unassigned players.
        # 2. j < n means there are still unused trainers
        # stop when either all players or all trainers have been processed.
        while i < m and j < n:
            # check whether the current trainer's ability is greater than or equal to the current player's ability.
            # 1. players[i] = ability required by the current player.
            # 2. trainers[j] = training capacity of the current trainer.
            # if this condition is true, the trainer can train the current player successfully.
            if players[i] <= trainers[j]:
                # successful player-trainer match has been found  increase the total number of successful matches.
                count += 1
                # move to the next player because the current player has already been assigned to a trainer each player can be matched with only one trainer.
                i += 1
            # move to the next trainer regardless of whether a successful match occurred if the current trainer was strong enough, they have been assigned to the current player if the trainer was not strong enough, they cannot train this player or any later player because players are sorted in ascending order therefore, this trainer can safely be skipped.
            j += 1
        # return the maximum number of successful matches.
        return count

# Time Complexity : O(Nlong)
# Space COmplexity : O(N)