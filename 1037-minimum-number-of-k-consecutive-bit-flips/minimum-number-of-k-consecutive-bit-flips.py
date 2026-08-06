# Brute Force Code & Optimal Code
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        # total number of elements in the array
        n = len(nums)
        # stores the total number of k bit flips performed
        flips = 0
        # is_flipped[i] = tree means flip operation start at index i
        is_flipped = [False] * n
        # number of flip operation that are currently affecting the current index
        active_flips = 0
        # traverse every element in the array
        for i in range(n):
            # if flip started at index (i - k) its effect ends before the current index so remove it from the active flip count
            if i >= k and is_flipped[i - k]:
                active_flips -= 1
            # determine the effective values at nums[i] if active_flips is even : current values remain unchanged & if active flip is odd : current values remain unchanged so, it the effective values is 0 must start a new flip here
            if active_flips % 2 == nums[i]:
                # not enough elements remain to perfrom k-length flip
                if i + k  > n:
                    return -1
                # start new flip at index i
                active_flips += 1
                # mark the flip starts 
                is_flipped[i] = True
                # increase the total flip count
                flips += 1
        # return the minimum number of flips required
        return flips

# Time Complexity : O(N)
# Space Complexity : O(N)