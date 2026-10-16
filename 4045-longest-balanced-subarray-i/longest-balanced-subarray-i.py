# Brute Force Code & Optimal Code
class Solution:
    def longestBalanced(self, nums: list[int]) -> int:
        # total number of elements in the array
        n = len(nums)
        # variable to store the maximum balanced subarray length
        maximum_length = 0
        # try every possible starting index
        for left in range(n):
            # sets to store the distinct even and odd numbers
            even = set()
            odd = set()
            # extend the subarray one element at a time
            for right in range(left, n):
                # add the current element to the appropriate set
                if nums[right] % 2 == 0:
                    even.add(nums[right])
                else:
                    odd.add(nums[right])
                # if the number of distinct even and odd elements is equal update the maximum length
                if len(even) == len(odd):
                    maximum_length = max(maximum_length,right - left + 1)
        # return the length of the longest balanced subarray
        return maximum_length

# Time Complexity : O(N)
# Space Complexity : O(N)