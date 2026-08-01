# Brute Force Code & Optimal Code
class Solution:
    # return whether each child can have the greatest number of candies after receiving all extra candies
    def kidsWithCandies(self,candies: list[int],
extraCandies: int) -> list[bool]:
        # find the maximum number of candies currently held by any child
        max_candies = max(candies)
        # store the result for each child
        result = []
        # check every child's candy count
        for candy in candies:
            # calculate how many candies this child would have after receiving all extra candies
            new_candy_count = candy + extraCandies
            # check whether the child would have at least as many candies as the child who currently has the most
            if new_candy_count >= max_candies:
                result.append(True)
            else:
                result.append(False)
        # return the result for all children
        return result

# Time Complexity : O(N)
# Space Complexity : O(N)