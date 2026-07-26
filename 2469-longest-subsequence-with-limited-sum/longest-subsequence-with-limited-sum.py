# Optimal Code
class Solution:
    # perform binary search to find the maximum number of elements whose prefix sum is less than or equal to the target
    def binarySearch(self, nums: list[int], n: int, target: int) -> int:
        # initialize the search range
        left = 0
        right = n - 1
        # store the last valid index whose prefix sum is <= target
        result_idx = -1
        # perform binary search
        while left <= right:
            mid = left + (right - left) // 2
            # current prefix sum is valid so try to find a larger one
            if nums[mid] <= target:
                result_idx = mid
                left = mid + 1
            # current prefix sum is too large, search on the left side
            else:
                right = mid - 1
        # convert the last valid index into the number of elements
        return result_idx + 1
    # return the maximum subsequence length for each query
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        # total number of elements
        n = len(nums)
        # sort the array so that choosing the smallest elements gives the maximum subsequence length
        nums.sort()
        # convert the sorted array into a prefix sum array
        for i in range(1, n):
            nums[i] += nums[i - 1]
        # store the answer for each query
        result = []
        # process every query independently
        for target in queries:
            # find the maximum number of elements whose prefix sum does not exceed the target
            count = self.binarySearch(nums, n, target)
            # store the result
            result.append(count)
        # return the answers for all queries
        return result

# Time Complexity : O(N)
# Space Complexity : O(N)