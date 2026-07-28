# Optimal Code
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # calculate the total sum of all elements
        total_sum = sum(nums)
        # intialize variables for kadane algoritms to find the minimum subarray sum
        kadane_min = nums[0]
        current_min = nums[0]
        # intialize varibles for kadane algoritms to find the maximum subarray sum
        kadane_max = nums[0]
        current_max = nums[0]
        # traverse the remaining elements
        for i in range(1, len(nums)):
            # update the minimum subarray sum ending at the current index
            current_min = min(nums[i] + current_min, nums[i])
            # update the overall minimum subarray sum
            kadane_min = min(kadane_min, current_min)
            # update the maximum subarray sum ending at the current index
            current_max = max(nums[i] + current_max, nums[i])
            # update the overall maximum subarray sun
            kadane_max = max(kadane_max, current_max)
        # compute the maximum circular subarray sum by excluding the minimum subarray
        circular_sum = total_sum - kadane_min
        # if there is at least one positive number compare the normal and circular answers
        if kadane_max > 0:
            return max(kadane_max, circular_sum)
        # if all numbers are negative the circular sum becomes invalid so return the largest elements
        return kadane_max

# Time Complexity : O(N)
# Space Complexity : O(1)