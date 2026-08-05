# Brute Force Code & Optimal Code
class Solution:
    def getSumAbsoluteDifferences(self, nums: list[int]) -> list[int]:
        # number of elements in the array
        n = len(nums)
        # create a prefix sum array so prefix_sum[i] stores the sum of all elements from index 0 to index i.
        prefix_sum = [0] * n
        # prefix sum for the first element
        prefix_sum[0] = nums[0]
        # build the remaining prefix sums
        for i in range(1, n):
            prefix_sum[i] = nums[i] + prefix_sum[i - 1]
        # store the final answer for every index
        result = [0] * n
        # calculate the answer for every nums[i]
        for i in range(n):
            # sum of all elements before nums[i] prefix_sum[i] contains: nums[0] + nums[1] + ... + nums[i] subtract nums[i] to get only the left side.
            left_sum = prefix_sum[i] - nums[i]
            # sum of all elements after nums[i] total sum - sum from index 0 to i
            right_sum = prefix_sum[n - 1] - prefix_sum[i]
            # number of elements on the left side
            left_count = i
            # number of elements on the right side
            right_count = n - i - 1
            # calculate absolute differences with left elements nums is sorted, so every element on the left is smaller than or equal to nums[i]. therefore: nums[i] - nums[j] for all left elements: (number of elements * nums[i]) - (sum of left elements)
            left_total = (left_count * nums[i] - left_sum)
            # calculate absolute differences with right elements nums is sorted, so every element on the right is greater than or equal to nums[i].
            # therefore: = nums[j] - nums[i] for all right elements: (sum of right elements) - (number of elements * nums[i])
            right_total = (right_sum - nums[i] * right_count)
            # total absolute difference for nums[i] = difference with left elements + difference with right elements
            result[i] = left_total + right_total
        # return the answer for every element
        return result

# Time Complexity : O(N)
# Space Complexity : O(N)