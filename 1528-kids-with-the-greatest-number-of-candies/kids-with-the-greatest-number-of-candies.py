# Brute Force Code & Optimal Code
class Solution:
    # return whether each child can have the greatest number of candies after receiving all extra candies
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # find the maximum number of candies currently held by any child
        max_candies = max(candies)
        # store the result for each child
        result = []
        # check every child candy count
        for candy in candies:
            # calculte how many candies this child would have afterr receiving all extra candies
            new_candy_count = candy + extraCandies
            # check whether the child would have at least as many candies as the child whos currently has the most
            if new_candy_count >= max_candies:
                result.append(True)
            else:
                result.append(False)
        # return the result for all children
        return result 

# Time Complexity : O(N)
# Space Complexity : O(1)
        