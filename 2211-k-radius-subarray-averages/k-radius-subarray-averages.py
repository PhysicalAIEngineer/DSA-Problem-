# Optimal Code [Sliding Window]
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # number of element in the array
        n = len(nums)
        # if k = 0 the window contains only the current elements
        if k == 0:
            return nums
        # intially every position is -1 because complete window may not exits
        result = [-1] * n
        # size of the window k element on the left = centre element + k element on the right
        window_size = 2 * k + 1
        # if the array is smaller than the required window no valid average can be calculated
        if n < window_size:
            return result
        # left boundary of the first window
        left = 0
        # right boundary of the second widnow
        right = 2 * k
        # centre of first window
        centre = k
        # calculate the sum of the first windows
        window_sum = 0
        for i in range(left, right + 1):
            window_sum += nums[i]
        # calculate and store the average for the first valid centre
        result[centre] = window_sum // window_size
        # move the centre one position forwards
        centre += 1
        # move the right bounary one position forward
        right += 1
        # continue sliding window until the right bounary reaches the end
        while right < n:
            # element that is leaving the current window
            out_of_window = nums[left]
            # element that is entering the current window
            came_to_window = nums[right]
            # remove the element leaving the window and add the new element entering the window
            window_sum = (window_sum - out_of_window + came_to_window)
            # calculate the average for the new centre of the window
            result[centre] = window_sum // window_size
            # move the center forward
            centre += 1
            # move the left bounary forward
            left += 1
            # move the right bounary forwar
            right += 1
        # return all calculated averages
        return result 

# Time Complexity : O(N)
# Space Complexity : O(N)
