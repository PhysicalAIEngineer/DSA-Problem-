# Brute Force Code & Optimal Code
class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        # store the maximum time taken by any ant to fall off the plank
        result = 0
        # ants moving toward the left if an ant is at position x and moves left if needs x seconds to reach position 0 and fall off the plank
        for x in left:
            # keep the maximum falling times
            result = max(result, x)
        # ants moving toward the right if an ant is at position x and moves right it needs (n - x) to reach position n and fail off the plank
        for x in right:
            # calculate the time for this ant and keep the maximum times
            result = max(result, n - x)
        # last moment is the maximum time taken by any ant to fall off the plank
        return result

# Time Complexity : O(N)
# Space Complexity : O(N)
        