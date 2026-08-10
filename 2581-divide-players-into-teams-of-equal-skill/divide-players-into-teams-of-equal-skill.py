# Brute Force Code & Optimal Code
class Solution:
    def dividePlayers(self, skill: List[int]):
        # sum of all players skills 
        total = sum(skill)
        # check if total sum can be evenly divided into n/2 teams each team has size 2, so target sum per team = (2 * total) / n
        if (2 * total) % len(skill):
            # cannot divide into equal total skill teams
            return -1
        # count of each skill values
        count = Counter(skill)
        # required total skill per team
        target = (2 * total) // len(skill)
        # sum of chemistry of all teams
        result = 0
        # iterate over each players skill
        for s in skill:
            # if count of each skill not found
            if not count[s]:
                # already used this player in a team
                continue
            # use this player
            count[s] -= 1
            # required skill for this players partner
            diffrence = target - s
            # if count of each skill not diffrence
            if not count[diffrence]:
                # no partner with the required skill exists
                return -1
            # add chemistry product of skills to result
            result += s * diffrence
            # use of the patner
            count[diffrence] -= 1
        # return sum of chemisty of all team
        return result

# Time Complexity : O(N)
# Space Complexity : O(N)