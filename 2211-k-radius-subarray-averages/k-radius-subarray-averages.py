# Optimal Code (Prefix Sum)
class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        # number of elements in the array
        n = len(nums)
        # if k is zero the window contains only the current element itself
        if k  == 0:
            return nums
        # initally every possible is -1 because valid window may not exits
        result = [-1] * n
        # size of the window centeted at index i window contains k elements on both sides plus the centre elements
        window_size = 2 * k + 1
        # if the array is smaller than the required window no valid average can be calculated
        if n < window_size:
            return result
        # create the prefix sum array prefix_sum[i] stores the sum of nums[0...i]
        prefix_sum = [0] * n
        # prefix sum for the first element
        prefix_sum[0] = nums[0]
        # bulid the prefix sum array
        for i in range(1, n):
            prefix_sum[i] = (prefix_sum[i - 1] + nums[i])
        # only indices from k to n - k - 1 can have a complete window
        for i in range(k, n - k):
            # left bounday of the window
            left_idx = i - k
            # right boundary of the window
            right_idx = i + k
            # get the sum from index 0 though right index
            total = prefix_sum[right_idx]
            # remove the elements before left_idx to get only the current window sum
            if left_idx > 0:
                total -= prefix_sum[left_idx - 1]
            # calculate the interger averages
            avg = int(total / window_size)
            # store the average at the centre index
            result[i] = avg
        # return all k radius averages
        return result

# Time Complexity : O(N)
# Space Complexity : O(N) 