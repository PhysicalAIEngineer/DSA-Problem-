# Brute Force Code & Optimal Code 
class Solution:
    def rob(self, nums: list[int]) -> int:
        # store the total number of houses
        n = len(nums)
        # create a memoization array of size 101 self.t[i] stores the maximum amount of money can rob starting from house index i and continuing to the end intially every position contain -1 meaning that the answer for that index has not been calculated yet
        self.t = [-1] * 101
        # define recursive helper function solve(i) return the maximum money can rob starting from house i
        def solve(i):
            # base case : if i is greater than or equal to n there are no houses left to rob thefore no additional money can be collected so return 0
            if i >= n:
                return 0
            # memoization check : if self.t[i] is not -1 have already calculated the maximum money obtainable starting from house i return the sorted result instend of solving it again
            if self.t[i] != -1:
                return self.t[i]
            # option 1: take the current house 
            # rob house i and collect nums[i] because two adjacent houses cannot both be robbed we must skip house i + 1 and continue from house i + 2 total money for this option : money in current house + best money from house i + 2
            take_current_house = nums[i] + solve(i + 2)
            # option 2: skip the current house
            # do not rob house i move to the next house i + 1 and find the maximum money obtainable from that point onward
            skip_current_house = solve(i + 1)
            # choose the better option : compare the money obtained by taking the current house with the money obtained by skipping it store the larger value in self.t[i] so that this subproblem does not need to be calculated again
            self.t[i] = max(take_current_house, skip_current_house)
            # return the maximum money obtainable from house i onward
            return self.t[i]
        # start from house index 0 this calcaultes the maximum money that can be robbed from all houses without robbing two adjacent houses
        return solve (0)

# Time Complexity : O(N)
# Space Complexity : O(N)