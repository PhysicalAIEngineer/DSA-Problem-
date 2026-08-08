# Optimal Code
class Solution:
    def longestSubarray(self, nums):
        # maximum value found so far
        maxVal = 0
        # longest streak of the maximum value
        result = 0
        # current consecutive streak
        streak = 0
        # traverse every number
        for num in nums:
            # found a new maximum value
            if num > maxVal:
                maxVal = num
                # reset the previous result because are now looking for the streak of this new maximum value
                result = 0
                streak = 0
            # current number is equal to the maximum value
            if maxVal == num:
                streak += 1
            # current number is not the maximum
            else:
                streak = 0
            # update the longest streak
            result = max(result, streak)
        return result

# Time Complexity : O(N)
# Space Complexity : O(1)