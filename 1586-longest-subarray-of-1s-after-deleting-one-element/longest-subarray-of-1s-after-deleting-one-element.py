# Brute Force Code & Optimal Code
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # variable to store the number of zeros in the current window
        zero_count = 0
        # variable to store the maximum length of valid subarray 
        longest_window = 0
        # left pointer of the sliding window
        left = 0
        # travese the array using the right pointer
        for right  in range(len(nums)):
            # include the current element in the sliding window
            if nums[right] == 0:
                zero_count += 1
            # shink the window until it contain at most one zero
            while zero_count > 1:
                # if zero leaves the window update the zero count
                if nums[left] == 0:
                    zero_count -= 1
                # move the left pointer to shrink the window
                left += 1
            # update the maximum valid length since one element must be deleted the window length is right - left
            longest_window = max(longest_window, right - left)
        # return the maximum length after deleting one element
        return longest_window

# Time Complexity : O(N)
# Space Complexity : O(N)