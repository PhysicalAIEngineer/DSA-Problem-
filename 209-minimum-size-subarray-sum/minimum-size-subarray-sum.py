#  Brute Force Code & Optimal Code
class Solution:
  def minSubArrayLen(self, target: int, nums: list[int]):
    # total number of element in the array
    n = len(nums)
    # intialize the sliding window pointer
    left = 0
    right = 0
    # variable to store the sum of the current window
    current_sum = 0
    # variable to store the minimum length of valid subarray
    minimum_length = n + 1
    # expand the sliding window using the right pointer
    while right < n:
      # include the current element in the window
      current_sum += nums[right]
      # when the current window sum is at least the target
      while current_sum >= target:
        # update the minimum length
        minimum_length = min(minimum_length, right - left + 1)
        # remove the leftmost element from the window
        current_sum -= nums[left]
        # slide the window to the right
        left += 1
      # slide the window to the right
      right += 1
    # if no valid subarray exists return 0 otherwise return the minimum length found
    return 0 if minimum_length == n + 1 else minimum_length

# Time Complexity : O(N)
# Space Complexity : O(1)