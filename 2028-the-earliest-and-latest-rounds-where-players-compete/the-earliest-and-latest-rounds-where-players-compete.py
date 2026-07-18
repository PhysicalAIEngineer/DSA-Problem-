# Brute Force Code & Optimal Code
class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> list[int]:
        # current positions of the two target players
        left = firstPlayer
        right = secondPlayer
        # base case: if the two players are paired in the current round they meet immediately
        if left == n - right + 1:
            return [1, 1]
        # ensure the first player is always on the left side of the tournament bracket
        if left > n - right + 1:
            temp = n - left + 1
            left = n - right + 1
            right = temp
        # store the earliest and latest possible meeting rounds
        min_round = n
        max_round = 1
        # number of players that advance to the next round
        next_round_players = (n + 1) // 2
        # case 1: both players are in the left half
        if right <= next_round_players:
            # number of players before the first player
            count_left = left - 1
            # number of players between the two players
            mid_count = right - left - 1
            # try every possible way survivors can be arranged
            for survivors_left in range(count_left + 1):
                for survivors_mid in range(mid_count + 1):
                    # new position of the first player
                    pos1 = survivors_left + 1
                    # new position of the second player
                    pos2 = pos1 + survivors_mid + 1
                    # recursively compute the earliest and latest meeting rounds
                    result = self.earliestAndLatest(next_round_players,pos1,pos2)
                    # add one for the current round
                    min_round = min(min_round, result[0] + 1)
                    max_round = max(max_round, result[1] + 1)
        # case 2: players are on opposite sides
        else:
            # mirrored position of the second player
            fights_right = n - right + 1
            # players before the first player
            count_left = left - 1
            # players between the first player and the mirrored second player
            mid_count = fights_right - left - 1
            # remaining players between the mirrored position and the actual second player
            remain_mid_count = right - fights_right - 1
            # try every possible survivor arrangement
            for survivors_left in range(count_left + 1):
                for survivors_mid in range(mid_count + 1):
                    # new position of the first player
                    pos1 = survivors_left + 1
                    # new position of the second player
                    pos2 = (pos1 + survivors_mid + (remain_mid_count + 1) // 2 + 1)
                    # solve the smaller tournament recursively
                    result = self.earliestAndLatest(next_round_players, pos1, pos2)
                    # include the current round
                    min_round = min(min_round, result[0] + 1)
                    max_round = max(max_round, result[1] + 1)
        # return the earliest and latest possible meeting rounds
        return [min_round, max_round]

# Time Complexity : O(N)
# Space Complexity : O(Nlog)