# Optimal Code 
class Solution:
    # compute the maximum height to the left of each index
    def getLeftMax(self, height: list[int], n: int):
        # store the maximum height from the left up to each index
        left_max = [0] * n
        # first bar is its own left maximum
        left_max[0] = height[0]
        # fill the left max 
        for i in range(1, n):
            # maximum height seen so far from the left
            left_max[i] = max(left_max[i- 1], height[i])
        # return the left maximum array
        return left_max
    # compute the maximum height to right of each index
    def getRightMax(self, height: list[int], n: int):
        # store the maxium height from right up to each index
        right_max = [0] * n
        # last bar is its own right maximum
        right_max[n - 1] = height[n - 1]
        # fil the right max by traversing from right to left
        for i in range(n - 2, -1, -1):
            # maximum height seen so far from the right
            right_max[i] = max(right_max[i + 1], height[i])
        # return the right maximum array
        return right_max
    def trap(self, height: List[int]) -> int:
        # total number of bars
        n = len(height)
        # less than two bars cannot trap water
        if n == 0 or n == 1:
            return 0
        # precompute the maximum heights on the left and right of every index
        left_max = self.getLeftMax(height, n)
        right_max = self.getRightMax(height, n)
        # store the total trapped water
        total_water = 0
        # calculate trapped water at every index
        for i in range(n):
            # water level is limited by the shorter of two boundaries
            total_water += min(left_max[i], right_max[i]) - height[i]
        # return the total trapped water
        return total_water

# Time Complexity : O(N)
# Space Complexity : O(N)