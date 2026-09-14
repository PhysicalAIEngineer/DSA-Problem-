# Brute Force Code & Optimal Code
class Solution:
    def maxWidthRamp(self, nums: list[int]) -> int:
        # total number of elements in the array
        n = len(nums)
        # maximum_right[i] stores the maximum value from index i to the end of the array
        maximum_right = [0] * n
        maximum_right[n - 1] = nums[n - 1]
        # build the maximum_right array by traversing from right to left
        for i in range(n - 2, -1, -1):
            maximum_right[i] = max(maximum_right[i + 1], nums[i])
        # variable to store the maximum ramp width
        maximum_ramp = 0
        # initialize two pointers
        # left  -> possible starting index of the ramp
        # right -> possible ending index of the ramp
        left = 0
        right = 0
        # traverse the array using the right pointer
        while right < n:
            # if nums[left] is greater than every value from right onward, move the left pointer until a valid ramp becomes possible
            while left < right and nums[left] > maximum_right[right]:
                left += 1
            # update the maximum ramp width
            maximum_ramp = max(maximum_ramp, right - left)
            # move to the next ending index
            right += 1
        # return the maximum ramp width found
        return maximum_ramp

# Time Complexity : O(N)
# Space Complexity : O(1)