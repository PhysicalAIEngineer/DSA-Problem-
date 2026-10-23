# Brute Force Code & Optimal Code
class Solution:
    def rob(self, nums: list[int]) -> int:
        # store the total number of houses
        n = len(nums)
        # edge case 1: if there is only one house rob it because there are no other houses that could be adjacent to its
        if n == 1:
            return nums[0]
        # edge case 2: if there are exactly two house they are adjacent therefore can rob only one of them choose the house containing the larger amount of money
        if n == 2:
            return max(nums[0], nums[1])
        # create memoization array of size 101 self.t[i] stores the maximum money can rob when considering houses starting at index i intially -1 means that answer has no been calculated
        self.t = [-1] * 101
        # define recurive helper function solve(i, end) return the maximum amount of money can rob from house i though house end inclusive end parameter limits the range of houses can considers
        def solve(i, end):
            # base case : if i has moved beynond the last allowed house there are no houses left to considers therfore no additional money can be collected
            if i > end:
                return 0
            # memoization check : if we have already calculated the answer for index i return the cached result instend of repeating the work this work here because each cell to solve uses fixed range during single sun reset the cache before running the second case
            if self.t[i] != -1:
                return self.t[i]
            # option 1: rob the current house
            # collect the money in house i because adjacent houses both be robbed skip house i + 1 and continue from house i + 2
            rob_current_house = nums[i] + solve(i + 2, end)
            # option 2: skip the current house
            # do not rob house i move to house i + 1 and calculte the maximum money obtainable from the remaining houses
            skip_current_house = solve(i + 1, end)
            # choose the better of the two options store the answer in the memoization array so it can be reused if the same index in encountered again
            self.t[i] = max(rob_current_house, skip_current_house)
            # return the maximum money obtainbles from index i onward 
            return self.t[i]
        # case 1 : exclude the last house
        # consider houses from index 0 though index n - 2 the first house is allowed but the last houe in excluded this remove the circular conflict between the first and last houses turning the remaining houses into a line
        exclude_last_house = solve(0, n - 2)
        # reset the memoization array before solving the second case this ensures that answer calculated for the first range are not incorrectly reused for the different range
        self.t = [-1] * 101
        # case 2 : exclude the first house
        # consider houses from index 1 though index n - 1 the first house is excluded but the last house is allowed this also removes the circular conflict and leaves a linear houses robber problem
        exclude_first_house = solve(1, n - 1)
        # optimal solution must belong to one of these cases : 1. exclude the last house & 2. exclude the first house return whichever case gives us more money
        return max(exclude_last_house, exclude_first_house)

# Time Complexity : O(N)
# Space Complexity : O(N)