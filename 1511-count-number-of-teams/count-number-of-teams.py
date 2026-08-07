class Solution:
    def numTeams(self, rating: list[int]) -> int:
        # number of soldiers
        n = len(rating)
        # store the total number of valid teams
        teams = 0
        # treat rating[j] as the middle soldier for a team of 3 soldiers i < j < k so j can be the middle soldier from index 1 to n - 2.
        for j in range(1, n - 1):
            # count elements on the left of j
            # 1. number of ratings smaller than rating[j]
            count_smaller_left = 0
            # 2. number of ratings larger than rating[j]
            count_larger_left = 0
            # count elements on the right of j
            # 1. number of ratings smaller than rating[j]
            count_smaller_right = 0
            # 2. number of ratings larger than rating[j]
            count_larger_right = 0
            # check every soldier before j
            for i in range(j):
                # if rating[i] is smaller than rating[j] it can be the first soldier of an increasing team.
                if rating[i] < rating[j]:
                    count_smaller_left += 1
                # if rating[i] is larger than rating[j] it can be the first soldier of a decreasing team.
                elif rating[i] > rating[j]:
                    count_larger_left += 1
            # check every soldier after j
            for k in range(j + 1, n):
                # if rating[k] is larger than rating[j] it can be the third soldier of an increasing team.
                if rating[k] > rating[j]:
                    count_larger_right += 1
                # if rating[k] is smaller than rating[j] it can be the third soldier of a decreasing team.
                elif rating[k] < rating[j]:
                    count_smaller_right += 1
            # count increasing teams
            # rating[i] < rating[j] < rating[k]
            # So:
            # - choose any smaller element from the left
            # - choose any larger element from the right
            # number of increasing teams: smaller_left * larger_right
            # count decreasing teams
            # rating[i] > rating[j] > rating[k]
            # So:
            # - choose any larger element from the left
            # - choose any smaller element from the right
            # number of decreasing teams: larger_left * smaller_right
            teams += (count_larger_left * count_smaller_right + count_smaller_left * count_larger_right)
        # return the total number of valid teams
        return teams

# Time Complexity : O(N^2)
# Space Complexity : O(N)